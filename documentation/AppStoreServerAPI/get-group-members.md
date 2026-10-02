# Get Group Members

**Framework**: App Store Server API  
**Kind**: httpRequest

Get a paginated list of the customers that belong to a group.

**Availability**:
- App Store Server API 1.22+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

> ❗ **Important**:  This endpoint is only available in the sandbox environment.

Call this endpoint to enumerate the customers that belong to a group. Get the `groupId` for a group by calling the [`Get Customer Groups`](get-customer-groups.md) endpoint.

The response, [`GetGroupMembersResponse`](getgroupmembersresponse.md), contains a [`GroupMemberEntry`](groupmemberentry.md) for each member. Each entry identifies the member by their [`appTransactionId`](apptransactionid.md).

Each response returns at most the number of members you request in the `limit` query parameter. If the [`hasMore`](hasmore.md) field in the response is `true`, more members are available: call the endpoint again with the [`paginationToken`](get-group-members/paginationtoken.md) from the previous response to get the next set.

The following request gets the first 50 members of a group:

```javascript
GET https://api.storekit-sandbox.apple.com/groups/v1/group/{groupId}?limit=50
```

Group membership is separate from any transaction information. To unlock content for a customer, read their transactions; don’t depend on this endpoint. For more information, see [`Get Customer Groups`](get-customer-groups.md).

##### Test in the Sandbox Environment

In the sandbox environment, this endpoint returns a placeholder response when you send the placeholder [`groupId`](get-group-members/groupid.md) of `900000000000000000` that the [`Get Customer Groups`](get-customer-groups.md) endpoint returns:

```json
{
  "members": [
    {
      "appTransactionId": "700000000000000000"
    }
  ],
  "hasMore": false
}
```

## Endpoint

`GET https://api.storekit-sandbox.apple.com/groups/v1/group/{groupId}`

## Parameters

- `paginationToken` (paginationToken): An optional token you use to get the next set of members. Responses that have more members available include a `paginationToken`. Note: Omit this parameter the first time you call this endpoint.
- `limit` (limit): An optional maximum number of members to return in a single response.

## See Also

- [Get Customer Groups](get-customer-groups.md)
  Get the groups that a customer belongs to, and their role in each group.
- [object GetCustomerGroupsResponse](getcustomergroupsresponse.md)
  A response that contains the groups a customer belongs to, and their role in each group.
- [object GetGroupMembersResponse](getgroupmembersresponse.md)
  A response that contains a page of the customers that belong to a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-group-members)*