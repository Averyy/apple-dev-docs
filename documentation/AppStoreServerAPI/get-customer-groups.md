# Get Customer Groups

**Framework**: App Store Server API  
**Kind**: httpRequest

Get the groups that a customer belongs to, and their role in each group.

**Availability**:
- App Store Server API 1.22+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

> ❗ **Important**:  This endpoint is only available in the sandbox environment.

Call this endpoint to determine whether a customer has access to your app or its in-app purchases through an organization or group, and what role they hold in it. A *group* consists of customers whose access is purchased and managed centrally by a single account, rather than individually. Groups come from multiseat purchases: an organization buys seats through Volume Purchasing, or a subscriber buys seats through Group Purchases and invites others to join.

Use this endpoint only if your app offers a group experience where a customer’s group or role changes what you present — for example, exposing extra controls to a customer with the `ADMIN` [`role`](role.md), or grouping members into that administrator’s shared workspace. Group membership is separate from entitlement. To unlock content for a customer, read their transactions; don’t depend on group membership.

Provide any transaction identifier that belongs to the customer for your app. The response, [`GetCustomerGroupsResponse`](getcustomergroupsresponse.md), contains a [`GroupEntry`](groupentry.md) for each group the customer currently belongs to. Each entry identifies the group with a [`groupId`](groupid.md) and indicates the kind of group with a [`groupType`](grouptype.md). For a group with a [`groupType`](grouptype.md) of `ORGANIZATION`, the entry also lists the customer’s role for each of your products in a [`RoleEntry`](roleentry.md) array. If the customer doesn’t belong to any group, the response contains an empty `groups` array.

A customer can belong to more than one group, and can hold a different role in each.

To list the members of a group, call the [`Get Group Members`](get-group-members.md) endpoint.

##### Test in the Sandbox Environment

In the sandbox environment, if the customer doesn’t belong to any groups with a [`groupType`](grouptype.md) of `CONSUMER`, this endpoint returns a placeholder group with a `groupType` of `ORGANIZATION`:

```json
{
  "groups": [
    {
      "groupId": "900000000000000000",
      "groupType": "ORGANIZATION",
      "roles": [
        {
          "productId": "example.productId.one",
          "role": "ADMIN"
        },
        {
          "productId": "example.productId.two",
          "role": "NONE"
        }
      ]
    }
  ]
}
```

Send the placeholder [`groupId`](groupid.md) of `900000000000000000` to the [`Get Group Members`](get-group-members.md) endpoint to get its corresponding placeholder response.

For more information about configuring your subscription for multiseat purchases, see [`Manage purchase options for an auto-renewable subscription`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions).

## Endpoint

`GET https://api.storekit-sandbox.apple.com/groups/v1/currentGroups/{anyTransactionId}`

## Parameters

- `anyTransactionId` (anyTransactionId) *(required)*: Any [`originalTransactionId`](originaltransactionid.md), [`transactionId`](transactionid.md), or [`appTransactionId`](apptransactionid.md) that belongs to the customer for your app.

## See Also

- [object GetCustomerGroupsResponse](getcustomergroupsresponse.md)
  A response that contains the groups a customer belongs to, and their role in each group.
- [Get Group Members](get-group-members.md)
  Get a paginated list of the customers that belong to a group.
- [object GetGroupMembersResponse](getgroupmembersresponse.md)
  A response that contains a page of the customers that belong to a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-customer-groups)*