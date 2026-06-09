# Read app category information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a specific app category.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCategories/{id}`

## Parameters

- `fields[appCategories]` ([string]): Additional fields to include for each app categories resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[subcategories]` (integer): The maximum number of related subcategories resources to return.

## See Also

- [Read the parent information of an app category](get-v1-appcategories-_id_-parent.md)
  Get the App Store category to which a specific subcategory belongs.
- [Get the parent category ID for an app category](get-v1-appcategories-_id_-relationships-parent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcategories-_id_)*