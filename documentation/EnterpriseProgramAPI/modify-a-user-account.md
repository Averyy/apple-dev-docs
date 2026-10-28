# Modify a User Account

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Change a user’s role, app visibility information, or other account details.

## Overview

- HTTPBody

## Endpoint

`PATCH https://api.enterprise.developer.apple.com/v1/users/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `UserUpdateRequest`

## Responses

- `200` OK (`UserResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)

## See Also

### Modifying and Removing User Accounts
- [Delete a User Account](./delete-a-user-account.md)
  Remove a user from your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/modify-a-user-account)*