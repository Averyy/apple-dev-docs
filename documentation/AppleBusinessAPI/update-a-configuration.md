# Update a Configuration

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update an existing custom Configuration in an organization.

**Availability**:
- Apple Business API 2.6+

## Overview

> ❗ **Important**: Only Configurations with type `CUSTOM_SETTING` can be updated via the API.

> **Note**: If a `filename` is provided, it must end in `.mobileconfig`. A provided `configurationProfile` is validated and must be compatible with the resolved `configuredForPlatforms` (either from the request or the existing value on the Configuration).

> **Note**: Only the fields included in the request are updated. One of `name`, `configuredForPlatforms`, `configurationProfile`, or `filename` must be included, and any omitted fields retain their existing values.

### Example

**Request**:

```
curl -X PATCH "https://api-business.apple.com/v1/configurations/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{
      "data": {
        "type": "configurations",
        "id": "config-12345",
        "attributes": {
          "name": "Updated Wi-Fi Configuration",
          "configuredForPlatforms": ["PLATFORM_IOS", "PLATFORM_MACOS"],
          "customSettingsValues": {
            "configurationProfile": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>...",
            "filename": "WiFi-Updated.mobileconfig"
          }
        }
      }
    }'
```

**Response**:

```json
{
  "data": {
    "type": "configurations",
    "id": "config-12345",
    "attributes": {
      "type": "CUSTOM_SETTING",
      "name": "Updated Wi-Fi Configuration",
      "configuredForPlatforms": [
        "PLATFORM_IOS",
        "PLATFORM_MACOS"
      ],
      "customSettingsValues": {
        "configurationProfile": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>...",
        "filename": "WiFi-Updated.mobileconfig"
      },
      "createdDateTime": "2024-01-15T10:30:00Z",
      "updatedDateTime": "2024-06-15T14:22:00Z"
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

`PATCH https://api-business.apple.com/v1/configurations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `ConfigurationUpdateRequest`

## Responses

- `200` OK (`ConfigurationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`): Request entity error(s).
- `422` (`ErrorResponse`, `application/json`): Unprocessable request entity error(s).
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Configurations
- [Get Configurations](./get-configurations.md)
  Get a list of Configurations in an organization.
- [Create a Configuration](./create-a-configuration.md)
  Create a new custom Configuration in an organization.
- [Get Configuration Information](./get-configuration-information.md)
  Get information about a specific Configuration in an organization.
- [Delete a Configuration](./delete-a-configuration.md)
  Delete a Configuration from an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/update-a-configuration)*