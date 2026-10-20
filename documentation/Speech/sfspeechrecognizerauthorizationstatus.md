# SFSpeechRecognizerAuthorizationStatus

**Framework**: Speech  
**Kind**: enum  
**Role**: Enumeration

The app’s authorization to perform speech recognition.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum SFSpeechRecognizerAuthorizationStatus
```

```c
enum SFSpeechRecognizerAuthorizationStatus : NSInteger;
```

## Topics

### Authorization statuses
- [SFSpeechRecognizerAuthorizationStatus.notDetermined](./sfspeechrecognizerauthorizationstatus/notdetermined.md)
  The app’s authorization status has not yet been determined.
- [SFSpeechRecognizerAuthorizationStatus.denied](./sfspeechrecognizerauthorizationstatus/denied.md)
  The user denied your app’s request to perform speech recognition.
- [SFSpeechRecognizerAuthorizationStatus.restricted](./sfspeechrecognizerauthorizationstatus/restricted.md)
  The device prevents your app from performing speech recognition.
- [SFSpeechRecognizerAuthorizationStatus.authorized](./sfspeechrecognizerauthorizationstatus/authorized.md)
  The user granted your app’s request to perform speech recognition.
### Initializers
- [init?(rawValue: Int)](./sfspeechrecognizerauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Essentials
- [Asking Permission to Use Speech Recognition](./asking-permission-to-use-speech-recognition.md)
  Ask the user’s permission to perform speech recognition using Apple’s servers.
- [class SFSpeechRecognizer](./sfspeechrecognizer.md)
  An object you use to check for the availability of the speech recognition service, and to initiate the speech recognition process.
- [protocol SFSpeechRecognizerDelegate](./sfspeechrecognizerdelegate.md)
  A protocol that you adopt in your objects to track the availability of a speech recognizer.
- [enum SFSpeechRecognitionTaskHint](./sfspeechrecognitiontaskhint.md)
  The type of task for which you are using speech recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizerauthorizationstatus)*