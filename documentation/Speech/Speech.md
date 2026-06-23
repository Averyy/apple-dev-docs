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

The [`SpeechTranscriber`](speechtranscriber.md) class and other module classes provide specific services. The [`AssetInventory`](assetinventory.md) class ensures that the system has the assets necessary to support those classes. The [`SpeechAnalyzer`](speechanalyzer.md) class manages an analysis session that uses those classes. The [`AssetInputSequenceProvider`](assetinputsequenceprovider.md) and [`CaptureInputSequenceProvider`](captureinputsequenceprovider.md) classes provide audio from files or microphone devices.

For a general understanding of how you use these classes together, see [`SpeechAnalyzer`](speechanalyzer.md).

## Topics

### Essentials
- [Speech updates](../Updates/Speech.md)
  Learn about important changes to Speech.
- [Recognizing speech in live audio](recognizing-speech-in-live-audio.md)
  Perform speech recognition and transcription on audio captured from the microphone of an iOS device.
- [Bringing advanced speech-to-text capabilities to your app](bringing-advanced-speech-to-text-capabilities-to-your-app.md)
  Learn how to incorporate live speech-to-text transcription into your app with SpeechAnalyzer.
- [actor SpeechAnalyzer](speechanalyzer.md)
  Analyzes spoken audio content in various ways and manages the analysis session.
- [class AssetInventory](assetinventory.md)
  Manages the assets that are necessary for transcription or other analyses.
### Modules
- [class SpeechTranscriber](speechtranscriber.md)
  A speech-to-text transcription module that’s appropriate for normal conversation and general purposes.
- [class DictationTranscriber](dictationtranscriber.md)
  A speech-to-text transcription module that’s similar to system dictation features and compatible with older devices.
- [class SpeechDetector](speechdetector.md)
  A module that performs a voice activity detection (VAD) analysis.
- [protocol SpeechModule](speechmodule.md)
  Protocol that all analyzer modules conform to.
- [protocol LocaleDependentSpeechModule](localedependentspeechmodule.md)
  A module that requires locale-specific assets.
### Input and output
- [struct AnalyzerInput](analyzerinput.md)
  Time-coded audio data.
- [protocol SpeechModuleResult](speechmoduleresult.md)
  Protocol that all module results conform to.
### Audio sources
- [class AssetInputSequenceProvider](assetinputsequenceprovider.md)
  Reads from an audio file or asset, providing its audio in a format suitable for analysis by a speech analyzer.
- [class CaptureInputSequenceProvider](captureinputsequenceprovider.md)
  Reads from an AV capture device such as a microphone, providing the captured audio in a format suitable for analysis by a speech analyzer.
- [class AnalyzerInputConverter](analyzerinputconverter.md)
  Converts audio buffers to a format suitable for analysis by a speech analyzer.
### Custom vocabulary
- [class AnalysisContext](analysiscontext.md)
  Contextual information that may be shared among analyzers.
- [class SFSpeechLanguageModel](sfspeechlanguagemodel.md)
  A language model built from custom training data.
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)
  An object describing the location of a custom language model and specialized vocabulary.
- [class SFCustomLanguageModelData](sfcustomlanguagemodeldata.md)
  An object that generates and exports custom language model training data.
### Asset and resource management
- [class AssetInstallationRequest](assetinstallationrequest.md)
  An object that describes, downloads, and installs a selection of assets.
- [enum SpeechModels](speechmodels.md)
  Namespace for methods related to model management.
### Legacy API
- [Speech Recognition in Objective-C](speech-recognition-in-objc.md)
  Use these classes to perform speech recognition in Objective-C code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Speech)*