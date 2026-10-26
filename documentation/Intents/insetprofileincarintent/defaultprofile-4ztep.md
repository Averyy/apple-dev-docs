# defaultProfile

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to make the profile the default profile.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * defaultProfile;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * defaultProfile;
```

#### Discussion

When the value in this property is [`true`](../../Swift/true.md), the user wants to make the profile the default profile for the vehicle.

## See Also

### Getting the Profile Information
- [var profileName: String?](./profilename.md)
  The name assigned to the profile.
- [var profileLabel: String?](./profilelabel.md)
  The name assigned to the profile.
- [profileNumber](./profilenumber-50f30.md)
  The profile index from which to restore the settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintent/defaultprofile-4ztep)*