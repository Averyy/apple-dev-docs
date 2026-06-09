# Read the parent information of an app category

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the App Store category to which a specific subcategory belongs.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCategories/{id}/parent`

## Parameters

- `fields[appCategories]` ([string]): Additional fields to include for each app categories resource returned by the response.

## See Also

- [Read app category information](get-v1-appcategories-_id_.md)
  Get a specific app category.
- [Get the parent category ID for an app category](get-v1-appcategories-_id_-relationships-parent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcategories-_id_-parent)*