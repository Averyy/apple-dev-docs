# Speech

**Framework**: Speech  
**Kind**: module

Perform speech recognition on live or prerecorded audio, and receive transcriptions, alternative interpretations, and confidence levels of the results.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

#### Overview

Use the Speech framework to recognize spoken words in recorded or live audio. The keyboard’s dictation support uses speech recognition to translate audio content into text. This framework provides a similar behavior, except that you can use it without the presence of the keyboard. For example, you might use speech recognition to recognize verbal commands or to handle text dictation in other parts of your app.

The framework provides a class, [`SpeechAnalyzer`](speechanalyzer.md), and a number of  that can be added to the analyzer to provide specific types of analysis and transcription. Many use cases only need a [`SpeechTranscriber`](speechtranscriber.md) module, which provides speech-to-text transcriptions.

The `SpeechAnalyzer` class is responsible for:

- Holding associated modules
- Accepting audio speech input
- Controlling the overall analysis

Each module is responsible for:

- Providing guidance on input that it can accept
- Providing its analysis or transcription output

The framework makes extensive use of Swift concurrency features, so be familiar with them. In particular, where an Objective C API might use a delegate to provide results to you, the Swift API’s modules provides their results via an `AsyncSequence`. Similarly, you provide speech input to this API via an `AsyncSequence` created and populated by you.

##### Perform Analysis

To perform analysis on audio files and streams, follow these general steps:

1. Create and configure the modules you want to use.
2. Create the input sequence you will use to provide speakers’ audio.
3. Create and configure the analyzer with the modules and input sequence.
4. Supply audio.
5. Perform analysis.
6. Act on results.
7. Finish analysis when desired.

This example shows how you could perform an analysis that transcribes audio using the `SpeechTranscriber` module:

```swift
import Speech

// Step 1: Modules
guard let locale = SpeechTranscriber.supportedLocale(equivalentTo: Locale.current) else {
    /* Note unsupported language */
}
let transcriber = SpeechTranscriber(locale: locale, preset: .offlineTranscription)

// Step 2: Input sequence
let (inputSequence, inputBuilder) = AsyncStream.makeStream(of: AnalyzerInput.self)

// Step 3: Analyzer
let audioFormat = await SpeechAnalyzer.bestAvailableAudioFormat(compatibleWith: [transcriber])
let analyzer = SpeechAnalyzer(inputSequence: inputSequence, modules: [transcriber])

// Step 4: Supply audio
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

// Step 6: Act on results
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

// Step 5: Perform analysis
let lastSampleTime = try await analyzer.analyzeSequence(inputSequence)

// Step 7: Finish analysis
if let lastSampleTime {
    try await analyzer.finalizeAndFinish(through: lastSampleTime)
} else {
    try analyzer.cancelAndFinishNow()
}
```

The framework includes powerful features not illustrated above. Here are some of them.

- [`analyzeSequence(from:)`](speechanalyzer/analyzesequence(from:).md)
- [`AttributeScopes.SpeechAttributes.TimeRangeAttribute`](https://developer.apple.com/documentation/Foundation/AttributeScopes/SpeechAttributes/TimeRangeAttribute)
- [`setModules(_:)`](speechanalyzer/setmodules(_:).md)
- [`prepareToAnalyze(in:withProgressReadyHandler:)`](speechanalyzer/preparetoanalyze(in:withprogressreadyhandler:).md)
- [`init(buffer:bufferStartTime:)`](analyzerinput/init(buffer:bufferstarttime:).md)
- [`finalize(through:)`](speechanalyzer/finalize(through:).md)

##### Manage Language Assets

The framework provides a class, [`AssetInventory`](assetinventory.md), through which you can manage the assets that are necessary for transcription or other analyses.

These assets are managed by the system. Once you download, install, or use an asset, the system will retain and update it automatically. The asset is shared with other applications.

The system makes a certain number of asset allocations available to your application. When your application no longer needs a particular asset, call [`deallocate(locale:)`](assetinventory/deallocate(locale:).md) to free that allocation.

## Topics

### Essentials
- [Bringing advanced speech-to-text capabilities to your app](bringing-advanced-speech-to-text-capabilities-to-your-app.md)
  Learn how to incorporate live speech-to-text transcription into your app with SpeechAnalyzer.
- [actor SpeechAnalyzer](speechanalyzer.md)
  Analyzes spoken audio content in various ways and manages the analysis session.
- [class AssetInventory](assetinventory.md)
  Before using `SpeechAnalyzer`, you must install the assets required by the modules you use. These assets are machine-learning models downloaded from Apple’s servers.
### Modules
- [protocol SpeechModule](speechmodule.md)
  Protocol that all analyzer modules conform to.
- [protocol LocaleDependentSpeechModule](localedependentspeechmodule.md)
  If a module conforms to this protocol, then its assets depend on the locale setting.
- [class SpeechTranscriber](speechtranscriber.md)
  A module that transcribes speech to text. This transcriber is appropriate for normal conversation and general purposes.
- [class DictationTranscriber](dictationtranscriber.md)
  A module that transcribes speech to text. This transcriber is used by `SFSpeechRecognizer` and system dictation features.
- [class SpeechDetector](speechdetector.md)
  A module that performs a voice activity detection (VAD) analysis.
### Input and output
- [struct AnalyzerInput](analyzerinput.md)
  Time-coded audio data.
- [protocol SpeechModuleResult](speechmoduleresult.md)
  Protocol that all module results conform to.
### Custom vocabulary
- [class AnalysisContext](analysiscontext.md)
  Contextual information that may be shared among analyzers.
- [class SFCustomLanguageModelData](sfcustomlanguagemodeldata.md)
  An object that generates and exports custom language model training data.
- [class SFSpeechLanguageModel](sfspeechlanguagemodel.md)
  A language model built from custom training data.
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.
- [protocol DataInsertable](datainsertable.md)
  A protocol supporting the custom language model training data result builder.
- [protocol TemplateInsertable](templateinsertable.md)
  A protocol supporting the custom language model training data result builder.
### Asset and resource management
- [enum SpeechModels](speechmodels.md)
  Namespace for methods related to model management.
- [class AssetInstallationRequest](assetinstallationrequest.md)
  An object that describes, downloads, and installs a selection of assets.
### Legacy API
- [Speech Recognition in Objective-C](speech-recognition-in-objc.md)
  Use these classes to perform speech recognition in Objective-C code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Speech)*