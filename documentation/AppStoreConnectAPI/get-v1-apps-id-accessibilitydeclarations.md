# List all accessibility declarations for an app

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

- `fields[accessibilityDeclarations]` ([string])
- `filter[deviceFamily]` ([string])
- `filter[state]` ([string])
- `limit` (integer)

## See Also

- [GET /v1/apps/{id}/relationships/accessibilityDeclarations](get-v1-apps-_id_-relationships-accessibilitydeclarations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-accessibilitydeclarations)*