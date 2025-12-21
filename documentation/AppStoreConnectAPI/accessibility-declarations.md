# Accessibility declarations

**Framework**: App Store Connect API

Manage accessibility metadata for your apps per device family.

#### Overview

There are five modalities for accessibility: Vision, Hearing, Speech, Mobility, and Cognitive. Apple operating systems provide opportunities to deliver high-quality experiences to everyone, including people with disabilities. To learn more  about all the features developers can leverage in their apps to support users with disabilities, see [`Building accessible apps`](https://developer.apple.comhttps://developer.apple.com/accessibility/).

Accessibility declarations enable you to show the accessibility modalities and the specific features your app supports. Use this resource to create and configure accessibility declarations for your apps. Once you create an accessibility declaration, your App Store page shows the accessibility details for your app. You make accessibility declarations for each app and they apply to a device family, to learn more, see [`DeviceFamily`](devicefamily.md).

> **Note**: The default value for each attribute in an accessibility declaration is `false`. If you modify a subset of the available attributes, the remaining attributes default to `false`.

To add an accessibility URL to your the App Store page for your app, use [`Modify an App`](patch-v1-apps-_id_.md) and update the the `accessibilityUrl` attribute.

To manage accessibility declarations, be sure you have one of the following user roles:

- `ADMIN`
- `APP MANAGER`
- `MARKETING`

Both Team and Individual API keys can use these endpoints with the correct role.

## Topics

### Essentials
- [Configuring accessibility declarations for your app](configuring-accessibility-declarations.md)
  Manage accessibility metadata for your apps per device family.
### Managing accessibility metadata
- [List all accessibility declarations for an app](get-v1-apps-_id_-accessibilitydeclarations.md)
  Get a list of the accessibility declarations for a specific app.
- [GET /v1/apps/{id}/relationships/accessibilityDeclarations](get-v1-apps-_id_-relationships-accessibilitydeclarations.md)
- [Read accessibility declaration information](get-v1-accessibilitydeclarations-_id_.md)
  Get information about a specific accessibility declaration.
- [Create an accessibility declaration](post-v1-accessibilitydeclarations.md)
  Add an accessibility declaration for a specific app.
- [Modify an accessibility declaration](patch-v1-accessibilitydeclarations-_id_.md)
  Update the attributes of a specific accessibility declaration.
- [Delete an accessibility declaration](delete-v1-accessibilitydeclarations-_id_.md)
  Delete a specific accessibility declaration.
### Objects
- [object AccessibilityDeclaration](accessibilitydeclaration.md)
  The data structure that represents an accessibility declarations resource.
- [object AccessibilityDeclarationsResponse](accessibilitydeclarationsresponse.md)
  A response that contains a list of accessibility declaration resources.
- [object AccessibilityDeclarationCreateRequest](accessibilitydeclarationcreaterequest.md)
  The request body you use to create an accessibility declaration for an app.
- [object AccessibilityDeclarationResponse](accessibilitydeclarationresponse.md)
  A response that contains a single accessibility declaration resource.
- [object AccessibilityDeclarationUpdateRequest](accessibilitydeclarationupdaterequest.md)
  The request body you use to update an accessibility declaration for an app.
- [object AppAccessibilityDeclarationsLinkagesResponse](appaccessibilitydeclarationslinkagesresponse.md)
- [type DeviceFamily](devicefamily.md)
  String that represents a device family.

## See Also

- [App Infos](app-infos.md)
  Manage or read the app metadata that applies across all versions of your app.
- [App Info Localizations](app-info-localizations.md)
  Manage the app metadata that is localized and appears on the App Store.
- [App Store Versions](app-store-versions.md)
  Manage versions of your app that are available in App Store.
- [App Store Version Localizations](app-store-version-localizations.md)
  Create and maintain version-specific App Store metadata that’s localized.
- [App tags](app-tags.md)
  Read or modify Apple created app tags.
- [Routing App Coverages](routing-app-coverages.md)
  Manage geographic coverage files for apps that use location to provide routing information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/accessibility-declarations)*