# removeVolatileDomain(forName:)

**Framework**: Foundation  
**Kind**: method

Removes the specified volatile domain from the user’s defaults.

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
func removeVolatileDomain(forName domainName: String)
```

## Parameters

- `domainName`: The volatile domain you want to remove.

## See Also

- [var volatileDomainNames: [String]](userdefaults/volatiledomainnames.md)
  The current volatile domain names.
- [func volatileDomain(forName: String) -> [String : Any]](userdefaults/volatiledomain(forname:).md)
  Returns the dictionary for the specified volatile domain.
- [func setVolatileDomain([String : Any], forName: String)](userdefaults/setvolatiledomain(_:forname:).md)
  Sets the dictionary for the specified volatile domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/removevolatiledomain(forname:))*