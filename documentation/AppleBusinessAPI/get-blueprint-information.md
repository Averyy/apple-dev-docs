# Get Blueprint Information

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific Blueprint in an organization.

**Availability**:
- Apple Business API 2.7+

### Example

**Request**:

```
curl "https://api-business.apple.com/v1/blueprints/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
{
  "data": {
    "type": "blueprints",
    "id": "blueprint-12345",
    "attributes": {
      "name": "Engineering Onboarding",
      "description": "Standard apps for engineering team",
      "status": "ACTIVE",
      "appLicenseDeficient": false,
      "createdDateTime": "2024-01-15T10:30:00Z",
      "updatedDateTime": "2024-06-01T14:22:00Z"
    },
    "relationships": {
      "apps": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/apps",
          "related": "https://api-business.apple.com/v1/blueprints/blueprint-12345/apps"
        }
      },
      "users": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/users",
          "related": "https://api-business.apple.com/v1/blueprints/blueprint-12345/users"
        }
      }
      "packages": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/packages",
          "related": "https://api-business.apple.com/v1/blueprints/blueprint-12345/packages"
        }
      },
      "userGroups": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/userGroups",
          "related": "https://api-business.apple.com/v1/blueprints/blueprint-12345/userGroups"
        }
      },
      "orgDevices": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/orgDevices",
          "related": "https://api-business.apple.com/v1/blueprints/blueprint-12345/orgDevices"
        }
      },
      "configurations": {
        "links": {
          "self": "https://api-business.apple.com/v1/blueprints/blueprint-12345/relationships/configurations",
          "related": "https://api-business.apple.com/v1/blueprints/blueprint-12345/configurations"
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

`GET https://api-business.apple.com/v1/blueprints/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `fields[blueprints]` ([string]): The fields to return for included related types.

  **Allowed Values**: `name`, `description`, `status`, `createdDateTime`, `updatedDateTime`, `appLicenseDeficient`, `apps`, `packages`, `configurations`, `orgDevices`, `users`, `userGroups`
- `include` ([string]): Related resources to include in the response. Possible values: `apps`, `configurations`, `packages`, `orgDevices`, `users`, `userGroups`.

  **Allowed Values**: `apps`, `packages`, `configurations`, `orgDevices`, `users`, `userGroups`
- `limit[apps]` (integer): Maximum number of related apps to include.

  **Maximum**: `1000`
- `limit[configurations]` (integer): Maximum number of related configurations to include.

  **Maximum**: `1000`
- `limit[packages]` (integer): Maximum number of related packages to include.

  **Maximum**: `1000`
- `limit[orgDevices]` (integer): Maximum number of related devices to include.

  **Maximum**: `1000`
- `limit[users]` (integer): Maximum number of related users to include.

  **Maximum**: `1000`
- `limit[userGroups]` (integer): Maximum number of related user groups to include.

  **Maximum**: `1000`

## Responses

- `200` OK (`BlueprintResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Blueprints
- [Get Blueprints](./get-blueprints.md)
  Get a list of Blueprints in an organization.
- [Create a Blueprint](./create-a-blueprint.md)
  Create a new Blueprint in an organization.
- [Update a Blueprint](./update-a-blueprint.md)
  Update an existing Blueprint in an organization.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-blueprint-information)*