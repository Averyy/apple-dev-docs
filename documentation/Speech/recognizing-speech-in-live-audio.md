# Recognizing speech in live audio

**Framework**: Speech

Perform speech recognition and transcription on audio captured from the microphone of an iOS device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

This sample project shows you how to use the Speech framework to transcribe or caption audio, and how to use a custom language model to add new vocabulary and improve the accuracy of the transcription.

When the user taps the Start Recording button, the SpokenWord app begins capturing audio from the device’s microphone, transcribes it using the Speech framework, and displays the transcription, continuously updating it until the user taps the Stop Recording button or the Pause/Resume button.

This sample uses [`CaptureInputSequenceProvider`](captureinputsequenceprovider.md) introduced in macOS and iOS 27; [`SpeechAnalyzer`](speechanalyzer.md), [`DictationTranscriber`](dictationtranscriber.md), and [`AssetInventory`](assetinventory.md) introduced in macOS and iOS 26; and [`SFCustomLanguageModelData`](sfcustomlanguagemodeldata.md) introduced in macOS 14 and iOS 17.

![A screenshot of the transcription process. On the left, the app lets the user know that it’s ready to begin transcription. On the right, the app displays what the user said.](/images/com.apple.speech/sample-screens_2x.png)

> **Note**: The sample app doesn’t run in the iOS Simulator, so you need to run it on a physical device with iOS or iPadOS 27 or later.

#### Configure the Speech Analyzer

When the user taps the Start Recording button, the app creates [`SpeechAnalyzer`](speechanalyzer.md) and [`DictationTranscriber`](dictationtranscriber.md) objects to generate the transcription.

The speech analyzer manages the flow of audio data through a processing pipeline composed of one or more modules. In this app, that’s the dictation transcriber module, which transcribes the audio into text.

```swift
let transcriber = createDictationTranscriber(locale: locale, lmConfiguration: customizedLanguageModelConfiguration)
let modules = [transcriber]
let analyzer = SpeechAnalyzer(modules: modules)
```

The transcriber module defines presets that bundle common configuration options together. The app uses the [`progressiveLongDictation`](dictationtranscriber/preset/progressivelongdictation.md) preset, which provides immediate preliminary transcriptions followed by more refined and accurate transcriptions as they become available.

