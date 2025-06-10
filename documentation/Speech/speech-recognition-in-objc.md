# Speech Recognition in Objective-C

**Framework**: Speech

Use these classes to perform speech recognition in Objective-C code.

## Topics

### Essentials
- [Asking Permission to Use Speech Recognition](asking-permission-to-use-speech-recognition.md)
  Ask the user’s permission to perform speech recognition using Apple’s servers.
- [class SFSpeechRecognizer](sfspeechrecognizer.md)
  An object you use to check for the availability of the speech recognition service, and to initiate the speech recognition process.
- [protocol SFSpeechRecognizerDelegate](sfspeechrecognizerdelegate.md)
  A protocol that you adopt in your objects to track the availability of a speech recognizer.
- [enum SFSpeechRecognitionTaskHint](sfspeechrecognitiontaskhint.md)
  The type of task for which you are using speech recognition.
- [enum SFSpeechRecognizerAuthorizationStatus](sfspeechrecognizerauthorizationstatus.md)
  The app’s authorization to perform speech recognition.
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
- [protocol SFSpeechRecognitionTaskDelegate](sfspeechrecognitiontaskdelegate.md)
  A protocol with methods for managing multi-utterance speech recognition requests.
- [enum SFSpeechRecognitionTaskState](sfspeechrecognitiontaskstate.md)
  The state of the task associated with the recognition request.
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
- [class SFAcousticFeature](sfacousticfeature.md)
  The value of a voice analysis metric.
### Errors
- [let SFSpeechErrorDomain: String](sfspeecherrordomain.md)
- [struct SFSpeechError](sfspeecherror.md)
- [SFSpeechError.Code](sfspeecherror/code.md)
  Error codes that can be thrown under the Speech framework’s error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speech-recognition-in-objc)*