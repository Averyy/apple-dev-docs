# OrderLookupStatus

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

A value that indicates whether the order ID in the request is valid for your app.

**Availability**:
- App Store Server API 1.1+

## Declaration

```
int32 OrderLookupStatus
```

## Possible Values

- `0`: The [`orderId`](./orderid.md) that you provided in the [`Look Up Order ID`](./look-up-order-id.md) request is valid and contains at least one in-app purchase for your app.
- `1`: The [`orderId`](./orderid.md) is invalid or doesn’t contain any in-app purchases for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/orderlookupstatus)*