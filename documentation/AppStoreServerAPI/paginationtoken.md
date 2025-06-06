# paginationToken

**Framework**: App Store Server API  
**Kind**: typealias

A pagination token that you return to the endpoint on a subsequent call to receive the next set of results.

**Availability**:
- App Store Server API 1.5+

## Declaration

```swift
string paginationToken
```

#### Discussion

A token you use in the [`Get Notification History`](get-notification-history.md) endpoint to ask for the next set of up to 20 notification history entries. All responses include a `paginationToken`.

## See Also

- [type hasMore](hasmore.md)
  A Boolean value indicating whether the App Store has more transaction data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/paginationtoken)*