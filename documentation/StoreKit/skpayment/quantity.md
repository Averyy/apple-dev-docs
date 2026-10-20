# quantity

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The number of items the user wants to purchase.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Create a Product.PurchaseOption.quantity to use in Product.purchase(confirmIn:options:).

## Declaration

```swift
var quantity: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger quantity;
```

#### Discussion

The default value is 1, the minimum value is 1, and the maximum value is 10.

## See Also

### Getting Payment Details
- [var productIdentifier: String](./productidentifier.md)
  A string used to identify a product that can be purchased from within your app.
- [var requestData: Data?](./requestdata.md)
  Reserved for future use.
- [var applicationUsername: String?](./applicationusername.md)
  A string that associates the transaction with a user account on your service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpayment/quantity)*