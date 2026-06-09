# List all source code management providers

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all source code management providers you connected to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmProviders`

## Parameters

- `fields[scmProviders]` ([string]): Additional fields to include for each Providers resource returned by the response.
- `limit` (integer): The number of Providers resources to return.

## See Also

- [Get a source code management provider](get-v1-scmproviders-_id_.md)
  Get information about a specific source code management provider you connected to Xcode Cloud.
- [List all repositories for a source code management provider](get-v1-scmproviders-_id_-repositories.md)
  List all Git repositories for a specific source code management provider you connected to Xcode Cloud.
- [List repository IDs for an SCM provider](get-v1-scmproviders-_id_-relationships-repositories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmproviders)*