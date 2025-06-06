# CallbackURLMatchingIsSupported

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean that indicates whether the app can handle callbacks to match authentication URLs.

**Availability**:
- macOS 10.15+

#### Discussion

Set the corresponding value to `YES` to indicate that your browser app supports using an [`ASWebAuthenticationSession.Callback`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession/Callback) to process authentication redirect URLs.

> ❗ **Important**: If the system doesn’t find this key in the default browser app’s `Info.plist`, it sends the request to Safari instead.

If the system doesn’t find this key in the default browser app’s `Info.plist`, it sends the request to Safari instead.

## See Also

- [IsSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/issupported.md)
  A Boolean that indicates whether the app acts as a browser that supports authentication sessions.
- [EphemeralBrowserSessionIsSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/ephemeralbrowsersessionissupported.md)
  A Boolean that indicates whether the app supports ephemeral browsing when conducting authentication sessions.
- [AdditionalHeaderFieldsAreSupported](information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/additionalheaderfieldsaresupported.md)
  A Boolean that indicates whether the app supports additional header fields in requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/callbackurlmatchingissupported)*