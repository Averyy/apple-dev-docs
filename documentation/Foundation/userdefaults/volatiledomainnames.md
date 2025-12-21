# volatileDomainNames

**Framework**: Foundation  
**Kind**: property

An array of identifiers for the volatile domains associated with the current object.

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
var volatileDomainNames: [String] { get }
```

#### Discussion

Each string in the array corresponds to one of the volatile domains this `UserDefaults` object searches. To get the contents of one of these domains, call the [`volatileDomain(forName:)`](userdefaults/volatiledomain(forname:).md) method.

## See Also

- [class let argumentDomain: String](userdefaults/argumentdomain.md)
  The identifier for the domain that contains command-line settings.
- [class let globalDomain: String](userdefaults/globaldomain.md)
  The identifier for the domain that contains system-specified settings for all apps.
- [class let registrationDomain: String](userdefaults/registrationdomain.md)
  The identifier for the domain that contains your app’s registered default values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/volatiledomainnames)*