# argumentDomain

**Framework**: Foundation  
**Kind**: property

The identifier for the domain that contains command-line settings.

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
class let argumentDomain: String
```

#### Discussion

When someone launches your app from Xcode or the command-line, they can override setting values using command-line arguments. The defaults system stores those overrides in this domain, which is volatile and resets with each app launch. Values in this domain override most other domains, including your app-specific settings.

To specify custom settings from the command line, add the `-default` parameter to your command-line invocation followed by a  string with the key and value you want to set.

## See Also

- [class let globalDomain: String](userdefaults/globaldomain.md)
  The identifier for the domain that contains system-specified settings for all apps.
- [class let registrationDomain: String](userdefaults/registrationdomain.md)
  The identifier for the domain that contains your app’s registered default values.
- [var volatileDomainNames: [String]](userdefaults/volatiledomainnames.md)
  An array of identifiers for the volatile domains associated with the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/argumentdomain)*