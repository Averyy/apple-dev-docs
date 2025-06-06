# constraints

**Framework**: CryptoTokenKit  
**Kind**: property

Access constraints for the keychain item, keyed by [`TKTokenOperation`](tktokenoperation.md) values wrapped in [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects.

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
var constraints: [NSNumber : Any]? { get set }
```

## See Also

- [var objectID: TKToken.ObjectID](tktokenkeychainitem/objectid.md)
  Returns the object ID used for keychain item identification.
- [var label: String?](tktokenkeychainitem/label.md)
  The user-visible label for the keychain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/constraints)*