# Read the Routing App Coverage Information of an App Store Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the routing app coverage file that is associated with a specific App Store version

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/routingAppCoverage`

## Parameters

- `fields[routingAppCoverages]` ([string])
- `fields[appStoreVersions]` ([string])
- `include` ([string])

## See Also

- [GET /v1/appStoreVersions/{id}/relationships/routingAppCoverage](get-v1-appstoreversions-_id_-relationships-routingappcoverage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-routingappcoverage)*