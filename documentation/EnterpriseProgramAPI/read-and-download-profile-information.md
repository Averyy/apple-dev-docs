# Read and Download Profile Information

**Framework**: Enterprise Program API  
**Kind**: httpRequest

Get information for a specific provisioning profile and download its data.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/profiles/{id}`

## Parameters

- `fields[bundleIds]` ([string])
- `fields[certificates]` ([string])
- `fields[devices]` ([string])
- `fields[profiles]` ([string])
- `include` ([string])
- `limit[certificates]` (integer)
- `limit[devices]` (integer)

## See Also

- [List and Download Profiles](list-and-download-profiles.md)
  Find and list provisioning profiles and download their data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/read-and-download-profile-information)*