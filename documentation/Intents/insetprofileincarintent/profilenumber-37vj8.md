# profileNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The profile index from which to restore the settings.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 10.0+ - Deprecated in 15.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
final var profileNumber: Int? { get }
```

#### Discussion

If your vehicle saves profile information using defined indexes, use this property to get the integer index of the profile slot from which to retrieve the settings.

## See Also

### Getting the Profile Information
- [var isDefaultProfile: Bool?](./isdefaultprofile.md)
  A Boolean value indicating whether to make the profile the default profile.
- [var profileName: String?](./profilename.md)
  The name assigned to the profile.
- [var profileLabel: String?](./profilelabel.md)
  The name assigned to the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintent/profilenumber-37vj8)*