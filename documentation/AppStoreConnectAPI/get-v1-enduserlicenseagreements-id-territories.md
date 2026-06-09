# List all territories for an end user license agreement

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all the App Store territories to which a specific custom app license agreement applies.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/{id}/territories`

## Parameters

- `fields[territories]` ([string])
- `limit` (integer): Number of resources to return.

## See Also

- [List territories](get-v1-territories.md)
  List all territories where the App Store operates.
- [List territory IDs for an end user license agreement](get-v1-enduserlicenseagreements-_id_-relationships-territories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-enduserlicenseagreements-_id_-territories)*