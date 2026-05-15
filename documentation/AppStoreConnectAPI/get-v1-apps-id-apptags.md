# List App Tags

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all app tags for a specific app.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appTags`

## Parameters

- `fields[appTags]` ([string])
- `fields[territories]` ([string])
- `filter[visibleInAppStore]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[territories]` (integer)
- `sort` ([string])

## See Also

- [List App Tags IDs](get-v1-apps-_id_-relationships-apptags.md)
  List all app tag IDs for a specific app.
- [List Territory IDs for an App Tag](get-v1-apptags-_id_-relationships-territories.md)
  List territory IDs for an app tag.
- [List Territories for an App Tag](get-v1-apptags-_id_-territories.md)
  List territory availability for a specific app tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-apptags)*