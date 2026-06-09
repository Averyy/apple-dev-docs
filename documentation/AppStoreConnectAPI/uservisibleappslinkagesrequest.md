# UserVisibleAppsLinkagesRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

A request body you use to add or remove visible apps from a user.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object UserVisibleAppsLinkagesRequest
```

## Topics

### Objects
- [object UserVisibleAppsLinkagesRequest.Data](uservisibleappslinkagesrequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` ([UserVisibleAppsLinkagesRequest.Data]) *(required)*: The object types and IDs of the related resources.

## See Also

- [object User](user.md)
  A member of your App Store Connect team, with assigned roles and access to specific apps.
- [object UserUpdateRequest](userupdaterequest.md)
  The request body you use to update a User.
- [object UserResponse](userresponse.md)
  The response body for endpoints that read or modify a single App Store Connect team member.
- [object UsersResponse](usersresponse.md)
  A response containing a list of team members who have access to your App Store Connect account.
- [object UserVisibleAppsLinkagesResponse](uservisibleappslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type UserRole](userrole.md)
  A string that represents user roles and permissions in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/uservisibleappslinkagesrequest)*