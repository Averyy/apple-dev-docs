# open(_:authenticating:)

**Framework**: Cryptokit  
**Kind**: method

Decrypts a message, if the ciphertext is valid, verifying the integrity of additional authentication data.

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
mutating func open<C, AD>(_ ciphertext: C, authenticating aad: AD) throws -> Data where C : DataProtocol, AD : DataProtocol
```

#### Return Value

The resulting cleartext message if the message is authentic.

#### Discussion

You can call this method multiple times to decrypt a series of messages. When using this method, the recipient of the ciphertext messages needs to decrypt them in the same order that the sender encrypts them. The system doesn’t decrypt the additional authentication data in the `aad` parameter that the recipient uses to verify the message integrity.

> **Note**: The system throws errors from [`HPKE.Errors`](hpke/errors.md) when it encounters them.

## Parameters

- `ciphertext`: The ciphertext message to decrypt.
- `aad`: Additional cleartext data to authenticate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/recipient/open(_:authenticating:))*