# volatileDomain(forName:)

**Framework**: Foundation  
**Kind**: method

Returns the dictionary for the specified volatile domain.

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
func volatileDomain(forName domainName: String) -> [String : Any]
```

#### Return Value

The dictionary of keys and values belonging to the domain. The keys in the dictionary are names of defaults, and the value corresponding to each key is a property list object (`NSData`, `NSString`, `NSNumber`, `NSDate`, `NSArray`, or `NSDictionary`).

## Parameters

- `domainName`: The domain whose keys and values you want.

## See Also

- [var volatileDomainNames: [String]](userdefaults/volatiledomainnames.md)
  The current volatile domain names.
- [func setVolatileDomain([String : Any], forName: String)](userdefaults/setvolatiledomain(_:forname:).md)
  Sets the dictionary for the specified volatile domain.
- [func removeVolatileDomain(forName: String)](userdefaults/removevolatiledomain(forname:).md)
  Removes the specified volatile domain from the user’s defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/volatiledomain(forname:))*