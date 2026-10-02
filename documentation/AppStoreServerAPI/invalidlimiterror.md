# InvalidLimitError

**Framework**: App Store Server API  
**Kind**: dictionary

An error that indicates the request limit is invalid.

**Availability**:
- App Store Server API 1.22+

## Declaration

```swift
object InvalidLimitError
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

A request returns this error if you call the [`Get Group Members`](get-group-members.md) endpoint with a [`limit`](limit.md) query parameter that’s outside the supported range. The maximum value is `100`.

## Properties

- `errorCode` (int64)
- `errorMessage` (string)

## See Also

- [object GroupNotFoundError](groupnotfounderror.md)
  An error that indicates the group wasn’t found.
- [object InvalidGroupIdError](invalidgroupiderror.md)
  An error that indicates the group identifier is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/invalidlimiterror)*