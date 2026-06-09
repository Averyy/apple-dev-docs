# UserResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read or modify a single App Store Connect team member.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object UserResponse
```

## Properties

- `data` (User) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([App])

## See Also

- [Read user information](get-v1-users-_id_.md)
  Get information about a user on your team, such as name, roles, and app visibility.
- [object User](user.md)
  A member of your App Store Connect team, with assigned roles and access to specific apps.
- [object UserUpdateRequest](userupdaterequest.md)
  The request body you use to update a User.
- [object UsersResponse](usersresponse.md)
  A response containing a list of team members who have access to your App Store Connect account.
- [object UserVisibleAppsLinkagesRequest](uservisibleappslinkagesrequest.md)
  A request body you use to add or remove visible apps from a user.
- [object UserVisibleAppsLinkagesResponse](uservisibleappslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type UserRole](userrole.md)
  A string that represents user roles and permissions in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/userresponse)*