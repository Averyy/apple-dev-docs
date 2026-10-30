# Get All User IDs for an Organizational Unit

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- Apple Business API 2.7+

## Endpoint

`GET https://api-business.apple.com/v1/organizationalUnits/{id}/relationships/users`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `1000`

## Responses

- `200` OK (`OrganizationalUnitUsersLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-all-user-ids-for-an-organizational-unit)*