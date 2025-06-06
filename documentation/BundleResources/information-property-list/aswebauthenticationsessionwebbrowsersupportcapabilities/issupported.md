# IsSupported

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean that indicates whether the app acts as a browser that supports authentication sessions.

**Availability**:
- macOS 10.15+

#### Discussion

Set the corresponding value to `YES` to indicate that your browser app can handle authentication requests that other apps generate with [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession). For details, see [`Supporting Single Sign-On in a Web Browser App`](https://developer.apple.com/documentation/AuthenticationServices/supporting-single-sign-on-in-a-web-browser-app).

## See Also

- [EphemeralBrowserSessionIsSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/ephemeralbrowsersessionissupported.md)
  A Boolean that indicates whether the app supports ephemeral browsing when conducting authentication sessions.
- [CallbackURLMatchingIsSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/callbackurlmatchingissupported.md)
  A Boolean that indicates whether the app can handle callbacks to match authentication URLs.
- [AdditionalHeaderFieldsAreSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/additionalheaderfieldsaresupported.md)
  A Boolean that indicates whether the app supports additional header fields in requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/issupported)*