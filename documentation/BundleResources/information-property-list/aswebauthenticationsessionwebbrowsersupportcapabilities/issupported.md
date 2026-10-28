# IsSupported

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean that indicates whether the app acts as a browser that supports authentication sessions.

**Availability**:
- macOS 10.15+

## Details

- **Name**: `IsSupported`
- **Type**: boolean

## Discussion

Set the corresponding value to `YES` to indicate that your browser app can handle authentication requests that other apps generate with [`ASWebAuthenticationSession`](../../../AuthenticationServices/aswebauthenticationsession.md). For details, see [Supporting Single Sign-On in a Web Browser App](../../../AuthenticationServices/supporting-single-sign-on-in-a-web-browser-app.md).

## See Also

### Capabilities
- [EphemeralBrowserSessionIsSupported](./ephemeralbrowsersessionissupported.md)
  A Boolean that indicates whether the app supports ephemeral browsing when conducting authentication sessions.
- [CallbackURLMatchingIsSupported](./callbackurlmatchingissupported.md)
  A Boolean that indicates whether the app can handle callbacks to match authentication URLs.
- [AdditionalHeaderFieldsAreSupported](./additionalheaderfieldsaresupported.md)
  A Boolean that indicates whether the app supports additional header fields in requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/issupported)*