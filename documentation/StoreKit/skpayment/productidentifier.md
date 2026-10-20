# productIdentifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string used to identify a product that can be purchased from within your app.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.purchase(confirmIn:options:).

## Declaration

```swift
var productIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * productIdentifier;
```

## Mentions

- [Testing an interrupted purchase](../testing-an-interrupted-purchase.md)

#### Discussion

The product identifier is a string previously agreed on between your app and the Apple App Store.

## See Also

### Getting Payment Details
- [var quantity: Int](./quantity.md)
  The number of items the user wants to purchase.
- [var requestData: Data?](./requestdata.md)
  Reserved for future use.
- [var applicationUsername: String?](./applicationusername.md)
  A string that associates the transaction with a user account on your service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpayment/productidentifier)*