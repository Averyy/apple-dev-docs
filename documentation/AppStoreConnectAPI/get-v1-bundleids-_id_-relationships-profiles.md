# List profile IDs for a bundle ID

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/bundleIds/{id}/relationships/profiles`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`BundleIdProfilesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Related Data
- [Read the app information of a bundle id](./get-v1-bundleids-_id_-app.md)
- [List all profiles for a bundle id](./get-v1-bundleids-_id_-profiles.md)
  Get a list of all profiles for a specific bundle ID.
- [List all capabilities for a bundle id](./get-v1-bundleids-_id_-bundleidcapabilities.md)
  Get a list of all capabilities for a specific bundle ID.
- [Get the app ID for a bundle ID](./get-v1-bundleids-_id_-relationships-app.md)
- [Read bundle Id capabilities ids for a bundle Id](./get-v1-bundleids-_id_-relationships-bundleidcapabilities.md)
  List all bundleIdCapabilities IDs for a specific bundle Id.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-bundleids-_id_-relationships-profiles)*