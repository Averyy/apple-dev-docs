# volatileDomainNames

**Framework**: Foundation  
**Kind**: property

The current volatile domain names.

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

The domain names are represented as strings. You can get the contents of each domain by passing the returned domain names to the [`volatileDomain(forName:)`](userdefaults/volatiledomain(forname:).md) method.

## See Also

- [func volatileDomain(forName: String) -> [String : Any]](userdefaults/volatiledomain(forname:).md)
  Returns the dictionary for the specified volatile domain.
- [func setVolatileDomain([String : Any], forName: String)](userdefaults/setvolatiledomain(_:forname:).md)
  Sets the dictionary for the specified volatile domain.
- [func removeVolatileDomain(forName: String)](userdefaults/removevolatiledomain(forname:).md)
  Removes the specified volatile domain from the user’s defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/volatiledomainnames)*