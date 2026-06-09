# Read the Android to iOS App Mapping Details for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about the Android to iOS app mapping for a specific app.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/androidToIosAppMappingDetails`

## Parameters

- `fields[androidToIosAppMappingDetails]` ([string]): Additional fields to include for each Android to iOS app mapping detail resource returned by the response.
- `limit` (integer): The maximum number of Android to iOS app mapping detail resources to return.

## See Also

- [List the IDs of Android to iOS App Mapping Details for an App](get-v1-apps-_id_-relationships-androidtoiosappmappingdetails.md)
  Get the IDs of Android to iOS app mapping details for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-androidtoiosappmappingdetails)*