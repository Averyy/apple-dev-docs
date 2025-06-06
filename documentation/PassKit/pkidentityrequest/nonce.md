# nonce

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An arbitrary number that the signed response playload includes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var nonce: Data? { get set }
```

## Mentions

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md)

#### Discussion

A [`PKIdentityAuthorizationController`](pkidentityauthorizationcontroller.md) treats this value as opaque, and has a maximum allowed size of 64 bytes. Your app’s server needs to use the same `nonce` value when decrypting and verifying the response.

Set this property before you invoke [`requestDocument(_:completion:)`](pkidentityauthorizationcontroller/requestdocument(_:completion:).md).

## See Also

- [var descriptor: (any PKIdentityDocumentDescriptor)?](pkidentityrequest/descriptor.md)
  The description of the document the app requests.
- [var merchantIdentifier: String?](pkidentityrequest/merchantidentifier.md)
  A value that represents the merchant that makes the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityrequest/nonce)*