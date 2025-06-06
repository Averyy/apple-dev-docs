# seal(_:)

**Framework**: Apple CryptoKit  
**Kind**: method

Encrypts the given cleartext message.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
mutating func seal<M>(_ msg: M) throws -> Data where M : DataProtocol
```

#### Return Value

The ciphertext for the recipient to decrypt.

#### Discussion

You can call this method multiple times to encrypt a series of messages. When using this method, you need to supply ciphertext messages to the decryption code on the receiving side in the same order as you encrypt them.

> **Note**: The system throws errors from [`HPKE.Errors`](hpke/errors.md) when it encounters them.

The system throws errors from [`HPKE.Errors`](hpke/errors.md) when it encounters them.

## Parameters

- `msg`: The cleartext message to encrypt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/sender/seal(_:))*