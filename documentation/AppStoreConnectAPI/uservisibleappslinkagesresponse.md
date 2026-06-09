# UserVisibleAppsLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response body that contains a list of related resource IDs.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object UserVisibleAppsLinkagesResponse
```

## Topics

### Objects
- [object UserVisibleAppsLinkagesResponse.Data](uservisibleappslinkagesresponse/data-data.dictionary.md)
  The data element of the response body.

## Properties

- `data` ([UserVisibleAppsLinkagesResponse.Data]) *(required)*: The object types and IDs of the related resources.
- `links` (PagedDocumentLinks) *(required)*: Navigational links including the self-link and links to the related data.
- `meta` (PagingInformation): Paging information.

## See Also

- [Get all visible app resource ids for a user](get-v1-users-_id_-relationships-visibleapps.md)
  Get a list of app resource IDs to which a user on your team has access.
- [object User](user.md)
  A member of your App Store Connect team, with assigned roles and access to specific apps.
- [object UserUpdateRequest](userupdaterequest.md)
  The request body you use to update a User.
- [object UserResponse](userresponse.md)
  The response body for endpoints that read or modify a single App Store Connect team member.
- [object UsersResponse](usersresponse.md)
  A response containing a list of team members who have access to your App Store Connect account.
- [object UserVisibleAppsLinkagesRequest](uservisibleappslinkagesrequest.md)
  A request body you use to add or remove visible apps from a user.
- [type UserRole](userrole.md)
  A string that represents user roles and permissions in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/uservisibleappslinkagesresponse)*