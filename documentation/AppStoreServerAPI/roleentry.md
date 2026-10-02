# RoleEntry

**Framework**: App Store Server API  
**Kind**: dictionary

A customer’s role for a single product within a group.

**Availability**:
- App Store Server API 1.22+

## Declaration

```swift
object RoleEntry
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

Each [`GroupEntry`](groupentry.md) contains an array of `RoleEntry` values. The array contains one role entry for each of your products for which the group provides the customer access.

Read the [`role`](roleentry/role.md) for the [`productId`](roleentry/productid.md) you’re evaluating. A customer can hold the `ADMIN` role for one product and the `NONE` role for another within the same group.

## Properties

- `productId` (productId): The product identifier of the in-app purchase that the role applies to.
- `role` (role): The customer’s role for the product.

## See Also

- [object GroupEntry](groupentry.md)
  The identifier, type, and per-product roles for a group that a customer belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/roleentry)*