# groupType

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

A string that describes the kind of multiseat purchase a customer’s access comes from.

**Availability**:
- App Store Server API 1.22+

## Declaration

```
string groupType
```

## Possible Values

- `ORGANIZATION`: An organization bought seats through Volume Purchasing and assigned one to the customer.
- `CONSUMER`: A subscriber bought seats through Group Purchases and invited the customer to join.

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

#### Discussion

Multiseat purchasing lets a customer buy your subscription in quantities greater than one. Each [`GroupEntry`](./groupentry.md) that the [`Get Customer Groups`](./get-customer-groups.md) endpoint returns includes a `groupType`, which identifies which form of multiseat purchase the customer’s access comes from:

- `ORGANIZATION` indicates Volume Purchasing. An organization that uses Apple Business Manager or Apple School Manager bought your subscription and assigns seats using a device management provider.
- `CONSUMER` indicates Group Purchases. A subscriber bought multiple seats and invited others to join.

For more information, see [Manage purchase options for an auto-renewable subscription](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions).

## See Also

### Group membership
- [object GroupEntry](./groupentry.md)
  The identifier, type, and per-product roles for a group that a customer belongs to.
- [object GroupMemberEntry](./groupmemberentry.md)
  A customer that belongs to a group.
- [object RoleEntry](./roleentry.md)
  A customer’s role for a single product within a group.
- [type groupId](./groupid.md)
  The unique identifier of a group, within the scope of your app.
- [type role](./role.md)
  A string that identifies a customer’s role for a product within a group.
- [type limit](./limit.md)
  The maximum number of group members to return in a single response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/grouptype)*