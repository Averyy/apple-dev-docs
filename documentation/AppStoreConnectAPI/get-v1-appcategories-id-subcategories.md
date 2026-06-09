# List all subcategories for an app category

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all App Store subcategories that belong to a specific category.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCategories/{id}/subcategories`

## Parameters

- `fields[appCategories]` ([string]): Additional fields to include for each app categories resource returned by the response.
- `limit` (integer): The maximum number of app categories resources to return.

## See Also

- [List app categories](get-v1-appcategories.md)
  List all categories on the App Store, including the category and subcategory hierarchy.
- [List subcategory IDs for an app category](get-v1-appcategories-_id_-relationships-subcategories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcategories-_id_-subcategories)*