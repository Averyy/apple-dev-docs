# requestData

**Framework**: StoreKit  
**Kind**: property

Reserved for future use.

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
var requestData: Data? { get set }
```

#### Discussion

The default value is `nil`. If [`requestData`](skmutablepayment/requestdata.md) is not `nil`, your payment will be rejected by the Apple App Store.

## See Also

- [var productIdentifier: String](skmutablepayment/productidentifier.md)
  A string that identifies a product that can be purchased from within your app.
- [var quantity: Int](skmutablepayment/quantity.md)
  The number of items the user wants to purchase.
- [var applicationUsername: String?](skmutablepayment/applicationusername.md)
  A string that associates the transaction with a user account on your service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skmutablepayment/requestdata)*