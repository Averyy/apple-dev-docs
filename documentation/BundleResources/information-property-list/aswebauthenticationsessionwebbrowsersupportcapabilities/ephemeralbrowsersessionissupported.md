# EphemeralBrowserSessionIsSupported

**Framework**: Bundleresources  
**Kind**: typealias

A Boolean that indicates whether the app supports ephemeral browsing when conducting authentication sessions.

**Availability**:
- macOS 10.15+

#### Discussion

Set the corresponding value to `YES` to indicate that your browser app, when handling authentication requests, offers ephemeral browsing.

If you don’t provide the key, or if you set its value to `NO` and an app tries to conduct an ephemeral authentication session, the system warns the user. If do you declare support by setting the value to `YES`, be sure to respect the [`shouldUseEphemeralSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSessionRequest/shouldUseEphemeralSession) property on any incoming authentication requests, as described in [`Supporting Single Sign-On in a Web Browser App`](https://developer.apple.com/documentation/AuthenticationServices/supporting-single-sign-on-in-a-web-browser-app).

> **Note**:  It’s strongly recommended that your web browser support ephemeral sessions. Apps can specifically request this kind of session, and it’s important to honor the request.

## See Also

- [IsSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/issupported.md)
  A Boolean that indicates whether the app acts as a browser that supports authentication sessions.
- [CallbackURLMatchingIsSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/callbackurlmatchingissupported.md)
  A Boolean that indicates whether the app can handle callbacks to match authentication URLs.
- [AdditionalHeaderFieldsAreSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/additionalheaderfieldsaresupported.md)
  A Boolean that indicates whether the app supports additional header fields in requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/ephemeralbrowsersessionissupported)*