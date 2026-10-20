# label

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The user-visible label for the keychain item.

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
var label: String? { get set }
```

```objc
@property (copy, nullable) NSString * label;
```

#### Discussion

This property is equivalent to the `kSecAttrLabel` attribute type.

## See Also

### Accessing Keychain Item Attributes
- [var objectID: TKToken.ObjectID](./objectid.md)
  Returns the object ID used for keychain item identification.
- [var constraints: [NSNumber : Any]?](./constraints.md)
  Access constraints for the keychain item, keyed by [`TKTokenOperation`](../tktokenoperation.md) values wrapped in [`NSNumber`](../../Foundation/nsnumber.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/label)*