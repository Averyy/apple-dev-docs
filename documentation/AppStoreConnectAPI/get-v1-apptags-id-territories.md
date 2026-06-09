# List Territories for an App Tag

**Framework**: App Store Connect API  
**Kind**: httpRequest

List territory availability for a specific app tag.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appTags/{id}/territories`

## Parameters

- `fields[territories]` ([string]): Additional fields to include for each territory resource returned by the response.
- `limit` (integer): The maximum number of territory resources to return.

## See Also

- [List App Tags](get-v1-apps-_id_-apptags.md)
  List all app tags for a specific app.
- [List app tags IDs](get-v1-apps-_id_-relationships-apptags.md)
  List all app tag IDs for a specific app.
- [List territory IDs for an app tag](get-v1-apptags-_id_-relationships-territories.md)
  List territory IDs for an app tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apptags-_id_-territories)*