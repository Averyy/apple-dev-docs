# List and download profiles

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list provisioning profiles and download their data.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/profiles`

## Parameters

- `fields[certificates]` ([string])
- `fields[devices]` ([string])
- `fields[profiles]` ([string])
- `filter[id]` ([string])
- `filter[name]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[certificates]` (integer)
- `limit[devices]` (integer)
- `sort` ([string])
- `fields[bundleIds]` ([string])
- `filter[profileState]` ([string])
- `filter[profileType]` ([string])

## See Also

- [Read and download profile information](get-v1-profiles-_id_.md)
  Get information for a specific provisioning profile and download its data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-profiles)*