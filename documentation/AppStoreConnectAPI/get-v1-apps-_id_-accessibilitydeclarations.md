# List All Accessibility Declarations for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of the accessibility declarations for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring accessibility declarations for your app](./configuring-accessibility-declarations.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/accessibilityDeclarations`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[accessibilityDeclarations]` ([string]): Additional fields to include for each accessibility declarations resource returned by the response.

  **Allowed Values**: `deviceFamily`, `state`, `supportsAudioDescriptions`, `supportsCaptions`, `supportsDarkInterface`, `supportsDifferentiateWithoutColorAlone`, `supportsLargerText`, `supportsReducedMotion`, `supportsSufficientContrast`, `supportsVoiceControl`, `supportsVoiceover`
- `filter[deviceFamily]` ([string]): Filter the returned accessibility declarations by device family.

  **Allowed Values**: `IPHONE`, `IPAD`, `APPLE_TV`, `APPLE_WATCH`, `MAC`, `VISION`
- `filter[state]` ([string]): Filter the returned accessibility declarations by state.

  **Allowed Values**: `DRAFT`, `PUBLISHED`, `REPLACED`
- `limit` (integer): The maximum number of accessibility declarations resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AccessibilityDeclarationsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting accessibility declaration information
- [List accessibility declaration IDs for an app](./get-v1-apps-_id_-relationships-accessibilitydeclarations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-accessibilitydeclarations)*