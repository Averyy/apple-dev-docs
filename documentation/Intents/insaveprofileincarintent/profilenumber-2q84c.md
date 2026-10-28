# profileNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The profile index in which to save the settings.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 10.0+ - Deprecated in 15.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@nonobjc
final var profileNumber: Int? { get }
```

## Discussion

If your vehicle saves profile information using defined indexes, use this property to get the integer index of the profile slot to use.

## See Also

### Getting the Profile Information
- [var profileName: String?](./profilename.md)
  The name to assign to the profile.
- [var profileLabel: String?](./profilelabel.md)
  The name to assign to the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insaveprofileincarintent/profilenumber-2q84c)*