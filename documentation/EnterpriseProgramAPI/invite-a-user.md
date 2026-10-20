# Invite a User

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Invite a user with assigned user roles to join your team.

#### Overview

- HTTPBody

## Endpoint

`POST https://api.enterprise.developer.apple.com/v1/userInvitations`

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

## See Also

### Sending and Canceling Invitations
- [Cancel a User Invitation](./cancel-a-user-invitation.md)
  Cancel a pending invitation for a user to join your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/invite-a-user)*