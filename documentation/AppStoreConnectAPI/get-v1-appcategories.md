# List App Categories

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all categories on the App Store, including the category and subcategory hierarchy.

**Availability**:
- App Store Connect API 1.2+

#### Discussion

Use this endpoint to retrieve the list of available App Store categories and subcategories. Associate an app with categories using the [`Modify an App Info`](patch-v1-appinfos-_id_.md) endpoint.

The first example retrieves the full category and subcategory hierarchy in one request. The second example retrieves just the top-level categories for macOS apps.

##### Get All App Categories and Subcategories

##### Get All Top Level Categories That Apply to Macos Apps

## See Also

- [List All Subcategories for an App Category](get-v1-appcategories-_id_-subcategories.md)
  List all App Store subcategories that belong to a specific category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcategories)*