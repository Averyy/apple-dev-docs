# nonce

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) NSData * nonce;
```

## Mentions

- [Requesting identity data from a Wallet pass](../requesting-identity-data-from-a-wallet-pass.md)
- [Verifying Wallet identity requests](../verifying-wallet-identity-requests.md)

#### Discussion

A [`PKIdentityAuthorizationController`](../pkidentityauthorizationcontroller.md) treats this value as opaque, and has a maximum allowed size of 64 bytes. Your app’s server needs to use the same `nonce` value when decrypting and verifying the response.

Set this property before you invoke [`requestDocument(_:completion:)`](../pkidentityauthorizationcontroller/requestdocument%28_,completion%29.md).

## See Also

### Configuring an identity request
- [var descriptor: (any PKIdentityDocumentDescriptor)?](./descriptor.md)
  The description of the document the app requests.
- [var merchantIdentifier: String?](./merchantidentifier.md)
  A value that represents the merchant that makes the request.
- [var usageDescriptionKey: String?](./usagedescriptionkey.md)
  The key in your app’s information property list that describes the reason for an identity request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityrequest/nonce)*