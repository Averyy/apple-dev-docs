# EphemeralBrowserSessionIsSupported

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean that indicates whether the app supports ephemeral browsing when conducting authentication sessions.

**Availability**:
- macOS 10.15+

## Details

- **Name**: `EphemeralBrowserSessionIsSupported` (Ephemeral Browser Session Is Supported)
- **Type**: boolean

#### Discussion

Set the corresponding value to `YES` to indicate that your browser app, when handling authentication requests, offers ephemeral browsing.

If you don’t provide the key, or if you set its value to `NO` and an app tries to conduct an ephemeral authentication session, the system warns the user. If do you declare support by setting the value to `YES`, be sure to respect the [`shouldUseEphemeralSession`](../../../AuthenticationServices/aswebauthenticationsessionrequest/shoulduseephemeralsession.md) property on any incoming authentication requests, as described in [Supporting Single Sign-On in a Web Browser App](../../../AuthenticationServices/supporting-single-sign-on-in-a-web-browser-app.md).

> **Note**:  It’s strongly recommended that your web browser support ephemeral sessions. Apps can specifically request this kind of session, and it’s important to honor the request.

## See Also

### Capabilities
- [IsSupported](./issupported.md)
  A Boolean that indicates whether the app acts as a browser that supports authentication sessions.
- [CallbackURLMatchingIsSupported](./callbackurlmatchingissupported.md)
  A Boolean that indicates whether the app can handle callbacks to match authentication URLs.
- [AdditionalHeaderFieldsAreSupported](./additionalheaderfieldsaresupported.md)
  A Boolean that indicates whether the app supports additional header fields in requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/ephemeralbrowsersessionissupported)*