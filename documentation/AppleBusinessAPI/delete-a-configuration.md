# Delete a Configuration

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a Configuration from an organization.

**Availability**:
- Apple Business API 2.7+

### Example

**Request**:

```
curl -X DELETE "https://api-business.apple.com/v1/configurations/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```
HTTP/1.1 204 No Content
```

## Endpoint

`DELETE https://api-business.apple.com/v1/configurations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`): Request entity error(s).
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Configurations
- [Get Configurations](./get-configurations.md)
  Get a list of Configurations in an organization.
- [Create a Configuration](./create-a-configuration.md)
  Create a new custom Configuration in an organization.
- [Get Configuration Information](./get-configuration-information.md)
  Get information about a specific Configuration in an organization.
- [Update a Configuration](./update-a-configuration.md)
  Update an existing custom Configuration in an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/delete-a-configuration)*