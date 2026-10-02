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

Endpoints that paginate their results return a `paginationToken` when more results are available. Provide it on your next call to that endpoint to get the following page, and check [`hasMore`](hasmore.md) to determine whether to keep requesting pages.

Each endpoint sets its own page size:

- [`Get Notification History`](get-notification-history.md) returns up to 20 notification history entries per page.
- [`Get Group Members`](get-group-members.md) returns up to the number of members you request in the [`limit`](limit.md) query parameter, to a maximum of 100 per page.

Omit this parameter the first time you call an endpoint, and don’t change the rest of the request when you ask for subsequent pages.

## See Also

- [type hasMore](hasmore.md)
  A Boolean value indicating whether the App Store has more data to return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/paginationtoken)*