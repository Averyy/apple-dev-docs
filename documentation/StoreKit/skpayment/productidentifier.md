# productIdentifier

**Framework**: StoreKit  
**Kind**: property

A string used to identify a product that can be purchased from within your app.

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
var productIdentifier: String { get }
```

## Mentions

- [Testing an interrupted purchase](testing-an-interrupted-purchase.md)

#### Discussion

The product identifier is a string previously agreed on between your app and the Apple App Store.

## See Also

- [var quantity: Int](skpayment/quantity.md)
  The number of items the user wants to purchase.
- [var requestData: Data?](skpayment/requestdata.md)
  Reserved for future use.
- [var applicationUsername: String?](skpayment/applicationusername.md)
  A string that associates the transaction with a user account on your service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpayment/productidentifier)*