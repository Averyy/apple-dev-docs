# Get Configuration Information

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific Configuration in an organization.

**Availability**:
- Apple Business API 2.6+

## Overview

> **Note**: Use this API to retrieve the `customSettingsValues` for a `CUSTOM_SETTING` Configuration.

### Example

**Request**:

```
curl "https://api-business.apple.com/v1/configurations/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
{
  "data": {
    "type": "configurations",
    "id": "config-12345",
    "attributes": {
      "type": "CUSTOM_SETTING",
      "name": "Wi-Fi Configuration",
      "configuredForPlatforms": [
        "PLATFORM_IOS",
        "PLATFORM_MACOS"
      ],
      "customSettingsValues": {
        "configurationProfile": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>...",
        "filename": "WiFi.mobileconfig"
      },
      "createdDateTime": "2024-01-15T10:30:00Z",
      "updatedDateTime": "2024-06-01T14:22:00Z"
    },
    "links": {
      "self": "https://api-business.apple.com/v1/configurations/config-12345"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/configurations/config-12345"
  }
}
```

## Topics

### Responses
- [object ConfigurationResponse](./configurationresponse.md)
  A response that contains information about a Configuration resource.

## Endpoint

`GET https://api-business.apple.com/v1/configurations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[configurations]` ([string]): The fields to return for included related types.

  **Allowed Values**: `type`, `name`, `configuredForPlatforms`, `customSettingsValues`, `createdDateTime`, `updatedDateTime`

## Responses

- `200` OK (`ConfigurationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Configurations
- [Get Configurations](./get-configurations.md)
  Get a list of Configurations in an organization.
- [Create a Configuration](./create-a-configuration.md)
  Create a new custom Configuration in an organization.
- [Update a Configuration](./update-a-configuration.md)
  Update an existing custom Configuration in an organization.
- [Delete a Configuration](./delete-a-configuration.md)
  Delete a Configuration from an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-configuration-information)*