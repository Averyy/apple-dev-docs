# objectID

**Framework**: CryptoTokenKit  
**Kind**: property

Returns the object ID used for keychain item identification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var objectID: TKToken.ObjectID { get }
```

## See Also

- [var label: String?](tktokenkeychainitem/label.md)
  The user-visible label for the keychain item.
- [var constraints: [NSNumber : Any]?](tktokenkeychainitem/constraints.md)
  Access constraints for the keychain item, keyed by [`TKTokenOperation`](tktokenoperation.md) values wrapped in [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/objectid)*