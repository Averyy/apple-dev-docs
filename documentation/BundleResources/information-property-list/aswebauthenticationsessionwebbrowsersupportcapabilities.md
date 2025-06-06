# ASWebAuthenticationSessionWebBrowserSupportCapabilities

**Framework**: Bundle Resources  
**Kind**: dictionary

A collection of keys that a browser app uses to declare its ability to handle authentication requests from other apps.

**Availability**:
- macOS 10.15+

#### Discussion

Add a dictionary for this key to your app’s [`Information Property List`](information-property-list.md) if your app is a web browser and it supports web authentication. In the dictionary, include the capability keys listed below to indicate your browser app’s capabilities. For more information, see [`Supporting Single Sign-On in a Web Browser App`](https://developer.apple.com/documentation/AuthenticationServices/supporting-single-sign-on-in-a-web-browser-app).

## Topics

### Capabilities
- [IsSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/issupported.md)
  A Boolean that indicates whether the app acts as a browser that supports authentication sessions.
- [EphemeralBrowserSessionIsSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/ephemeralbrowsersessionissupported.md)
  A Boolean that indicates whether the app supports ephemeral browsing when conducting authentication sessions.
- [CallbackURLMatchingIsSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/callbackurlmatchingissupported.md)
  A Boolean that indicates whether the app can handle callbacks to match authentication URLs.
- [AdditionalHeaderFieldsAreSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/additionalheaderfieldsaresupported.md)
  A Boolean that indicates whether the app supports additional header fields in requests.

## See Also

- [ASAccountAuthenticationModificationOptOutOfSecurityPromptsOnSignIn](information-property-list/asaccountauthenticationmodificationoptoutofsecuritypromptsonsignin.md)
  A Boolean value that indicates the system shouldn’t show security recommendation prompts when users sign in using the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities)*