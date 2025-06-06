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

You can perform speech recognition in many languages, but each [`SFSpeechRecognizer`](sfspeechrecognizer.md) object operates on a single language. On-device speech recognition is available for some languages, but the framework also relies on Apple’s servers for speech recognition. Always assume that performing speech recognition requires a network connection.

## Topics

### Essentials
- [Asking Permission to Use Speech Recognition](asking-permission-to-use-speech-recognition.md)
  Ask the user’s permission to perform speech recognition using Apple’s servers.
- [class SFSpeechRecognizer](sfspeechrecognizer.md)
  An object you use to check for the availability of the speech recognition service, and to initiate the speech recognition process.
### Audio sources
- [Recognizing speech in live audio](recognizing-speech-in-live-audio.md)
  Perform speech recognition on audio coming from the microphone of an iOS device.
- [class SFSpeechURLRecognitionRequest](sfspeechurlrecognitionrequest.md)
  A request to recognize speech in a recorded audio file.
- [class SFSpeechAudioBufferRecognitionRequest](sfspeechaudiobufferrecognitionrequest.md)
  A request to recognize speech from captured audio content, such as audio from the device’s microphone.
- [class SFSpeechRecognitionRequest](sfspeechrecognitionrequest.md)
  An abstract class that represents a request to recognize speech from an audio source.
### In-progress requests
- [class SFSpeechRecognitionTask](sfspeechrecognitiontask.md)
  A task object for monitoring the speech recognition progress.
### Transcription results
- [class SFSpeechRecognitionResult](sfspeechrecognitionresult.md)
  An object that contains the partial or final results of a speech recognition request.
- [class SFSpeechRecognitionMetadata](sfspeechrecognitionmetadata.md)
  The metadata of speech in the audio of a speech recognition request.
- [class SFTranscription](sftranscription.md)
  A textual representation of the specified speech in its entirety, as recognized by the speech recognizer.
- [class SFTranscriptionSegment](sftranscriptionsegment.md)
  A discrete part of an entire transcription, as identified by the speech recognizer.
### Voice analytics
- [class SFVoiceAnalytics](sfvoiceanalytics.md)
  A collection of vocal analysis metrics.
### Structures
- [struct SFSpeechError](sfspeecherror.md)
### Classes
- [class SFCustomLanguageModelData](sfcustomlanguagemodeldata.md)
- [class SFSpeechLanguageModel](sfspeechlanguagemodel.md)
- [SFSpeechLanguageModel.Configuration](sfspeechlanguagemodel/configuration.md)
### Protocols
- [protocol DataInsertable](datainsertable.md)
- [protocol TemplateInsertable](templateinsertable.md)
### Reference
- [Speech Enumerations](speech-enumerations.md)
  Constants that specify types of speech recognition, the state of a recognition task, and the status of the authorization request.
- [Speech Constants](speech-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Speech)*