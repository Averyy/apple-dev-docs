# GroupEntry

**Framework**: App Store Server API  
**Kind**: dictionary

The identifier, type, and per-product roles for a group that a customer belongs to.

**Availability**:
- App Store Server API 1.22+

## Declaration

```swift
object GroupEntry
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The [`Get Customer Groups`](get-customer-groups.md) endpoint returns a `GroupEntry` for each group a customer belongs to.

A customer’s role can differ per product, so `roles` is an array of [`RoleEntry`](roleentry.md) values rather than a single role. Read the [`role`](roleentry/role.md) for the [`productId`](roleentry/productid.md) you’re evaluating rather than assuming a single role applies across your products.

## Topics

### Group data types
- [object RoleEntry](roleentry.md)
  A customer’s role for a single product within a group.

## Properties

- `groupId` (groupId): The identifier of the group.
- `groupType` (groupType): The type of the group.
- `roles` ([RoleEntry]): An optional array of the customer’s roles in this group, one for each of your products that the group provides access to. This array is present for a group with a [`groupType`](groupentry/grouptype.md) of `ORGANIZATION`, and absent for a group with a `groupType` of `CONSUMER`.

## See Also

- [object RoleEntry](roleentry.md)
  A customer’s role for a single product within a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/groupentry)*