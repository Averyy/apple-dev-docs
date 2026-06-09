# UsersResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of team members who have access to your App Store Connect account.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object UsersResponse
```

## Properties

- `data` ([User]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([App])

## See Also

- [List users](get-v1-users.md)
  Get a list of the users on your team.
- [object User](user.md)
  A member of your App Store Connect team, with assigned roles and access to specific apps.
- [object UserUpdateRequest](userupdaterequest.md)
  The request body you use to update a User.
- [object UserResponse](userresponse.md)
  The response body for endpoints that read or modify a single App Store Connect team member.
- [object UserVisibleAppsLinkagesRequest](uservisibleappslinkagesrequest.md)
  A request body you use to add or remove visible apps from a user.
- [object UserVisibleAppsLinkagesResponse](uservisibleappslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type UserRole](userrole.md)
  A string that represents user roles and permissions in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/usersresponse)*