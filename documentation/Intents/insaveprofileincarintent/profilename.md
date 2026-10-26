# profileName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name to assign to the profile.

**Availability**:
- iOS 10.2+ - Deprecated in 15.0
- iPadOS 10.2+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var profileName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * profileName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * profileName;
```

#### Discussion

Use this property if your vehicle supports saving named profiles.

## See Also

### Getting the Profile Information
- [var profileNumber: Int?](./profilenumber-2q84c.md)
  The profile index in which to save the settings.
- [var profileLabel: String?](./profilelabel.md)
  The name to assign to the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insaveprofileincarintent/profilename)*