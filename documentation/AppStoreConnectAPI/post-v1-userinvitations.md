# Invite a user

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Invite a user with assigned user roles to join your team.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/userInvitations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `UserInvitationCreateRequest`

## Responses

- `201` Created (`UserInvitationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Sending and Canceling Invitations
- [Cancel a user invitation](./delete-v1-userinvitations-_id_.md)
  Cancel a pending invitation for a user to join your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-userinvitations)*