# Get App Information

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific app for an organization using the built-in device management in Apple Business.

**Availability**:
- Apple Business API 2.6+

## Overview

> ❗ **Important**: This endpoint requires the built-in device management service to be turned on for the organization. If you need to manage apps without the built-in device management, use the [Apps and Books for Organizations](../DeviceManagement/apps-and-books-for-organizations.md) API instead.

### Example

**Request**:

```
curl "https://api-business.apple.com/v1/apps/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
{
  "data": {
    "type": "apps",
    "id": "361309726",
    "attributes": {
      "name": "Pages",
      "bundleId": "com.apple.Pages",
      "websiteUrl": "https://www.apple.com/pages/",
      "version": "14.0",
      "supportedOS": [
        "SUPPORTED_OS_IOS",
        "SUPPORTED_OS_MACOS"
      ],
      "isCustomApp": false,
      "appStoreUrl": "https://apps.apple.com/app/pages/id361309726"
    },
    "links": {
      "self": "https://api-business.apple.com/v1/apps/361309726"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/apps/361309726"
  }
}
```

## Topics

### Responses
- [object AppResponse](./appresponse.md)
  A response that contains information about an app resource.

## Endpoint

`GET https://api-business.apple.com/v1/apps/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[apps]` ([string]): The fields to return for included related types.

  **Allowed Values**: `name`, `bundleId`, `websiteUrl`, `version`, `supportedOS`, `isCustomApp`, `appStoreUrl`

## Responses

- `200` OK (`AppResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Apps and Packages
- [Get Apps](./get-apps.md)
  Get a list of apps for an organization using the built-in device management in Apple Business.
- [Get Packages](./get-packages.md)
  Get a list of packages for an organization using Apple Business’s built-in device management.
- [Get Package Information](./get-package-information.md)
  Get information about a specific package for an organization using Apple Business’s built-in device management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-app-information)*