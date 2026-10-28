# registrationDomain

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```c
extern NSString * const NSRegistrationDomain;
```

## Mentions

- [Accessing settings from your code](../accessing-settings-from-your-code.md)

## Discussion

The settings in this domain represent default values you want to use for its settings. To register your app’s default settings, call the [`register(defaults:)`](./register%28defaults%29.md) method shortly after launch.

## See Also

### Getting the domain names
- [class let argumentDomain: String](./argumentdomain.md)
  The identifier for the domain that contains command-line settings.
- [class let globalDomain: String](./globaldomain.md)
  The identifier for the domain that contains system-specified settings for all apps.
- [var volatileDomainNames: [String]](./volatiledomainnames.md)
  An array of identifiers for the volatile domains associated with the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/registrationdomain)*