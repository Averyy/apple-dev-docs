# declaration/activation/{identifier}

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

The endpoint for fetching an activation declaration.

## Endpoint

`PUT https://yourmdmhost.example.com/checkin`

## Parameters

### Path Parameters

- `identifier` (string) *(required)*: The identifier of the activation declaration to fetch.

## Responses

- `200` OK (`DeclarationResponse`, `application/json`): The details of the activation declaration.
- `404` Not Found: The system doesn’t support the activation declaration with the specified identifier.

## See Also

### Declaration Endpoints
- [declaration/asset/{identifier}](./declaration-asset-_identifier_.md)
  The endpoint for fetching an asset declaration.
- [declaration/configuration/{identifier}](./declaration-configuration-_identifier_.md)
  The endpoint for fetching a configuration declaration.
- [declaration/management/{identifier}](./declaration-management-_identifier_.md)
  The endpoint for fetching a management declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declaration-activation-_identifier_)*