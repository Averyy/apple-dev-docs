# AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus

**Framework**: AVFAudio  
**Kind**: enum

An enumeration that models the personal voices authorization status.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum PersonalVoiceAuthorizationStatus
```

## Topics

### Authorization statuses
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus.authorized](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum/authorized.md)
  The user granted your app’s request to use personal voices.
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus.denied](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum/denied.md)
  The user denied your app’s request to use personal voices.
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus.notDetermined](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum/notdetermined.md)
  The app hasn’t requested authorization to use personal voices.
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus.unsupported](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum/unsupported.md)
  The device doesn’t support personal voices.
### Initializers
- [init?(rawValue: UInt)](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class var personalVoiceAuthorizationStatus: AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus](avspeechsynthesizer/personalvoiceauthorizationstatus-swift.type.property.md)
  Your app’s authorization to use personal voices.
- [class let availableVoicesDidChangeNotification: NSNotification.Name](avspeechsynthesizer/availablevoicesdidchangenotification.md)
  A notification that indicates a change in available voices for speech synthesis.
- [class func requestPersonalVoiceAuthorization(completionHandler: (AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus) -> Void)](avspeechsynthesizer/requestpersonalvoiceauthorization(completionhandler:).md)
  Prompts the user to authorize your app to use personal voices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum)*