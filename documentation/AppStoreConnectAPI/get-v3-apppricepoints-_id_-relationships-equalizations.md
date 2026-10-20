# List equalization price point IDs for an app price point

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of equalization price point IDs for a specific app price point.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v3/appPricePoints/{id}/relationships/equalizations`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`AppPricePointV3EqualizationsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting an app’s price points
- [List All Price Points for an App](./get-v1-apps-_id_-apppricepoints.md)
  Get all the available price points for a specific app.
- [List app price point IDs for an app](./get-v1-apps-_id_-relationships-apppricepoints.md)
- [Read App Price Point Information](./get-v3-apppricepoints-_id_.md)
  Get details about a specific app price point.
- [List App Price Point Equalizations](./get-v3-apppricepoints-_id_-equalizations.md)
  List all equivalent app prices points to a base price point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v3-apppricepoints-_id_-relationships-equalizations)*