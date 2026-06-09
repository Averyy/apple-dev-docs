# List App Tags

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all app tags for a specific app.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appTags`

## Parameters

- `fields[appTags]` ([string]): Additional fields to include for each app tag resource returned by the response.
- `fields[territories]` ([string]): Additional fields to include for each territory resource returned by the response.
- `filter[visibleInAppStore]` ([string]): Filter the returned app tags by visibility in the App Store.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of app tag resources to return.
- `limit[territories]` (integer): The maximum number of related territory resources to return.
- `sort` ([string]): Attributes by which to sort.

## See Also

- [List app tags IDs](get-v1-apps-_id_-relationships-apptags.md)
  List all app tag IDs for a specific app.
- [List territory IDs for an app tag](get-v1-apptags-_id_-relationships-territories.md)
  List territory IDs for an app tag.
- [List Territories for an App Tag](get-v1-apptags-_id_-territories.md)
  List territory availability for a specific app tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-apptags)*