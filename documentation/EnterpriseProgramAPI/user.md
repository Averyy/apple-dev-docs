# User

**Framework**: Enterprise Program API  
**Kind**: dictionary

The data structure that represents a Users resource.

## Declaration

```swift
object User
```

## Topics

### Objects
- [object User.Attributes](user/attributes-data.dictionary.md)
  Attributes that describe a Users resource.

## Properties

- `attributes` (User.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object UserUpdateRequest](userupdaterequest.md)
  The request body you use to update a User.
- [object UserResponse](userresponse.md)
  A response that contains a single Users resource.
- [object UsersResponse](usersresponse.md)
  A response that contains a list of Users resources.
- [type UserRole](userrole.md)
  Strings that represent user roles and permissions in the Apple Developer website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/user)*