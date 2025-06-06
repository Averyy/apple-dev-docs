# merchantIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

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

#### Discussion

This property identifies the merchant making the request, and must match one of the merchant identifiers in the app’s entitlement. For information about configuring the entitlement, see [`com.apple.developer.in-app-identity-presentment.merchant-identifiers`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.in-app-identity-presentment.merchant-identifiers).

Set this property before you invoke [`requestDocument(_:completion:)`](pkidentityauthorizationcontroller/requestdocument(_:completion:).md).

## See Also

- [var descriptor: (any PKIdentityDocumentDescriptor)?](pkidentityrequest/descriptor.md)
  The description of the document the app requests.
- [var nonce: Data?](pkidentityrequest/nonce.md)
  An arbitrary number that the signed response playload includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityrequest/merchantidentifier)*