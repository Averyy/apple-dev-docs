# Read Accessibility Declaration Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific accessibility declaration.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring accessibility declarations for your app](./configuring-accessibility-declarations.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/accessibilityDeclarations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `accessibilityDeclarations` resource ID from the [`List All Accessibility Declarations for an App`](./get-v1-apps-_id_-accessibilitydeclarations.md) response.

### Query Parameters

- `fields[accessibilityDeclarations]` ([string]): Additional fields to include for each accessibility declarations resource returned by the response.

  **Allowed Values**: `deviceFamily`, `state`, `supportsAudioDescriptions`, `supportsCaptions`, `supportsDarkInterface`, `supportsDifferentiateWithoutColorAlone`, `supportsLargerText`, `supportsReducedMotion`, `supportsSufficientContrast`, `supportsVoiceControl`, `supportsVoiceover`

## Responses

- `200` OK (`AccessibilityDeclarationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing accessibility metadata
- [List All Accessibility Declarations for an App](./get-v1-apps-_id_-accessibilitydeclarations.md)
  Get a list of the accessibility declarations for a specific app.
- [List accessibility declaration IDs for an app](./get-v1-apps-_id_-relationships-accessibilitydeclarations.md)
- [Create an Accessibility Declaration](./post-v1-accessibilitydeclarations.md)
  Add an accessibility declaration for a specific app.
- [Modify an Accessibility Declaration](./patch-v1-accessibilitydeclarations-_id_.md)
  Update the attributes of a specific accessibility declaration.
- [Delete an Accessibility Declaration](./delete-v1-accessibilitydeclarations-_id_.md)
  Delete a specific accessibility declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-accessibilitydeclarations-_id_)*