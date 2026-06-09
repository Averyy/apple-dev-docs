# Delete a profile

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a provisioning profile that is used for app development or distribution.

**Availability**:
- App Store Connect API 1.1+

#### Discussion

You can delete provisioning profiles, and may wish to do so if they are expiring or obsolete.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/profiles/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create a profile](post-v1-profiles.md)
  Create a new provisioning profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-profiles-_id_)*