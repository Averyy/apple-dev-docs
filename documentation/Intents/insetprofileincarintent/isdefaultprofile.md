# isDefaultProfile

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to make the profile the default profile.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 10.0+ - Deprecated in 15.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var isDefaultProfile: Bool? { get }
```

#### Discussion

When the value in this property is [`true`](../../Swift/true.md), the user wants to make the profile the default profile for the vehicle.

## See Also

### Getting the Profile Information
- [var profileName: String?](./profilename.md)
  The name assigned to the profile.
- [var profileNumber: Int?](./profilenumber-37vj8.md)
  The profile index from which to restore the settings.
- [var profileLabel: String?](./profilelabel.md)
  The name assigned to the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintent/isdefaultprofile)*