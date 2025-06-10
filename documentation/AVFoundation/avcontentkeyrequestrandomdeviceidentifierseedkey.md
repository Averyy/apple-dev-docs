# AVContentKeyRequestRandomDeviceIdentifierSeedKey

**Framework**: AVFoundation  
**Kind**: var

Value is an NSData containing a 16-byte seed to randomize the user’s deviceID contained in the SPC blob during FairPlay key exchange

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
let AVContentKeyRequestRandomDeviceIdentifierSeedKey: String
```

#### Discussion

This property must be used in conjunction with AVContentKeyRequestShouldRandomizeDeviceIdentifierKey. Use a RND function to generate a 16 byte seed. This seed will be used to randomize the user’s anonymized device ID if AVContentKeyRequestShouldRandomizeDeviceIdentifierKey is true. Content providers use the SPC to distinguish the playback device from other devices, typically to enforce per-screen business rule limits. If the app developer, in cooperation with the content vendor, does not require to distinguish the playback device, they can further enhance user privacy by making this identifier non-constant, using this option. In either case, apps are not allowed to store or use the FairPlay anonymized device ID for anything other than to enforce business rule limits. App developers must use the AppTrackingTransparency framework to disclose to users if the application or the related FairPlay Key Server collect data about end users and share it with other companies for purposes of tracking across apps and web sites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequestrandomdeviceidentifierseedkey)*