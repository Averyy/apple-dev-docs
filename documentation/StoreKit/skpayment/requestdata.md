# requestData

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

Reserved for future use.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Create Product.PurchaseOption.custom values to use in Product.purchase(confirmIn:options:).

## Declaration

```swift
var requestData: Data? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSData * requestData;
```

## Discussion

The default value is `nil`. If [`requestData`](./requestdata.md) is not `nil`, your payment request will be rejected.

## See Also

### Getting Payment Details
- [var productIdentifier: String](./productidentifier.md)
  A string used to identify a product that can be purchased from within your app.
- [var quantity: Int](./quantity.md)
  The number of items the user wants to purchase.
- [var applicationUsername: String?](./applicationusername.md)
  A string that associates the transaction with a user account on your service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpayment/requestdata)*