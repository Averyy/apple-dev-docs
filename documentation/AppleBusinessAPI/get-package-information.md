# Get Package Information

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific package for an organization using Apple Business’s built-in device management.

**Availability**:
- Apple Business API 2.7+

### Example

**Request**:

```
curl "https://api-business.apple.com/v1/packages/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
{
  "data": {
    "type": "packages",
    "id": "pkg-12345",
    "attributes": {
      "name": "Enterprise Software Suite",
      "url": "https://example.com/packages/enterprise-suite.pkg",
      "hash": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
      "bundleIds": [
        "com.example.enterpriseapp"
      ],
      "description": "Complete enterprise productivity software suite",
      "version": "2.5.1",
      "createdDateTime": "2024-01-15T10:30:00Z",
      "updatedDateTime": "2024-06-01T14:22:00Z"
    },
    "links": {
      "self": "https://api-business.apple.com/v1/packages/pkg-12345"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/packages/pkg-12345"
  }
}
```

## Topics

### Responses
- [object PackageResponse](./packageresponse.md)
  A response that contains information about a package resource.

## Endpoint

`GET https://api-business.apple.com/v1/packages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[packages]` ([string]): The fields to return for included related types.

  **Allowed Values**: `name`, `url`, `hash`, `bundleIds`, `description`, `version`, `createdDateTime`, `updatedDateTime`

## Responses

- `200` OK (`PackageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Apps and Packages
- [Get Apps](./get-apps.md)
  Get a list of apps for an organization using the built-in device management in Apple Business.
- [Get App Information](./get-app-information.md)
  Get information about a specific app for an organization using the built-in device management in Apple Business.
- [Get Packages](./get-packages.md)
  Get a list of packages for an organization using Apple Business’s built-in device management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-package-information)*