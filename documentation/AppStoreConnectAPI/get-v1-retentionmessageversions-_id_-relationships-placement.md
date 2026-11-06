# Read the placement ID for a retention message version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the image placement ID for a specific retention message version.

**Availability**:
- App Store Connect API 4.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/retentionMessageVersions/{id}/relationships/placement`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the retention message version resource ID from the [`List versions for a retention message`](./get-v1-retentionmessages-_id_-versions.md) response.

## Responses

- `200` OK (`RetentionMessageVersionPlacementLinkageResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Getting retention message versions
- [Read a retention message version](./get-v1-retentionmessageversions-_id_.md)
  Read details about a specific retention message version, including its review state.
- [List localizations for a retention message version](./get-v1-retentionmessageversions-_id_-localizations.md)
  Get a list of localizations for a specific retention message version.
- [List localization IDs for a retention message version](./get-v1-retentionmessageversions-_id_-relationships-localizations.md)
  Get a list of localization IDs for a specific retention message version.
- [Read the placement for a retention message version](./get-v1-retentionmessageversions-_id_-placement.md)
  Get the image placement for a specific retention message version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-retentionmessageversions-_id_-relationships-placement)*