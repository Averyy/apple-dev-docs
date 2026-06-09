# Read and download profile information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information for a specific provisioning profile and download its data.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/profiles/{id}`

## Parameters

- `fields[certificates]` ([string])
- `fields[devices]` ([string])
- `fields[profiles]` ([string])
- `include` ([string])
- `fields[bundleIds]` ([string])
- `limit[devices]` (integer)
- `limit[certificates]` (integer)

## See Also

- [List and download profiles](get-v1-profiles.md)
  Find and list provisioning profiles and download their data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-profiles-_id_)*