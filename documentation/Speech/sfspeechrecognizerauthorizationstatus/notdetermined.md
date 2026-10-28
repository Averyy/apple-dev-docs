# SFSpeechRecognizerAuthorizationStatus.notDetermined

**Framework**: Speech  
**Kind**: case  
**Role**: Case

The app’s authorization status has not yet been determined.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case notDetermined
```

```c
SFSpeechRecognizerAuthorizationStatusNotDetermined
```

## Discussion

When your app’s status is not determined, calling the [`requestAuthorization(_:)`](../sfspeechrecognizer/requestauthorization%28_%29.md) method prompts the user to grant or deny authorization.

## See Also

### Authorization statuses
- [SFSpeechRecognizerAuthorizationStatus.denied](./denied.md)
  The user denied your app’s request to perform speech recognition.
- [SFSpeechRecognizerAuthorizationStatus.restricted](./restricted.md)
  The device prevents your app from performing speech recognition.
- [SFSpeechRecognizerAuthorizationStatus.authorized](./authorized.md)
  The user granted your app’s request to perform speech recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizerauthorizationstatus/notdetermined)*