# authorizationStatus()

**Framework**: Speech  
**Kind**: method

Returns your app’s current authorization to perform speech recognition.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func authorizationStatus() -> SFSpeechRecognizerAuthorizationStatus
```

#### Return Value

The app’s current authorization status value. For a list of values, see [`SFSpeechRecognizerAuthorizationStatus`](sfspeechrecognizerauthorizationstatus.md).

#### Discussion

The user can reject your app’s request to perform speech recognition, but your request can also be denied if speech recognition is not supported on the device. The app can also change your app’s authorization status at any time from the Settings app.

## See Also

- [class func requestAuthorization((SFSpeechRecognizerAuthorizationStatus) -> Void)](sfspeechrecognizer/requestauthorization(_:).md)
  Asks the user to allow your app to perform speech recognition.
- [enum SFSpeechRecognizerAuthorizationStatus](sfspeechrecognizerauthorizationstatus.md)
  The app’s authorization to perform speech recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/authorizationstatus())*