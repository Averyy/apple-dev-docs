# SFSpeechRecognitionRequest

**Framework**: Speech  
**Kind**: class

An abstract class that represents a request to recognize speech from an audio source.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class SFSpeechRecognitionRequest
```

#### Overview

Don’t create [`SFSpeechRecognitionRequest`](sfspeechrecognitionrequest.md) objects directly. Create an [`SFSpeechURLRecognitionRequest`](sfspeechurlrecognitionrequest.md) or [`SFSpeechAudioBufferRecognitionRequest`](sfspeechaudiobufferrecognitionrequest.md) object instead. Use the properties of this class to configure various aspects of your request object before you start the speech recognition process. For example, use the [`shouldReportPartialResults`](sfspeechrecognitionrequest/shouldreportpartialresults.md) property to specify whether you want partial results or only the final result of speech recognition.

## Topics

### Configuring a recognition request
- [var requiresOnDeviceRecognition: Bool](sfspeechrecognitionrequest/requiresondevicerecognition.md)
  A Boolean value that determines whether a request must keep its audio data on the device.
- [var shouldReportPartialResults: Bool](sfspeechrecognitionrequest/shouldreportpartialresults.md)
  A Boolean value that indicates whether you want intermediate results returned for each utterance.
- [var contextualStrings: [String]](sfspeechrecognitionrequest/contextualstrings.md)
  An array of phrases that should be recognized, even if they are not in the system vocabulary.
### Speech Type Classification
- [var taskHint: SFSpeechRecognitionTaskHint](sfspeechrecognitionrequest/taskhint.md)
  A value that indicates the type of speech recognition being performed.
- [enum SFSpeechRecognitionTaskHint](sfspeechrecognitiontaskhint.md)
  The type of task for which you are using speech recognition.
### Punctuation
- [var addsPunctuation: Bool](sfspeechrecognitionrequest/addspunctuation.md)
  A Boolean value that indicates whether to add punctuation to speech recognition results.
### Deprecated
- [var interactionIdentifier: String?](sfspeechrecognitionrequest/interactionidentifier.md)
  An identifier string that you use to describe the type of interaction associated with the speech recognition request.
### Instance Properties
- [var customizedLanguageModel: SFSpeechLanguageModel.Configuration?](sfspeechrecognitionrequest/customizedlanguagemodel.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SFSpeechAudioBufferRecognitionRequest](sfspeechaudiobufferrecognitionrequest.md)
- [SFSpeechURLRecognitionRequest](sfspeechurlrecognitionrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Recognizing speech in live audio](recognizing-speech-in-live-audio.md)
  Perform speech recognition on audio coming from the microphone of an iOS device.
- [class SFSpeechURLRecognitionRequest](sfspeechurlrecognitionrequest.md)
  A request to recognize speech in a recorded audio file.
- [class SFSpeechAudioBufferRecognitionRequest](sfspeechaudiobufferrecognitionrequest.md)
  A request to recognize speech from captured audio content, such as audio from the device’s microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest)*