# Read end user license agreement information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the custom end user license agreement associated with an app, and the territories it applies to.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/{id}`

## Parameters

- `fields[endUserLicenseAgreements]` ([string])
- `fields[territories]` ([string])
- `include` ([string])
- `limit[territories]` (integer)
- `fields[apps]` ([string])

## See Also

- [Read the end user license agreement information of an app](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [List all territories for an end user license agreement](get-v1-enduserlicenseagreements-_id_-territories.md)
  List all the App Store territories to which a specific custom app license agreement applies.
- [List territory IDs for an end user license agreement](get-v1-enduserlicenseagreements-_id_-relationships-territories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-enduserlicenseagreements-_id_)*