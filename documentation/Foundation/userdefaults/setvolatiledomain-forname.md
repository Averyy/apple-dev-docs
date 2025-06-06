# setVolatileDomain(_:forName:)

**Framework**: Foundation  
**Kind**: method

Sets the dictionary for the specified volatile domain.

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
func setVolatileDomain(_ domain: [String : Any], forName domainName: String)
```

#### Discussion

This method raises an `NSInvalidArgumentException` if a volatile domain with the specified name already exists.

## Parameters

- `domain`: The dictionary of keys and values you want to assign to the domain.
- `domainName`: The domain whose keys and values you want to set.

## See Also

- [var volatileDomainNames: [String]](userdefaults/volatiledomainnames.md)
  The current volatile domain names.
- [func volatileDomain(forName: String) -> [String : Any]](userdefaults/volatiledomain(forname:).md)
  Returns the dictionary for the specified volatile domain.
- [func removeVolatileDomain(forName: String)](userdefaults/removevolatiledomain(forname:).md)
  Removes the specified volatile domain from the user’s defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/setvolatiledomain(_:forname:))*