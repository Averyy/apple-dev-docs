# List and Download Profiles

**Framework**: Enterprise Program API  
**Kind**: httpRequest

Find and list provisioning profiles and download their data.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/profiles`

## Parameters

- `fields[bundleIds]` ([string])
- `fields[certificates]` ([string])
- `fields[devices]` ([string])
- `fields[profiles]` ([string])
- `filter[id]` ([string])
- `filter[name]` ([string])
- `filter[profileState]` ([string])
- `filter[profileType]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[certificates]` (integer)
- `limit[devices]` (integer)
- `sort` ([string])

## See Also

- [Read and Download Profile Information](read-and-download-profile-information.md)
  Get information for a specific provisioning profile and download its data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-and-download-profiles)*