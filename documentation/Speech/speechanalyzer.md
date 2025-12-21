# SpeechAnalyzer

**Framework**: Speech  
**Kind**: class

Analyzes spoken audio content in various ways and manages the analysis session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final actor SpeechAnalyzer
```

#### Overview

The Speech framework provides several modules that can be added to an analyzer to provide specific types of analysis and transcription. Many use cases only need a [`SpeechTranscriber`](speechtranscriber.md) module, which performs speech-to-text transcriptions.

The `SpeechAnalyzer` class is responsible for:

- Holding associated modules
- Accepting audio speech input
- Controlling the overall analysis

Each module is responsible for:

- Providing guidance on acceptable input
- Providing its analysis or transcription output

Analysis is asynchronous. Input, output, and session control are decoupled and typically occur over several different tasks created by you or by the session. In particular, where an Objective-C API might use a delegate to provide results to you, the Swift API’s modules provides their results via an `AsyncSequence`. Similarly, you provide speech input to this API via an `AsyncSequence` you create and populate.

The analyzer can only analyze one input sequence at a time.

##### Perform Analysis

To perform analysis on audio files and streams, follow these general steps:

1. Create and configure the necessary modules.
2. Ensure the relevant assets are installed or already present. See [`AssetInventory`](assetinventory.md).
3. Create an input sequence you can use to provide the spoken audio.
4. Create and configure the analyzer with the modules and input sequence.
5. Supply audio.
6. Start analysis.
7. Act on results.
8. Finish analysis when desired.

This example shows how you could perform an analysis that transcribes audio using the `SpeechTranscriber` module:

```swift
import Speech

// Step 1: Modules
guard let locale = SpeechTranscriber.supportedLocale(equivalentTo: Locale.current) else {
    /* Note unsupported language */
}
let transcriber = SpeechTranscriber(locale: locale, preset: .offlineTranscription)

// Step 2: Assets
if let installationRequest = try await AssetInventory.assetInstallationRequest(supporting: [transcriber]) {
    try await installationRequest.downloadAndInstall()
}

// Step 3: Input sequence
let (inputSequence, inputBuilder) = AsyncStream.makeStream(of: AnalyzerInput.self)

// Step 4: Analyzer
let audioFormat = await SpeechAnalyzer.bestAvailableAudioFormat(compatibleWith: [transcriber])
let analyzer = SpeechAnalyzer(modules: [transcriber])

// Step 5: Supply audio
Task {
    while /* audio remains */ {
        /* Get some audio */
        /* Convert to audioFormat */
        let pcmBuffer = /* an AVAudioPCMBuffer containing some converted audio */
        let input = AnalyzerInput(buffer: pcmBuffer)
        inputBuilder.yield(input)
    }
    inputBuilder.finish()
}

// Step 7: Act on results
Task {
    do {
        for try await result in transcriber.results {
            let bestTranscription = result.text // an AttributedString
            let plainTextBestTranscription = String(bestTranscription.characters) // a String
            print(plainTextBestTranscription)
        }
    } catch {
        /* Handle error */
    }
}

// Step 6: Perform analysis
let lastSampleTime = try await analyzer.analyzeSequence(inputSequence)

