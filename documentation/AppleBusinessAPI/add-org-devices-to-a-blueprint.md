# Add Devices to a Blueprint

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add devices to a Blueprint.

**Availability**:
- Apple Business API 2.6+

### Example

**Request**:

```
curl -X POST "https://api-business.apple.com/v1/blueprints/{id}/relationships/orgDevices" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{
      "data": [
        {"type": "orgDevices", "id": "ABC123DEF456"}
      ]
    }'
```

**Response**:

```
HTTP/1.1 204 No Content
```

## Endpoint

`POST https://api-business.apple.com/v1/blueprints/{id}/relationships/orgDevices`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BlueprintOrgDevicesLinkagesRequest`

## Responses

- `204` No Content
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/add-org-devices-to-a-blueprint)*