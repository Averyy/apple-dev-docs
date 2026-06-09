# Read the routing app coverage information of an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the routing app coverage file that is associated with a specific App Store version

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/routingAppCoverage`

## Parameters

- `fields[routingAppCoverages]` ([string]): Additional fields to include for each routing app coverage resource returned by the response.
- `fields[appStoreVersions]` ([string])
- `include` ([string])

## See Also

- [Get the routing app coverage ID for an App Store version](get-v1-appstoreversions-_id_-relationships-routingappcoverage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-routingappcoverage)*