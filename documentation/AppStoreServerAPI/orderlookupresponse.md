# OrderLookupResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that includes the order lookup status and an array of signed transactions for the in-app purchases in the order.

**Availability**:
- App Store Server API 1.1+

## Declaration

```swift
object OrderLookupResponse
```

#### Discussion

The order lookup response contains information about the [`orderId`](orderid.md) you specify when you call [`Look Up Order ID`](look-up-order-id.md).

If the `orderId` that you provide in the request is invalid, the response doesn’t include the `signedTransactions` array. If the `orderId` is valid, expect at least one transaction in the `signedTransactions` array.

## Topics

### Response data types
- [type OrderLookupStatus](orderlookupstatus.md)
  A value that indicates whether the order ID in the request is valid for your app.

## See Also

- [Look Up Order ID](look-up-order-id.md)
  Get a customer’s in-app purchases from a receipt using the order ID.
- [type orderId](orderid.md)
  The customer’s order ID from an App Store receipt for in-app purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/orderlookupresponse)*