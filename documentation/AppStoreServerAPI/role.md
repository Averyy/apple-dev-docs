# role

**Framework**: App Store Server API  
**Kind**: typealias

A string that identifies a customer’s role for a product within a group.

**Availability**:
- App Store Server API 1.22+

## Declaration

```swift
string role
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

Each [`RoleEntry`](roleentry.md) that the [`Get Customer Groups`](get-customer-groups.md) endpoint returns includes a `role` for a single [`productId`](productid.md). A customer can hold a different role for each of your products within the same group.

Roles apply only to a group with a [`groupType`](grouptype.md) of `ORGANIZATION`. A group with a `groupType` of `CONSUMER` doesn’t report roles.

This value is informational. Determine access to content based on the customer’s transactions. Use `role` if you want to offer an administrator something the other members don’t get, such as naming the team or configuring an experience for the whole group.

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
- [type limit](limit.md)
  The maximum number of group members to return in a single response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/role)*