The app also configures the transcriber with a content hint. Content hints help the transcriber understand the type of content being dictated, improving transcription accuracy. The [`customizedLanguage(modelConfiguration:)`](dictationtranscriber/contenthint/customizedlanguage(modelconfiguration:).md) hint provides the transcriber with the specialized chess vocabulary described in the [`Customize the language model`](https://developer.apple.com#customize-the-language-model) section below, helping to ensure that the app transcribes that vocabulary correctly.

```swift
let preset = DictationTranscriber.Preset.progressiveLongDictation

// Set customized language model if one is given.
let contentHints = if let lmConfiguration {
    preset.contentHints.union([.customizedLanguage(modelConfiguration: lmConfiguration)])
} else {
    preset.contentHints
}

return DictationTranscriber(
    locale: locale,
    contentHints: contentHints,
    transcriptionOptions: preset.transcriptionOptions,
    reportingOptions: preset.reportingOptions,
    attributeOptions: preset.attributeOptions
)
```

#### Configure the Capture Session

When the user taps the Start Recording button, the app starts a capture session managed by an [`AVCaptureSession`](https://developer.apple.com/documentation/avfoundation/avcapturesession) instance.

First, the app selects an audio source. The app records audio from the default microphone, which may be the device’s built-in microphone or an external device. The app selects the [`AVCaptureDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice) object corresponding to that microphone.

```swift
guard let captureDevice = AVCaptureDevice.default(.microphone, for: .audio, position: .unspecified) else {
    throw TranscriptionError.couldNotCaptureMicrophone
}
```

Then, the app sets up the capture session and audio conversion pipeline using the selected audio source.

The speech analyzer processes audio taken from an asynchronous sequence; the app must convert the audio to a format that the transcriber module can work with and add it to that sequence. The app uses [`CaptureInputSequenceProvider`](captureinputsequenceprovider.md) to do that. This class sets up a capture session, audio conversion pipeline, and asynchronous sequence that are compatible with the speech analyzer and transcriber module. The provider also configures the session automatically, eliminating the need to install audio engine taps to convert and route audio buffers.

```swift
let provider = try await CaptureInputSequenceProvider.providerWithSession(from: captureDevice, compatibleWith: modules)
```

An app may also configure a capture session independently. The input sequence provider can supply an output destination object that the app can add to its session.

Finally, the app saves a reference to the [`AVCaptureSession`](https://developer.apple.com/documentation/avfoundation/avcapturesession) instance created by the provider in the view controller’s `captureSession` property, and uses that to manage the session later. To avoid concurrency-related compilation errors, the app actually saves the session instance in an actor and manages the session through that actor.

#### Analyze Audio and Display Results

The app does its primary work in the `runSession` method. This work consists of two subtasks:

- Analyzing audio from the capture session
- Displaying transcription updates from the transcriber module

The app adds the subtasks to a task group in `runSession`. The task group uses Swift’s structured concurrency mechanism to ensure that both subtasks run to completion before `runSession` returns.

```swift
try await withThrowingDiscardingTaskGroup() { group in
    // Subtask 1: Analyze audio from the capture session
    group.addTask {
        try await self.captureAndAnalyzeAudio(
            transcriber: transcriber,
            captureSession: captureSession,
            audioSequence: audioSequence
        )
    }

    // Subtask 2: Display transcription updates from the transcriber module
    group.addTask {
        // This cancellation shield prevents the transcription update loop from immediately ending
        // when the `stopRecording()` method cancels the recording task.
        try await withTaskCancellationShield {
            try await self.updateTranscription(transcriber: transcriber)
        }
    }
}
```

To perform the first subtask — analyzing audio — the app gets audio from the capture session in the form of an asynchronous sequence and passes that sequence to the speech analyzer. The app gets audio through the input sequence provider’s [`analyzerInputs`](captureinputsequenceprovider/analyzerinputs.md) property. This property is an asynchronous sequence, populated as audio is captured and converted. The app passes this sequence to the speech analyzer’s [`analyzeSequence(_:)`](speechanalyzer/analyzesequence(_:).md) method. The speech analyzer and transcriber module consume newly added audio from the sequence and transcribe that audio as soon as possible.

```swift
let lastAudioTime = try await analyzer.analyzeSequence(audioSequence)
if let lastAudioTime {
    try await analyzer.finalizeAndFinish(through: lastAudioTime)
}
```

To perform the second subtask — displaying transcriptions — the app gets an update from the transcriber module, incorporates it into an overall transcript, and displays that transcript in the UI. The app gets updates from the transcriber module’s [`results`](dictationtranscriber/results.md) property. The transcriber module provides an update moments after a new batch of audio becomes available.

```swift
let transcriptsSequence = transcriber.results.map { @MainActor transcriberResult in
    return self.updateTranscript(with: transcriberResult)
}
```

The transcriber module doesn’t accumulate an overall transcription. Instead, it provides a number of results for different audio time ranges. The app incorporates each update into an overall transcription and replaces the currently displayed transcription with the new one.

Since the app uses the transcriber module’s [`progressiveLongDictation`](dictationtranscriber/preset/progressivelongdictation.md) preset, some results replace previous results. The app uses the audio time range of each result to determine if part of the overall transcript needs to be replaced.

```swift
if let rangeToReplace = transcript.rangeOfAudioTimeRangeAttributes(intersecting: resultTimeRange) {
    transcript.replaceSubrange(rangeToReplace, with: resultTranscript)
} else {
    transcript.append(resultTranscript)
}
```

This technique is straightforward, but another common technique is to maintain two separate transcriptions: one containing finalized results that won’t be replaced, and another containing volatile results that are expected to be replaced. When a result is final, it is added to the first transcript; when a result is volatile, it replaces all or part of the second transcript. The overall transcript in this scenario, then, consists of the first transcript followed by the current second transcript.

If the app didn’t need to provide immediate UI feedback, it could configure the transcriber to only provide final results, and just append each result to the overall transcript, further simplifying the code.

#### Stop the Capture Session

The app calls the `runSession` method in an overall recording task, saving a reference to that task in the view controller’s `recordingTask` property. When the user taps the Stop Recording button, the app simply cancels that task. Because the recording task’s subtasks are in a task group, the recording task doesn’t actually end until both subtasks finish cleanly and `runSession` returns.

Task cancellation is cooperative in Swift. While the app allows the cancellation of the first subtask, it shields the second subtask from cancellation.

In the first subtask (which analyzes audio), the canceled [`analyzeSequence(_:)`](speechanalyzer/analyzesequence(_:).md) method immediately stops analyzing additional audio and returns, and then the app calls [`finalizeAndFinish(through:)`](speechanalyzer/finalizeandfinish(through:).md) to get a final update and end the analysis. After the transcriber module adds that final update to its [`results`](dictationtranscriber/results.md) sequence, it terminates the sequence. Then the app stops the capture session and finishes that subtask.

The second subtask (which displays transcriptions) is shielded from cancellation and so it continues reading from the results sequence until it reads the final update and finds the end of the sequence, at which point the app finishes that subtask. Without the cancellation shield, the second subtask stops reading the sequence immediately, before the transcriber module adds its final updates.

The app cancels the recording task when the user taps the stop button, but it’s not the only way to implement the app. An alternative is to fully end the capture session, ending the audio sequence, after which the [`analyzeSequence(_:)`](speechanalyzer/analyzesequence(_:).md) method returns as in the cancellation case. However, a capture session can start, stop, and restart many times, so the only way to fully end a capture session is to release all references to it and let it deallocate.

Because it’s easy to overlook a stray reference, cancellation is the more reliable approach. But an app that uses another kind of audio sequence, such as one obtained from an [`AssetInputSequenceProvider`](assetinputsequenceprovider.md) or one that the app itself creates, can simply finish the analysis session after the audio sequence ends and [`analyzeSequence(_:)`](speechanalyzer/analyzesequence(_:).md) returns normally.

#### Prepare to Record and Transcribe Speech

When the app launches, it uses [`AssetInventory`](assetinventory.md) to ensure that any necessary transcription assets install. If the assets aren’t present on the device, it downloads them.

```swift
let transcriber = createDictationTranscriber(locale: locale, lmConfiguration: lmConfiguration)
if let request = try await AssetInventory.assetInstallationRequest(supporting: [transcriber]) {
    try await request.downloadAndInstall()
}
```

The app also prepares a customized language model that adds specialized chess terms to the transcription. The process of building this language model is described below.

```swift
try await SFSpeechLanguageModel.prepareCustomLanguageModel(for: trainingData, configuration: lmConfiguration)
```

Finally, the app asks the user for permission to record using `requestAccess(for:completionHandler:)`.

```swift
guard await AVCaptureDevice.requestAccess(for: .audio) else {
    throw TranscriptionError.micPermissionDenied
}
```

#### Customize the Language Model

Developers can enhance the [`DictationTranscriber`](dictationtranscriber.md) transcriber module for specific use cases and applications by customizing its language model. This sample uses language model customization to improve accuracy when recognizing certain chess moves. The high-level steps in this process are:

- Training data generation
- Training data preparation
- Transcriber configuration

This sample includes a command-line utility named `datagenerator` that generates a training data file, and includes the file itself (named `CustomLMData (en_US).bin`) in the sample app’s bundle. The `datagenerator` utility uses [`SFCustomLanguageModelData`](sfcustomlanguagemodeldata.md) to generate this file from training data described by its result builder DSL.

Training data samples can include exact phrases that the app is likely to encounter.

```swift
SFCustomLanguageModelData.PhraseCount(phrase: "Play the Albin counter gambit", count: 10)
```

The training data generator can also define phrases using templates, which expand automatically to provide a large number of exact phrases.

```swift
SFCustomLanguageModelData.PhraseCountsFromTemplates(classes: [
    "piece": ["pawn", "rook", "knight", "bishop", "queen", "king"],
    "royal": ["queen", "king"],
    "rank": Array(1...8).map({ String($0) })
]) {
    SFCustomLanguageModelData.TemplatePhraseCountGenerator.Template(
        "<piece> to <royal> <piece> <rank>",
        count: 10_000
    )
}
```

An app that uses specialized terminology can also define custom vocabulary, complete with pronunciation information.

```swift
SFCustomLanguageModelData.CustomPronunciation(grapheme: "Winawer", phonemes: ["w I n aU @r"])
SFCustomLanguageModelData.CustomPronunciation(grapheme: "Tartakower", phonemes: ["t A r t @ k aU @r"])

SFCustomLanguageModelData.PhraseCount(phrase: "Play the Winawer variation", count: 10)
SFCustomLanguageModelData.PhraseCount(phrase: "Play the Tartakower", count: 10)
```

The remaining high-level steps — training data preparation and transcriber configuration — are described in sections above.

## See Also

- [Speech updates](../updates/speech.md)
  Learn about important changes to Speech.
- [Bringing advanced speech-to-text capabilities to your app](bringing-advanced-speech-to-text-capabilities-to-your-app.md)
  Learn how to incorporate live speech-to-text transcription into your app with SpeechAnalyzer.
- [actor SpeechAnalyzer](speechanalyzer.md)
  Analyzes spoken audio content in various ways and manages the analysis session.
- [class AssetInventory](assetinventory.md)
  Manages the assets that are necessary for transcription or other analyses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/recognizing-speech-in-live-audio)*