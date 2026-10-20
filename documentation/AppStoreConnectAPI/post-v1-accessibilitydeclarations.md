# Create an Accessibility Declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add an accessibility declaration for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring accessibility declarations for your app](./configuring-accessibility-declarations.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/accessibilityDeclarations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AccessibilityDeclarationCreateRequest`

## Responses

- `201` Created (`AccessibilityDeclarationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing accessibility metadata
- [List All Accessibility Declarations for an App](./get-v1-apps-_id_-accessibilitydeclarations.md)
  Get a list of the accessibility declarations for a specific app.
- [List accessibility declaration IDs for an app](./get-v1-apps-_id_-relationships-accessibilitydeclarations.md)
- [Read Accessibility Declaration Information](./get-v1-accessibilitydeclarations-_id_.md)
  Get information about a specific accessibility declaration.
- [Modify an Accessibility Declaration](./patch-v1-accessibilitydeclarations-_id_.md)
  Update the attributes of a specific accessibility declaration.
- [Delete an Accessibility Declaration](./delete-v1-accessibilitydeclarations-_id_.md)
  Delete a specific accessibility declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-accessibilitydeclarations)*