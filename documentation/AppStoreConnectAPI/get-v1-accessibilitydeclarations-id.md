# Read Accessibility Declaration Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific accessibility declaration.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring accessibility declarations for your app](configuring-accessibility-declarations.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/accessibilityDeclarations/{id}`

## Parameters

- `fields[accessibilityDeclarations]` ([string])

## See Also

- [List All Accessibility Declarations for an App](get-v1-apps-_id_-accessibilitydeclarations.md)
  Get a list of the accessibility declarations for a specific app.
- [GET /v1/apps/{id}/relationships/accessibilityDeclarations](get-v1-apps-_id_-relationships-accessibilitydeclarations.md)
- [Create an Accessibility Declaration](post-v1-accessibilitydeclarations.md)
  Add an accessibility declaration for a specific app.
- [Modify an Accessibility Declaration](patch-v1-accessibilitydeclarations-_id_.md)
  Update the attributes of a specific accessibility declaration.
- [Delete an Accessibility Declaration](delete-v1-accessibilitydeclarations-_id_.md)
  Delete a specific accessibility declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-accessibilitydeclarations-_id_)*