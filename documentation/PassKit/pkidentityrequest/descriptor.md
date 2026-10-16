# descriptor

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The description of the document the app requests.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var descriptor: (any PKIdentityDocumentDescriptor)? { get set }
```

#### Discussion

Set this property before you invoke [`requestDocument(_:completion:)`](pkidentityauthorizationcontroller/requestdocument(_:completion:).md).

## See Also

- [var nonce: Data?](pkidentityrequest/nonce.md)
  An arbitrary number that the signed response playload includes.
- [var merchantIdentifier: String?](pkidentityrequest/merchantidentifier.md)
  A value that represents the merchant that makes the request.
- [var usageDescriptionKey: String?](pkidentityrequest/usagedescriptionkey.md)
  The key in your app’s information property list that describes the reason for an identity request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityrequest/descriptor)*