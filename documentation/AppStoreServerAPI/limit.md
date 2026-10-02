# limit

**Framework**: App Store Server API  
**Kind**: typealias

The maximum number of group members to return in a single response.

**Availability**:
- App Store Server API 1.22+

## Declaration

```swift
int32 limit
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

Use this optional query parameter with the [`Get Group Members`](get-group-members.md) endpoint to control the size of each page of results. The maximum value is `100`; a request with a greater value fails with an [`InvalidLimitError`](invalidlimiterror.md).

If the group has more members than the response contains, the [`hasMore`](hasmore.md) field is `true`. Call the endpoint again with the [`paginationToken`](paginationtoken.md) from the response to get the next set of members.

## See Also

- [object GroupEntry](groupentry.md)
  The identifier, type, and per-product roles for a group that a customer belongs to.
- [object GroupMemberEntry](groupmemberentry.md)
  A customer that belongs to a group.
- [object RoleEntry](roleentry.md)
  A customer’s role for a single product within a group.
- [type groupId](groupid.md)
  The unique identifier of a group, within the scope of your app.
- [type groupType](grouptype.md)
  A string that describes the kind of multiseat purchase a customer’s access comes from.
- [type role](role.md)
  A string that identifies a customer’s role for a product within a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/limit)*