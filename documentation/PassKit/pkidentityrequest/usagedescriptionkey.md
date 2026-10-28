# usageDescriptionKey

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The key in your app’s information property list that describes the reason for an identity request.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
var usageDescriptionKey: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * usageDescriptionKey;
```

## Mentions

- [Requesting identity data from a Wallet pass](../requesting-identity-data-from-a-wallet-pass.md)

## Discussion

Use this key in the dictionary for [`NSIdentityUsageDescriptionDictionary`](../../BundleResources/information-property-list/nsidentityusagedescriptiondictionary.md) if you have multiple use cases for requesting identity information. Each key in the dictionary maps to a string that describes why your app requests identity information. If you have one use case for requesting identity information, use [`NSIdentityUsageDescription`](../../BundleResources/information-property-list/nsidentityusagedescription.md).

## See Also

### Configuring an identity request
- [var descriptor: (any PKIdentityDocumentDescriptor)?](./descriptor.md)
  The description of the document the app requests.
- [var nonce: Data?](./nonce.md)
  An arbitrary number that the signed response playload includes.
- [var merchantIdentifier: String?](./merchantidentifier.md)
  A value that represents the merchant that makes the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityrequest/usagedescriptionkey)*