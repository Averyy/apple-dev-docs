# requestedSize

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

Returns the requested output size, in bytes, of key exchange result.

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
var requestedSize: Int { get }
```

```objc
@property (readonly) NSInteger requestedSize;
```

## Discussion

This property should be ignored if the output size is not configurable for the specified key exchange algorithm.

## See Also

### Accessing Parameters
- [var sharedInfo: Data?](./sharedinfo.md)
  Returns shared information typically used during the key derivation (KDF) step of a key exchange algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyexchangeparameters/requestedsize)*