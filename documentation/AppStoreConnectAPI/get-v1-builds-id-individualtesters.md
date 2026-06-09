# List all individual testers for a build

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of beta testers individually assigned to a build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}/individualTesters`

## Parameters

- `limit` (integer): Number of resources to return
- `fields[betaTesters]` ([string]): Fields to return for included related types.

## See Also

- [Get all resource ids of individual testers for a build](get-v1-builds-_id_-relationships-individualtesters.md)
  Get a list of resource IDs of individual testers associated with a build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-individualtesters)*