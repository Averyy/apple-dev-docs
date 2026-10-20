# declaration/asset/{identifier}

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

The endpoint for fetching an asset declaration.

## Endpoint

`PUT https://yourmdmhost.example.com/checkin`

## Parameters

### Path Parameters

- `identifier` (string) *(required)*: The identifier of the asset declaration to fetch.

## Responses

- `200` OK (`DeclarationResponse`, `application/json`): The details of the asset declaration.
- `404` Not Found: The system doesn’t have an asset with the specified identifier.

## See Also

### Declaration Endpoints
- [declaration/activation/{identifier}](./declaration-activation-_identifier_.md)
  The endpoint for fetching an activation declaration.
- [declaration/configuration/{identifier}](./declaration-configuration-_identifier_.md)
  The endpoint for fetching a configuration declaration.
- [declaration/management/{identifier}](./declaration-management-_identifier_.md)
  The endpoint for fetching a management declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declaration-asset-_identifier_)*