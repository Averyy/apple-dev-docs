# init(identifier:keyIdentifier:nonce:signature:timestamp:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

Initializes the payment discount with a signature and the parameters used by the signature.

**Availability**:
- iOS 12.2+ - Deprecated in 18.0
- iPadOS 12.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14.4+ - Deprecated in 15.0
- tvOS 12.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

## Declaration

```swift
init(identifier: String, keyIdentifier: String, nonce: UUID, signature: String, timestamp: NSNumber)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier keyIdentifier:(NSString *) keyIdentifier nonce:(NSUUID *) nonce signature:(NSString *) signature timestamp:(NSNumber *) timestamp;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/init(identifier:keyidentifier:nonce:signature:timestamp:))*