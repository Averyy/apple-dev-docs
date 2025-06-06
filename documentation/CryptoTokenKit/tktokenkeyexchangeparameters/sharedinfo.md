# sharedInfo

**Framework**: CryptoTokenKit  
**Kind**: property

Returns shared information typically used during the key derivation (KDF) step of a key exchange algorithm.

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
var sharedInfo: Data? { get }
```

#### Discussion

This property should be ignored if shared information isn’t used by the specified key exchange algorithm.

## See Also

- [var requestedSize: Int](tktokenkeyexchangeparameters/requestedsize.md)
  Returns the requested output size, in bytes, of key exchange result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyexchangeparameters/sharedinfo)*