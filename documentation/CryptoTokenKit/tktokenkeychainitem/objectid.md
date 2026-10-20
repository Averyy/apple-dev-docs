# objectID

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) TKTokenObjectID objectID;
```

## See Also

### Accessing Keychain Item Attributes
- [var label: String?](./label.md)
  The user-visible label for the keychain item.
- [var constraints: [NSNumber : Any]?](./constraints.md)
  Access constraints for the keychain item, keyed by [`TKTokenOperation`](../tktokenoperation.md) values wrapped in [`NSNumber`](../../Foundation/nsnumber.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/objectid)*