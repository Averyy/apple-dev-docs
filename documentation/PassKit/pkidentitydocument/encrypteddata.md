# encryptedData

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An encrypted data object that contains the document information and metadata to associate with a request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var encryptedData: Data { get }
```

## Mentions

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)

#### Discussion

The system encrypts this property to the public key with the developer portal for the calling app. You need to send this data to the server holding the corresponding private key for decryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydocument/encrypteddata)*