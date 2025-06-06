# SFSpeechRecognizer

**Framework**: Speech  
**Kind**: class

An object you use to check for the availability of the speech recognition service, and to initiate the speech recognition process.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class SFSpeechRecognizer
```

## Mentions

- [Asking Permission to Use Speech Recognition](asking-permission-to-use-speech-recognition.md)

#### Overview

An [`SFSpeechRecognizer`](sfspeechrecognizer.md) object is the central object for managing the speech recognizer process. Use this object to:

- Request authorization to use speech recognition services.
- Specify the language to use during the recognition process.
- Initiate new speech recognition tasks.

##### Set Up Speech Recognition

Each speech recognizer supports only one language, which you specify at creation time. The successful creation of a speech recognizer does not guarantee that speech recognition services are available. For some languages, the recognizer might require an Internet connection. Use the [`isAvailable`](sfspeechrecognizer/isavailable.md) property to find out if speech recognition services are available for the current language.

To initiate the speech recognition process, do the following:

1. Request authorization to use speech recognition. See [`Asking Permission to Use Speech Recognition`](asking-permission-to-use-speech-recognition.md).
2. Create an [`SFSpeechRecognizer`](sfspeechrecognizer.md) object.
3. Verify the availability of services using the [`isAvailable`](sfspeechrecognizer/isavailable.md) property of your speech recognizer object.
4. Prepare your audio content.
5. Create a recognition request object—an object that descends from [`SFSpeechRecognitionRequest`](sfspeechrecognitionrequest.md).
6. Call the [`recognitionTask(with:delegate:)`](sfspeechrecognizer/recognitiontask(with:delegate:).md) or [`recognitionTask(with:resultHandler:)`](sfspeechrecognizer/recognitiontask(with:resulthandler:).md) method to begin the recognition process.

The type of recognition request object you create depends on whether you are processing an existing audio file or an incoming stream of audio. For existing audio files, create a [`SFSpeechURLRecognitionRequest`](sfspeechurlrecognitionrequest.md) object. For audio streams, create a [`SFSpeechAudioBufferRecognitionRequest`](sfspeechaudiobufferrecognitionrequest.md) object.

##### Create a Great User Experience for Speech Recognition

Here are some tips to consider when adding speech recognition support to your app.

-  Because speech recognition is a network-based service, limits are enforced so that the service can remain freely available to all apps. Individual devices may be limited in the number of recognitions that can be performed per day, and each app may be throttled globally based on the number of requests it makes per day. If a recognition request fails quickly (within a second or two of starting), check to see if the recognition service became unavailable. If it is, you may want to ask users to try again later.
-  Speech recognition places a relatively high burden on battery life and network usage. To minimize this burden, the framework stops speech recognition tasks that last longer than one minute. This limit is similar to the one for keyboard-related dictation.
-  For example, display a visual indicator and play sounds at the beginning and end of speech recognition to help users understand that they’re being actively recorded. You can also display speech as it is being recognized so that users understand what your app is doing and see any mistakes made during the recognition process.
-  Some speech is not appropriate for recognition. Don’t send passwords, health or financial data, and other sensitive speech for recognition.

## Topics

### Creating a Speech Recognizer
- [convenience init?()](sfspeechrecognizer/init.md)
  Creates a speech recognizer associated with the user’s default language settings.
- [init?(locale: Locale)](sfspeechrecognizer/init(locale:).md)
  Creates a speech recognizer associated with the specified locale.
### Monitoring the Availability of Speech Recognition
- [var delegate: (any SFSpeechRecognizerDelegate)?](sfspeechrecognizer/delegate.md)
  The delegate object that handles changes to the availability of speech recognition services.
- [protocol SFSpeechRecognizerDelegate](sfspeechrecognizerdelegate.md)
  A protocol that you adopt in your objects to track the availability of a speech recognizer.
- [var isAvailable: Bool](sfspeechrecognizer/isavailable.md)
  A Boolean value that indicates whether the speech recognizer is currently available.
- [var supportsOnDeviceRecognition: Bool](sfspeechrecognizer/supportsondevicerecognition.md)
  A Boolean value that indicates whether the speech recognizer can operate without network access.
### Requesting Authorization from the User
- [class func requestAuthorization((SFSpeechRecognizerAuthorizationStatus) -> Void)](sfspeechrecognizer/requestauthorization(_:).md)
  Asks the user to allow your app to perform speech recognition.
- [class func authorizationStatus() -> SFSpeechRecognizerAuthorizationStatus](sfspeechrecognizer/authorizationstatus.md)
  Returns your app’s current authorization to perform speech recognition.
- [enum SFSpeechRecognizerAuthorizationStatus](sfspeechrecognizerauthorizationstatus.md)
  The app’s authorization to perform speech recognition.
### Configuring the Speech Recognizer
- [var defaultTaskHint: SFSpeechRecognitionTaskHint](sfspeechrecognizer/defaulttaskhint.md)
  A hint that indicates the type of speech recognition being requested.
- [var queue: OperationQueue](sfspeechrecognizer/queue.md)
  The queue on which to execute recognition task handlers and delegate methods.
### Performing Speech Recognition on Audio
- [func recognitionTask(with: SFSpeechRecognitionRequest, resultHandler: (SFSpeechRecognitionResult?, (any Error)?) -> Void) -> SFSpeechRecognitionTask](sfspeechrecognizer/recognitiontask(with:resulthandler:).md)
  Executes the speech recognition request and delivers the results to the specified handler block.
- [func recognitionTask(with: SFSpeechRecognitionRequest, delegate: any SFSpeechRecognitionTaskDelegate) -> SFSpeechRecognitionTask](sfspeechrecognizer/recognitiontask(with:delegate:).md)
  Recognizes speech from the audio source associated with the specified request, using the specified delegate to manage the results.
- [protocol SFSpeechRecognitionTaskDelegate](sfspeechrecognitiontaskdelegate.md)
  A protocol with methods for managing multi-utterance speech recognition requests.
### Getting the Current Language
- [var locale: Locale](sfspeechrecognizer/locale.md)
  The locale of the speech recognizer.
- [class func supportedLocales() -> Set<Locale>](sfspeechrecognizer/supportedlocales.md)
  Returns the set of locales that are supported by the speech recognizer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Asking Permission to Use Speech Recognition](asking-permission-to-use-speech-recognition.md)
  Ask the user’s permission to perform speech recognition using Apple’s servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer)*