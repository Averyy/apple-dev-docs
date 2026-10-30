# Update a Blueprint

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update an existing Blueprint in an organization.

**Availability**:
- Apple Business API 2.7+

## Overview

> **Note**: Only the fields included in the request are updated. Any omitted fields retain their existing values.

> **Note**: Any invalid resource IDs will be dropped from the request during Blueprint update.

### Example

**Request**:

```
curl -X PATCH "https://api-business.apple.com/v1/blueprints/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{
      "data": {
        "type": "blueprints",
        "id": "blueprint-12345",
        "attributes": {
          "description": "Updated description"
        },
        "relationships": {
          "apps": {
            "data": [
              {"type": "apps", "id": "361309726"}
            ]
          },
          "users": {
            "data": [
              {"type": "users", "id": "user-215"},
              {"type": "users", "id": "user-225"},
              {"type": "users", "id": "user-235"},
            ]
          }
        }
      }
    }'
```

**Response**:

```json
{
  "data": {
    "type": "blueprints",
    "id": "blueprint-12345",
    "attributes": {
      "name": "Engineering Onboarding",
      "description": "Updated description",
      "status": "ACTIVE",
      "appLicenseDeficient": false,
      "createdDateTime": "2024-01-15T10:30:00Z",
      "updatedDateTime": "2024-06-15T14:22:00Z"
    },
    "relationships": {
      "userGroups": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/userGroups",
          "include": "https://api-business.apple.com/v1/blueprints/blueprint-12345?include=userGroups"
        }
      },
      "orgDevices": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/orgDevices",
          "include": "https://api-business.apple.com/v1/blueprints/blueprint-12345?include=orgDevices"
        }
      },
      "packages": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/packages",
          "include": "https://api-business.apple.com/v1/blueprints/blueprint-12345?include=packages"
        }
      },
      "configurations": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/configurations",
          "include": "https://api-business.apple.com/v1/blueprints/blueprint-12345?include=configurations"
        }
      },
      "users": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/users",
          "include": "https://api-business.apple.com/v1/blueprints/blueprint-12345?include=users"
        }
      },
      "apps": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/apps",
          "include": "https://api-business.apple.com/v1/blueprints/blueprint-12345?include=apps"
        }
      }
    },
    "links": {
      "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345"
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345"
  }
}
```

## Topics

### Responses
- [object BlueprintResponse](./blueprintresponse.md)
  A response that contains information about a Blueprint resource.

## Endpoint

`PATCH https://api-business.apple.com/v1/blueprints/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BlueprintUpdateRequest`

## Responses

- `200` OK (`BlueprintResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`): Request entity error(s).
- `422` (`ErrorResponse`, `application/json`): Unprocessable request entity error(s).
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Blueprints
- [Get Blueprints](./get-blueprints.md)
  Get a list of Blueprints in an organization.
- [Create a Blueprint](./create-a-blueprint.md)
  Create a new Blueprint in an organization.
- [Get Blueprint Information](./get-blueprint-information.md)
  Get information about a specific Blueprint in an organization.
- [Delete a Blueprint](./delete-a-blueprint.md)
  Delete a Blueprint from an organization.
- [Get App IDs for a Blueprint](./get-all-app-ids-for-a-blueprint.md)
  Get a list of app IDs associated with a Blueprint.
- [Add Apps to a Blueprint](./add-apps-to-a-blueprint.md)
  Add apps to a Blueprint.
- [Remove Apps from a Blueprint](./remove-apps-from-a-blueprint.md)
  Remove apps from a Blueprint.
- [Get Configuration IDs for a Blueprint](./get-all-configuration-ids-for-a-blueprint.md)
  Get a list of Configuration IDs associated with a Blueprint.
- [Add Configurations to a Blueprint](./add-configurations-to-a-blueprint.md)
  Add Configurations to a Blueprint.
- [Remove Configurations from a Blueprint](./remove-configurations-from-a-blueprint.md)
  Remove Configurations from a Blueprint.
- [Get Package IDs for a Blueprint](./get-all-package-ids-for-a-blueprint.md)
  Get a list of package IDs associated with a Blueprint.
- [Add Packages to a Blueprint](./add-packages-to-a-blueprint.md)
  Add packages to a Blueprint.
- [Remove Packages from a Blueprint](./remove-packages-from-a-blueprint.md)
  Remove packages from a Blueprint.
- [Get Device IDs for a Blueprint](./get-all-orgdevice-ids-for-a-blueprint.md)
  Get a list of device IDs associated with a Blueprint.
- [Add Devices to a Blueprint](./add-org-devices-to-a-blueprint.md)
  Add devices to a Blueprint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/update-a-blueprint)*