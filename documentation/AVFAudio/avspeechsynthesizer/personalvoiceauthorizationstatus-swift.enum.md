# AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVSpeechSynthesisPersonalVoiceAuthorizationStatus : NSUInteger;
```

## Topics

### Creating an authorization status
- [init?(rawValue: UInt)](./personalvoiceauthorizationstatus-swift.enum/init%28rawvalue%29.md)
### Checking authorization status
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus.authorized](./personalvoiceauthorizationstatus-swift.enum/authorized.md)
  The user granted your app’s request to use personal voices.
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus.denied](./personalvoiceauthorizationstatus-swift.enum/denied.md)
  The user denied your app’s request to use personal voices.
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus.notDetermined](./personalvoiceauthorizationstatus-swift.enum/notdetermined.md)
  The app hasn’t requested authorization to use personal voices.
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus.unsupported](./personalvoiceauthorizationstatus-swift.enum/unsupported.md)
  The device doesn’t support personal voices.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enabling personal voices
- [class var personalVoiceAuthorizationStatus: AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus](./personalvoiceauthorizationstatus-swift.type.property.md)
  Your app’s authorization to use personal voices.
- [class let availableVoicesDidChangeNotification: NSNotification.Name](./availablevoicesdidchangenotification.md)
  A notification that indicates a change in available voices for speech synthesis.
- [class func requestPersonalVoiceAuthorization(completionHandler: (AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus) -> Void)](./requestpersonalvoiceauthorization%28completionhandler%29.md)
  Prompts the user to authorize your app to use personal voices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/personalvoiceauthorizationstatus-swift.enum)*