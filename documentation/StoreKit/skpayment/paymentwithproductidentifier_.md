# paymentWithProductIdentifier:

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Returns a new payment with the specified product identifier.

**Availability**:
- iOS 3.0+ - Deprecated in 5.0
- iPadOS 3.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.0

> **Deprecated**: Use [`init(product:)`](./init%28product%29.md) instead, passing a product returned from [`SKProductsRequest`](../skproductsrequest.md).

## Declaration

```objc
+ (id) paymentWithProductIdentifier:(NSString *) identifier;
```

## Return Value

A new payment object.

## Discussion

The product identifier is a string previously agreed on between your application and the Apple App Store. The quantity property defaults to `1`.

To create a [`SKPayment`](../skpayment.md) object with a quantity greater than `1`, create a `SKMutablePayment` object, adjust its [`quantity`](../skmutablepayment/quantity.md) property and then add it to the payment queue:

```objc
SKMutablePayment *myPayment = [SKMutablePayment paymentWithProductIdentifier: myIdentifier];
myPayment.quantity = 2;
[[SKPaymentQueue defaultQueue] addPayment:myPayment];
```

## Parameters

- `identifier`: A string that identifies the item to be purchased.

## See Also

### Creating Payments
- [convenience init(product: SKProduct)](./init%28product%29.md)
  Returns a new payment for the specified product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpayment/paymentwithproductidentifier:)*