// Step 8: Finish analysis
if let lastSampleTime {
    try await analyzer.finalizeAndFinish(through: lastSampleTime)
} else {
    try analyzer.cancelAndFinishNow()
}
```

##### Analyze Audio Files

To analyze one or more audio files represented by an `AVAudioFile` object, call methods such as [`analyzeSequence(from:)`](speechanalyzer/analyzesequence(from:).md) or [`start(inputAudioFile:finishAfterFile:)`](speechanalyzer/start(inputaudiofile:finishafterfile:).md), or create the analyzer with one of the initializers that has a file parameter. These methods automatically convert the file to a supported audio format and process the file in its entirety.

To end the analysis session after one file, pass `true` for the `finishAfterFile` parameter or call one of the `finish` methods.

Otherwise, by default, the analyzer won’t terminate its result streams and will wait for additional audio files or buffers. The analysis session doesn’t reset the audio timeline after each file; the next audio is assumed to come immediately after the completed file.

##### Analyze Audio Buffers

To analyze audio buffers directly, convert them to a supported audio format, either on the fly or in advance. You can use [`bestAvailableAudioFormat(compatibleWith:)`](speechanalyzer/bestavailableaudioformat(compatiblewith:).md) or individual modules’ [`availableCompatibleAudioFormats`](speechmodule/availablecompatibleaudioformats.md) methods to select a format to convert to.

Create an [`AnalyzerInput`](analyzerinput.md) object for each audio buffer and add the object to an input sequence you create. Supply that input sequence to [`analyzeSequence(_:)`](speechanalyzer/analyzesequence(_:).md), [`start(inputSequence:)`](speechanalyzer/start(inputsequence:).md), or a similar parameter of the analyzer’s initializer.

To skip past part of an audio stream, omit the buffers you want to skip from the input sequence. When you resume analysis with a later buffer, you can ensure the time-code of each module’s result accounts for the skipped audio. To do this, pass the later buffer’s time-code within the audio stream as the `bufferStartTime` parameter of the later `AnalyzerInput` object.

##### Analyze Autonomously

You can and usually should perform analysis using the [`analyzeSequence(_:)`](speechanalyzer/analyzesequence(_:).md) or [`analyzeSequence(from:)`](speechanalyzer/analyzesequence(from:).md) methods; those methods work well with Swift structured concurrency techniques. However, you may prefer that the analyzer proceed independently and perform its analysis autonomously as audio input becomes available in a task managed by the analyzer itself.

To use this capability, create the analyzer with one of the initializers that has an input sequence or file parameter, or call [`start(inputSequence:)`](speechanalyzer/start(inputsequence:).md) or [`start(inputAudioFile:finishAfterFile:)`](speechanalyzer/start(inputaudiofile:finishafterfile:).md). To end the analysis when the input ends, call [`finalizeAndFinishThroughEndOfInput()`](speechanalyzer/finalizeandfinishthroughendofinput().md). To end the analysis of that input and start analysis of different input, call one of the `start` methods again.

##### Control Processing and Timing of Results

Modules deliver results periodically, but you can manually synchronize their processing and delivery to outside cues.

To deliver a result for a particular time-code, call [`finalize(through:)`](speechanalyzer/finalize(through:).md). To cancel processing of results that are no longer of interest, call [`cancelAnalysis(before:)`](speechanalyzer/cancelanalysis(before:).md).

##### Improve Responsiveness

By default, the analyzer and modules load the system resources that they require lazily, and unload those resources when they’re deallocated.

To proactively load system resources and “preheat” the analyzer, call [`prepareToAnalyze(in:)`](speechanalyzer/preparetoanalyze(in:).md) after setting its modules. This may improve how quickly the modules return their first results.

To delay or prevent unloading an analyzer’s resources — caching them for later use by a different analyzer instance — you can select a [`SpeechAnalyzer.Options.ModelRetention`](speechanalyzer/options/modelretention-swift.enum.md) option and create the analyzer with an appropriate [`SpeechAnalyzer.Options`](speechanalyzer/options.md) object.

To set the priority of analysis work, create the analyzer with a [`SpeechAnalyzer.Options`](speechanalyzer/options.md) object given a `priority` value.

Specific modules may also offer options that improve responsiveness.

##### Finish Analysis

To end an analysis session, you must use one of the analyzer’s `finish` methods or parameters, or deallocate the analyzer.

When the analysis session transitions to the  state:

- The analyzer won’t take additional input from the input sequence
- Most methods won’t do anything; in particular, the analyzer won’t accept different input sequences or modules
- Module result streams terminate and modules won’t publish additional results, though the app can continue to iterate over already-published results

> **Note**: While you can terminate the input sequence you created with a method such as `AsyncStream.Continuation.finish()`, finishing the input sequence does  cause the analysis session to become finished, and you can continue the session with a different input sequence.

##### Respond to Errors

When the analyzer or its modules’ result streams throw an error, the analysis session becomes finished as described above, and the same error (or a `CancellationError`) is thrown from all waiting methods and result streams.

## Topics

### Creating an analyzer
- [convenience init(modules: [any SpeechModule], options: SpeechAnalyzer.Options?)](speechanalyzer/init(modules:options:).md)
  Creates an analyzer.
- [convenience init<InputSequence>(inputSequence: InputSequence, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?)](speechanalyzer/init(inputsequence:modules:options:analysiscontext:volatilerangechangedhandler:).md)
  Creates an analyzer and begins analysis.
- [convenience init(inputAudioFile: AVAudioFile, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, finishAfterFile: Bool, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?) async throws](speechanalyzer/init(inputaudiofile:modules:options:analysiscontext:finishafterfile:volatilerangechangedhandler:).md)
  Creates an analyzer and begins analysis on an audio file.
- [SpeechAnalyzer.Options](speechanalyzer/options.md)
  Analysis processing options.
### Managing modules
- [func setModules([any SpeechModule]) async throws](speechanalyzer/setmodules(_:).md)
  Adds or removes modules.
- [var modules: [any SpeechModule]](speechanalyzer/modules.md)
  The modules performing analysis on the audio input.
### Performing analysis
- [func analyzeSequence<InputSequence>(InputSequence) async throws -> CMTime?](speechanalyzer/analyzesequence(_:).md)
  Analyzes an input sequence, returning when the sequence is consumed.
- [func analyzeSequence(from: AVAudioFile) async throws -> CMTime?](speechanalyzer/analyzesequence(from:).md)
  Analyzes an input sequence created from an audio file, returning when the file has been read.
### Performing autonomous analysis
- [func start<InputSequence>(inputSequence: InputSequence) async throws](speechanalyzer/start(inputsequence:).md)
  Starts analysis of an input sequence and returns immediately.
- [func start(inputAudioFile: AVAudioFile, finishAfterFile: Bool) async throws](speechanalyzer/start(inputaudiofile:finishafterfile:).md)
  Starts analysis of an input sequence created from an audio file and returns immediately.
### Finalizing and cancelling results
- [func cancelAnalysis(before: CMTime)](speechanalyzer/cancelanalysis(before:).md)
  Stops analyzing audio predating the given time.
- [func finalize(through: CMTime?) async throws](speechanalyzer/finalize(through:).md)
  Finalizes the modules’ analyses.
### Finishing analysis
- [func cancelAndFinishNow() async](speechanalyzer/cancelandfinishnow.md)
  Finishes analysis immediately.
- [func finalizeAndFinishThroughEndOfInput() async throws](speechanalyzer/finalizeandfinishthroughendofinput.md)
  Finishes analysis after an audio input sequence has been fully consumed and its results are finalized.
- [func finalizeAndFinish(through: CMTime) async throws](speechanalyzer/finalizeandfinish(through:).md)
  Finishes analysis after finalizing results for a given time-code.
- [func finish(after: CMTime) async throws](speechanalyzer/finish(after:).md)
  Finishes analysis once input for a given time is consumed.
### Determining audio formats
- [static func bestAvailableAudioFormat(compatibleWith: [any SpeechModule]) async -> AVAudioFormat?](speechanalyzer/bestavailableaudioformat(compatiblewith:).md)
  Retrieves the best-quality audio format that the specified modules can work with, from assets installed on the device.
- [static func bestAvailableAudioFormat(compatibleWith: [any SpeechModule], considering: AVAudioFormat?) async -> AVAudioFormat?](speechanalyzer/bestavailableaudioformat(compatiblewith:considering:).md)
  Retrieves the best-quality audio format that the specified modules can work with, taking into account the natural format of the audio and assets installed on the device.
### Improving responsiveness
- [func prepareToAnalyze(in: AVAudioFormat?) async throws](speechanalyzer/preparetoanalyze(in:).md)
  Prepares the analyzer to begin work with minimal startup delay.
- [func prepareToAnalyze(in: AVAudioFormat?, withProgressReadyHandler: sending ((Progress) -> Void)?) async throws](speechanalyzer/preparetoanalyze(in:withprogressreadyhandler:).md)
  Prepares the analyzer to begin work with minimal startup delay, reporting the progress of that preparation.
### Monitoring analysis
- [func setVolatileRangeChangedHandler(sending ((CMTimeRange, Bool, Bool) -> Void)?)](speechanalyzer/setvolatilerangechangedhandler(_:).md)
  A closure that the analyzer calls when the volatile range changes.
- [var volatileRange: CMTimeRange?](speechanalyzer/volatilerange.md)
  The range of results that can change.
### Managing contexts
- [func setContext(AnalysisContext) async throws](speechanalyzer/setcontext(_:).md)
  Sets contextual information to improve or inform the analysis.
- [var context: AnalysisContext](speechanalyzer/context.md)
  An object containing contextual information.

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Bringing advanced speech-to-text capabilities to your app](bringing-advanced-speech-to-text-capabilities-to-your-app.md)
  Learn how to incorporate live speech-to-text transcription into your app with SpeechAnalyzer.
- [class AssetInventory](assetinventory.md)
  Manages the assets that are necessary for transcription or other analyses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer)*