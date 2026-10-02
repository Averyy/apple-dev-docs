# GroupNotFoundError

**Framework**: App Store Server API  
**Kind**: dictionary

An error that indicates the group wasn’t found.

**Availability**:
- App Store Server API 1.22+

## Declaration

```swift
object GroupNotFoundError
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

A request returns this error if you call the [`Get Group Members`](get-group-members.md) endpoint with a `groupId` that’s well-formed but doesn’t identify a group in your app.

A group that existed previously can stop existing — for example, when its subscription ends. Get a current `groupId` by calling the [`Get Customer Groups`](get-customer-groups.md) endpoint.

## Properties

- `errorCode` (int64)
- `errorMessage` (string)

## See Also

- [object InvalidGroupIdError](invalidgroupiderror.md)
  An error that indicates the group identifier is invalid.
- [object InvalidLimitError](invalidlimiterror.md)
  An error that indicates the request limit is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/groupnotfounderror)*