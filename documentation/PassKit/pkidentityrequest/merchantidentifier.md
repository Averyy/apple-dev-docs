# merchantIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A value that represents the merchant that makes the request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var merchantIdentifier: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * merchantIdentifier;
```

#### Discussion

This property identifies the merchant making the request, and must match one of the merchant identifiers in the app’s entitlement. For information about configuring the entitlement, see [`com.apple.developer.in-app-identity-presentment.merchant-identifiers`](../../BundleResources/entitlements/com.apple.developer.in-app-identity-presentment.merchant-identifiers.md).

Set this property before you invoke [`requestDocument(_:completion:)`](../pkidentityauthorizationcontroller/requestdocument%28_,completion%29.md).

## See Also

### Configuring an identity request
- [var descriptor: (any PKIdentityDocumentDescriptor)?](./descriptor.md)
  The description of the document the app requests.
- [var nonce: Data?](./nonce.md)
  An arbitrary number that the signed response playload includes.
- [var usageDescriptionKey: String?](./usagedescriptionkey.md)
  The key in your app’s information property list that describes the reason for an identity request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityrequest/merchantidentifier)*