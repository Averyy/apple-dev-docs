# SecKeyGetBlockSize(_:)

**Framework**: Security  
**Kind**: func

Gets the block length associated with a cryptographic key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func SecKeyGetBlockSize(_ key: SecKey) -> Int
```

## Mentions

- [Using Keys for Encryption](using-keys-for-encryption.md)

#### Return Value

The block length associated with the key in bytes. If the key is an RSA key, for example, this is the size of the modulus.

## Parameters

- `key`: The key for which you want the block length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeygetblocksize(_:))*