# List all devices in a profile

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of all devices for a specific provisioning profile.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/profiles/{id}/devices`

## Parameters

- `limit` (integer)
- `fields[devices]` ([string])

## See Also

- [Read the bundle id in a profile](get-v1-profiles-_id_-bundleid.md)
  Get the bundle ID information for a specific provisioning profile.
- [Get the bundle ID for a profile](get-v1-profiles-_id_-relationships-bundleid.md)
- [List all certificates in a profile](get-v1-profiles-_id_-certificates.md)
  Get a list of all certificates and their data for a specific provisioning profile.
- [List certificate IDs for a profile](get-v1-profiles-_id_-relationships-certificates.md)
- [List device IDs for a profile](get-v1-profiles-_id_-relationships-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-profiles-_id_-devices)*