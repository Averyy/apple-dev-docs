# List All Accessibility Declarations for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of the accessibility declarations for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring accessibility declarations for your app](configuring-accessibility-declarations.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/accessibilityDeclarations`

## Parameters

- `fields[accessibilityDeclarations]` ([string]): Additional fields to include for each accessibility declarations resource returned by the response.
- `filter[deviceFamily]` ([string]): Filter the returned accessibility declarations by device family.
- `filter[state]` ([string]): Filter the returned accessibility declarations by state.
- `limit` (integer): The maximum number of accessibility declarations resources to return.

## See Also

- [List accessibility declaration IDs for an app](get-v1-apps-_id_-relationships-accessibilitydeclarations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-accessibilitydeclarations)*