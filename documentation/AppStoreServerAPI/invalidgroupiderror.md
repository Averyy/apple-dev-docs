# InvalidGroupIdError

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the group identifier is invalid.

**Availability**:
- App Store Server API 1.22+

## Declaration

```
object InvalidGroupIdError
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

#### Discussion

A request returns this error if you call the [`Get Group Members`](./get-group-members.md) endpoint with a `groupId` that isn’t well-formed.

If the identifier is well-formed but doesn’t identify a group in your app, the request returns a [`GroupNotFoundError`](./groupnotfounderror.md) instead. Use a [`groupId`](./groupid.md) that the [`Get Customer Groups`](./get-customer-groups.md) endpoint returns.

## Properties

- `errorCode` (int64): **Allowed Values**: `4000225`
- `errorMessage` (string): **Allowed Values**: `Invalid request. The group ID is invalid.`

## See Also

### Group membership errors
- [object GroupNotFoundError](./groupnotfounderror.md)
  An error that indicates the group wasn’t found.
- [object InvalidLimitError](./invalidlimiterror.md)
  An error that indicates the request limit is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/invalidgroupiderror)*