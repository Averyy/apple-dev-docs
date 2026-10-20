# requestPersonalVoiceAuthorization(completionHandler:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Type Method

Prompts the user to authorize your app to use personal voices.

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
class func requestPersonalVoiceAuthorization(completionHandler handler: @escaping @Sendable (AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus) -> Void)
```

```swift
class func requestPersonalVoiceAuthorization() async -> AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus
```

```objc
+ (void) requestPersonalVoiceAuthorizationWithCompletionHandler:(void (^)(AVSpeechSynthesisPersonalVoiceAuthorizationStatus status)) handler;
```

#### Discussion

## Parameters

- `handler`: A completion handler that the system calls after the user responds to a request to authorize use of personal voices, which receives the authorization status as an argument.

## See Also

### Enabling personal voices
- [class var personalVoiceAuthorizationStatus: AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus](./personalvoiceauthorizationstatus-swift.type.property.md)
  Your app’s authorization to use personal voices.
- [class let availableVoicesDidChangeNotification: NSNotification.Name](./availablevoicesdidchangenotification.md)
  A notification that indicates a change in available voices for speech synthesis.
- [AVSpeechSynthesizer.PersonalVoiceAuthorizationStatus](./personalvoiceauthorizationstatus-swift.enum.md)
  An enumeration that models the personal voices authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/requestpersonalvoiceauthorization(completionhandler:))*