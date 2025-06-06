# quantity

**Framework**: StoreKit  
**Kind**: property

The number of items the user wants to purchase.

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
var quantity: Int { get set }
```

#### Discussion

The quantity property must be greater than `0`.

## See Also

- [var productIdentifier: String](skmutablepayment/productidentifier.md)
  A string that identifies a product that can be purchased from within your app.
- [var requestData: Data?](skmutablepayment/requestdata.md)
  Reserved for future use.
- [var applicationUsername: String?](skmutablepayment/applicationusername.md)
  A string that associates the transaction with a user account on your service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skmutablepayment/quantity)*