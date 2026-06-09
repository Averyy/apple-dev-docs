# Read the app store version submission information of an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the App Review submission for a specific App Store version.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/appStoreVersionSubmission`

## Parameters

- `fields[appStoreVersionSubmissions]` ([string]): Additional fields to include for each App Store version submission resource returned by the response.
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.
- `include` ([string]): The relationship data to include in the response.

## See Also

- [Get the App Store version submission ID for an App Store version](get-v1-appstoreversions-_id_-relationships-appstoreversionsubmission.md)
- [Read the app store review details resource information of an app store version](get-v1-appstoreversions-_id_-appstorereviewdetail.md)
  Get the details you provide to App Review so they can test your app.
- [Get the App Store review detail ID for an App Store version](get-v1-appstoreversions-_id_-relationships-appstorereviewdetail.md)
- [Read the app store version phased release information of an app store version](get-v1-appstoreversions-_id_-appstoreversionphasedrelease.md)
  Read the phased release status and configuration for a version with phased release enabled.
- [Get the phased release ID for an App Store version](get-v1-appstoreversions-_id_-relationships-appstoreversionphasedrelease.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-appstoreversionsubmission)*