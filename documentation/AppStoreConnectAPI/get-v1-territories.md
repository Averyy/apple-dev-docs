# List territories

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all territories where the App Store operates.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/territories`

## Parameters

### Query Parameters

- `fields[territories]` ([string]): **Allowed Values**: `currency`
- `limit` (integer): Number of resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`TerritoriesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Territories
- [List all territories for an end user license agreement](./get-v1-enduserlicenseagreements-_id_-territories.md)
  List all the App Store territories to which a specific custom app license agreement applies.
- [List territory IDs for an end user license agreement](./get-v1-enduserlicenseagreements-_id_-relationships-territories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-territories)*