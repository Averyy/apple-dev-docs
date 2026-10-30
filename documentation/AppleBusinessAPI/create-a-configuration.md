# Create a Configuration

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a new custom Configuration in an organization.

**Availability**:
- Apple Business API 2.7+

## Overview

> ❗ **Important**: Only Configurations with type `CUSTOM_SETTING` can be created with the API.

> **Note**: `configurationProfile` is required. `filename` is optional — if omitted, a default filename is generated from the Configuration ID. `configuredForPlatforms` is optional — if omitted, supported platforms are auto-detected from the payload content in the Configuration profile. The profile must be compatible with the resolved platforms.

### Example

**Request**:

```
curl -X POST "https://api-business.apple.com/v1/configurations" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{
      "data": {
        "type": "configurations",
        "attributes": {
          "type": "CUSTOM_SETTING",
          "name": "AirPlay Security Settings",
          "configuredForPlatforms": ["PLATFORM_IOS"],
          "customSettingsValues": {
            "configurationProfile": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\"><dict><key>PayloadContent</key><array><dict><key>AccessType</key><string>WIFI_ONLY</string><key>PayloadType</key><string>com.apple.airplay.security</string></dict></array></dict></plist>",
            "filename": "Airplay.mobileconfig"
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
    "id": "config-new-456",
    "attributes": {
      "type": "CUSTOM_SETTING",
      "name": "AirPlay Security Settings",
      "configuredForPlatforms": [
        "PLATFORM_IOS"
      ],
      "customSettingsValues": {
        "configurationProfile": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>...",
        "filename": "Airplay.mobileconfig"
      },
      "createdDateTime": "2024-06-15T10:30:00Z",
      "updatedDateTime": "2024-06-15T10:30:00Z"
    },
    "links": {
      "self": "https://api-business.apple.com/v1/configurations/config-new-456"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/configurations/config-new-456"
  }
}
```

## Topics

### Responses
- [object ConfigurationResponse](./configurationresponse.md)
  A response that contains information about a Configuration resource.

## Endpoint

`POST https://api-business.apple.com/v1/configurations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `ConfigurationCreateRequest`

## Responses

- `201` Created (`ConfigurationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): Request entity error(s).
- `422` (`ErrorResponse`, `application/json`): Unprocessable request entity error(s).
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Configurations
- [Get Configurations](./get-configurations.md)
  Get a list of Configurations in an organization.
- [Get Configuration Information](./get-configuration-information.md)
  Get information about a specific Configuration in an organization.
- [Update a Configuration](./update-a-configuration.md)
  Update an existing custom Configuration in an organization.
- [Delete a Configuration](./delete-a-configuration.md)
  Delete a Configuration from an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/create-a-configuration)*