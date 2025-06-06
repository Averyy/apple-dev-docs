# init(product:)

**Framework**: StoreKit  
**Kind**: init

Returns a new payment for the specified product.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
convenience init(product: SKProduct)
```

#### Return Value

A new payment object.

#### Discussion

This [`Object creation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) uses the `productIdentifier` property obtained from the `product` parameter to create and return a new payment with that identifier. The quantity property defaults to `1`.

To create a [`SKPayment`](skpayment.md) object with a quantity greater than `1`, create a `SKMutablePayment` object, adjust its `quantity` property and then add it to the payment queue.

```objc
SKMutablePayment *myPayment = [SKMutablePayment paymentWithProduct: myProduct];
myPayment.quantity = 2;
[[SKPaymentQueue defaultQueue] addPayment:myPayment];
```

## Parameters

- `product`: The product the user wishes to purchase.

## See Also

- [In-App Purchase Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpayment/init(product:))*