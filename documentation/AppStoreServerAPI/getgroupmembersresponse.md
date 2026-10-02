# GetGroupMembersResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains a page of the customers that belong to a group.

**Availability**:
- App Store Server API 1.22+

## Declaration

```swift
object GetGroupMembersResponse
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

This response contains information that you request by calling the [`Get Group Members`](get-group-members.md) endpoint.

If [`hasMore`](getgroupmembersresponse/hasmore.md) is `true`, call [`Get Group Members`](get-group-members.md) again with the [`paginationToken`](getgroupmembersresponse/paginationtoken.md) from this response to get the next set of members.

## Topics

### Response data types
- [object GroupMemberEntry](groupmemberentry.md)
  A customer that belongs to a group.

## Properties

- `members` ([GroupMemberEntry]): An array of the customers that belong to the group.
- `paginationToken` (paginationToken): A token you send in a subsequent request to get the next set of members. The response includes this value only when more members are available.
- `hasMore` (hasMore): A Boolean value that indicates whether the group has more members than the response contains.

## See Also

- [Get Customer Groups](get-customer-groups.md)
  Get the groups that a customer belongs to, and their role in each group.
- [object GetCustomerGroupsResponse](getcustomergroupsresponse.md)
  A response that contains the groups a customer belongs to, and their role in each group.
- [Get Group Members](get-group-members.md)
  Get a paginated list of the customers that belong to a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/getgroupmembersresponse)*