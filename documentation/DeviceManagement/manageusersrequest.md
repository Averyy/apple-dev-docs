# ManageUsersRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for user management.

**Availability**:
- VPP License Management 2.0+

## Declaration

```swift
object ManageUsersRequest
```

## Mentions

- [Managing users](managing-users.md)

## Topics

### Objects and Data Types
- [object RequestUser](requestuser.md)
  The requested user in the organization.

## Properties

- `users` ([RequestUser]) *(required)*: The set of users to manage.

## See Also

- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/manageusersrequest)*