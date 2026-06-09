# Modify an Accessibility Declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the attributes of a specific accessibility declaration.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring accessibility declarations for your app](configuring-accessibility-declarations.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/accessibilityDeclarations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `accessibilityDeclarations` resource ID from the [`List All Accessibility Declarations for an App`](get-v1-apps-_id_-accessibilitydeclarations.md) response.

## See Also

- [List All Accessibility Declarations for an App](get-v1-apps-_id_-accessibilitydeclarations.md)
  Get a list of the accessibility declarations for a specific app.
- [List accessibility declaration IDs for an app](get-v1-apps-_id_-relationships-accessibilitydeclarations.md)
- [Read Accessibility Declaration Information](get-v1-accessibilitydeclarations-_id_.md)
  Get information about a specific accessibility declaration.
- [Create an Accessibility Declaration](post-v1-accessibilitydeclarations.md)
  Add an accessibility declaration for a specific app.
- [Delete an Accessibility Declaration](delete-v1-accessibilitydeclarations-_id_.md)
  Delete a specific accessibility declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-accessibilitydeclarations-_id_)*