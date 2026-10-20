# List all source code management providers

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all source code management providers you connected to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmProviders`

## Parameters

### Query Parameters

- `fields[scmProviders]` ([string]): Additional fields to include for each Providers resource returned by the response.

  **Allowed Values**: `scmProviderType`, `url`, `repositories`
- `limit` (integer): The number of Providers resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`ScmProvidersResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Provider Information
- [Get a source code management provider](./get-v1-scmproviders-_id_.md)
  Get information about a specific source code management provider you connected to Xcode Cloud.
- [List all repositories for a source code management provider](./get-v1-scmproviders-_id_-repositories.md)
  List all Git repositories for a specific source code management provider you connected to Xcode Cloud.
- [List repository IDs for an SCM provider](./get-v1-scmproviders-_id_-relationships-repositories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmproviders)*