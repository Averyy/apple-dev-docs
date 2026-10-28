# applicationUsername

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string that associates the transaction with a user account on your service.

**Availability**:
- iOS 7.0+ - Deprecated in 18.0
- iPadOS 7.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.9+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Create a Product.PurchaseOption.appAccountToken to use in Product.purchase(confirmIn:options:).

## Declaration

```swift
var applicationUsername: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * applicationUsername;
```

## Discussion

For more information on how to set and use this property, see [`applicationUsername`](../skmutablepayment/applicationusername.md).

## See Also

### Getting Payment Details
- [var productIdentifier: String](./productidentifier.md)
  A string used to identify a product that can be purchased from within your app.
- [var quantity: Int](./quantity.md)
  The number of items the user wants to purchase.
- [var requestData: Data?](./requestdata.md)
  Reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpayment/applicationusername)*