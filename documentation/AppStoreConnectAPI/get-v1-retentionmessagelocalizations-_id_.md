# Read a retention message localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read details about a specific retention message localization.

**Availability**:
- App Store Connect API 4.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/retentionMessageLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the retention message localization resource ID from the [`List localizations for a retention message version`](./get-v1-retentionmessageversions-_id_-localizations.md) response.

### Query Parameters

- `fields[retentionMessageLocalizations]` ([string]): Additional fields to include for each retention message localization resource returned by the response.

  **Allowed Values**: `locale`, `header`, `body`, `retentionMessageVersion`
- `fields[retentionMessageVersions]` ([string]): Additional fields to include for each retention message version resource returned by the response.

  **Allowed Values**: `state`, `retentionMessage`, `localizations`, `placement`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `retentionMessageVersion`

## Responses

- `200` OK (`RetentionMessageLocalizationResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-retentionmessagelocalizations-_id_)*