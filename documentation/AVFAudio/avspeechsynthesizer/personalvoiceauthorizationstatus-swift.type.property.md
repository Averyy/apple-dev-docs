# personalVoiceAuthorizationStatus

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

Your app’s authorization to use personal voices.

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
class var personalVoiceAuthorizationStatus: AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus { get }
```

```objc
@property (class, nonatomic, readonly) AVSpeechSynthesisPersonalVoiceAuthorizationStatus personalVoiceAuthorizationStatus;
```

#### Discussion

The user can grant or deny your app’s request to use personal voices when they’re initially prompted, and change the authorization in the Settings app. Additionally, the framework denies the request if the device doesn’t support using personal voices.

## See Also

### Enabling personal voices
- [class let availableVoicesDidChangeNotification: NSNotification.Name](./availablevoicesdidchangenotification.md)
  A notification that indicates a change in available voices for speech synthesis.
- [class func requestPersonalVoiceAuthorization(completionHandler: (AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus) -> Void)](./requestpersonalvoiceauthorization%28completionhandler%29.md)
  Prompts the user to authorize your app to use personal voices.
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus](./personalvoiceauthorizationstatus-swift.enum.md)
  An enumeration that models the personal voices authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/personalvoiceauthorizationstatus-swift.type.property)*