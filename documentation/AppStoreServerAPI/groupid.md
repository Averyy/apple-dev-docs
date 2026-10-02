# groupId

**Framework**: App Store Server API  
**Kind**: typealias

The unique identifier of a group, within the scope of your app.

**Availability**:
- App Store Server API 1.22+

## Declaration

```swift
string groupId
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The [`Get Customer Groups`](get-customer-groups.md) endpoint returns a `groupId` for each group a customer belongs to. Pass that value to the [`Get Group Members`](get-group-members.md) endpoint to enumerate the group’s members.

This identifier is unique within your app.

## See Also

- [object GroupEntry](groupentry.md)
  The identifier, type, and per-product roles for a group that a customer belongs to.
- [object GroupMemberEntry](groupmemberentry.md)
  A customer that belongs to a group.
- [object RoleEntry](roleentry.md)
  A customer’s role for a single product within a group.
- [type groupType](grouptype.md)
  A string that describes the kind of multiseat purchase a customer’s access comes from.
- [type role](role.md)
  A string that identifies a customer’s role for a product within a group.
- [type limit](limit.md)
  The maximum number of group members to return in a single response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/groupid)*