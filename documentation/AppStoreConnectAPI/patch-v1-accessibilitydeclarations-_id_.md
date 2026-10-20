# Modify an Accessibility Declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the attributes of a specific accessibility declaration.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring accessibility declarations for your app](./configuring-accessibility-declarations.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/accessibilityDeclarations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `accessibilityDeclarations` resource ID from the [`List All Accessibility Declarations for an App`](./get-v1-apps-_id_-accessibilitydeclarations.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AccessibilityDeclarationUpdateRequest`

## Responses

- `200` OK (`AccessibilityDeclarationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
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
- [Create an Accessibility Declaration](./post-v1-accessibilitydeclarations.md)
  Add an accessibility declaration for a specific app.
- [Delete an Accessibility Declaration](./delete-v1-accessibilitydeclarations-_id_.md)
  Delete a specific accessibility declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-accessibilitydeclarations-_id_)*