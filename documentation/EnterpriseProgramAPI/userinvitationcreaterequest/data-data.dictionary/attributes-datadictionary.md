# UserInvitationCreateRequest.Data.Attributes

**Framework**: Enterprise Program API  
**Kind**: dictionary

Attributes that you set that describe the new resource.

## Declaration

```swift
object UserInvitationCreateRequest.Data.Attributes
```

## Properties

- `email` (email) *(required)*: The email address of a pending user invitation. The email address must be valid to activate the account. It can be any email address, not necessarily one associated with an Apple Account.
- `firstName` (string) *(required)*: The user invitation recipient’s first name.
- `lastName` (string) *(required)*: The user invitation recipient’s last name.
- `roles` ([UserRole]) *(required)*: Assigned user roles that determine the user’s access to sections of the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com) and tasks they can perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/userinvitationcreaterequest/data-data.dictionary/attributes-data.dictionary)*