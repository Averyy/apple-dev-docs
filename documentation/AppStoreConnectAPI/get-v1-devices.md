# List Devices

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list devices registered to your team.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/devices`

## Parameters

- `fields[devices]` ([string])
- `filter[id]` ([string])
- `filter[name]` ([string])
- `filter[platform]` ([string])
- `filter[status]` ([string])
- `filter[udid]` ([string])
- `limit` (integer)
- `sort` ([string])

## See Also

- [Read Device Information](get-v1-devices-_id_.md)
  Get information for a specific device registered to your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-devices)*