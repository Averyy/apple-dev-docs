# User

**Framework**: App Store Connect API  
**Kind**: dictionary

A member of your App Store Connect team, with assigned roles and access to specific apps.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object User
```

## Topics

### Objects
- [object User.Attributes](user/attributes-data.dictionary.md)
  Attributes that describe a Users resource.
- [object User.Relationships](user/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (User.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (User.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [Users](users.md)
  Manage users on your App Store Connect team.
- [object UserUpdateRequest](userupdaterequest.md)
  The request body you use to update a User.
- [object UserResponse](userresponse.md)
  The response body for endpoints that read or modify a single App Store Connect team member.
- [object UsersResponse](usersresponse.md)
  A response containing a list of team members who have access to your App Store Connect account.
- [object UserVisibleAppsLinkagesRequest](uservisibleappslinkagesrequest.md)
  A request body you use to add or remove visible apps from a user.
- [object UserVisibleAppsLinkagesResponse](uservisibleappslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type UserRole](userrole.md)
  A string that represents user roles and permissions in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/user)*