# registrationDomain

**Framework**: Foundation  
**Kind**: property

The identifier for the domain that contains your app’s registered default values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let registrationDomain: String
```

## Mentions

- [Accessing settings from your code](accessing-settings-from-your-code.md)

#### Discussion

The settings in this domain represent default values you want to use for its settings. To register your app’s default settings, call the [`register(defaults:)`](userdefaults/register(defaults:).md) method shortly after launch.

## See Also

- [class let argumentDomain: String](userdefaults/argumentdomain.md)
  The identifier for the domain that contains command-line settings.
- [class let globalDomain: String](userdefaults/globaldomain.md)
  The identifier for the domain that contains system-specified settings for all apps.
- [var volatileDomainNames: [String]](userdefaults/volatiledomainnames.md)
  An array of identifiers for the volatile domains associated with the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/registrationdomain)*