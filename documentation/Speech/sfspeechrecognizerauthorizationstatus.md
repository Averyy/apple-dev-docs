# SFSpeechRecognizerAuthorizationStatus

**Framework**: Speech  
**Kind**: enum

The app’s authorization to perform speech recognition.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum SFSpeechRecognizerAuthorizationStatus
```

## Topics

### Authorization Statuses
- [SFSpeechRecognizerAuthorizationStatus.notDetermined](sfspeechrecognizerauthorizationstatus/notdetermined.md)
  The app’s authorization status has not yet been determined.
- [SFSpeechRecognizerAuthorizationStatus.denied](sfspeechrecognizerauthorizationstatus/denied.md)
  The user denied your app’s request to perform speech recognition.
- [SFSpeechRecognizerAuthorizationStatus.restricted](sfspeechrecognizerauthorizationstatus/restricted.md)
  The device prevents your app from performing speech recognition.
- [SFSpeechRecognizerAuthorizationStatus.authorized](sfspeechrecognizerauthorizationstatus/authorized.md)
  The user granted your app’s request to perform speech recognition.
### Initializers
- [init?(rawValue: Int)](sfspeechrecognizerauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func requestAuthorization((SFSpeechRecognizerAuthorizationStatus) -> Void)](sfspeechrecognizer/requestauthorization(_:).md)
  Asks the user to allow your app to perform speech recognition.
- [class func authorizationStatus() -> SFSpeechRecognizerAuthorizationStatus](sfspeechrecognizer/authorizationstatus.md)
  Returns your app’s current authorization to perform speech recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizerauthorizationstatus)*