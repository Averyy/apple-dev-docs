# List territory IDs for an end user license agreement

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/{id}/relationships/territories`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`EndUserLicenseAgreementTerritoriesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Territories
- [List territories](./get-v1-territories.md)
  List all territories where the App Store operates.
- [List all territories for an end user license agreement](./get-v1-enduserlicenseagreements-_id_-territories.md)
  List all the App Store territories to which a specific custom app license agreement applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-enduserlicenseagreements-_id_-relationships-territories)*