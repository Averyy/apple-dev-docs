# CallbackURLMatchingIsSupported

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean that indicates whether the app can handle callbacks to match authentication URLs.

**Availability**:
- macOS 10.15+

## Details

- **Name**: `CallbackURLMatchingIsSupported`
- **Type**: boolean

## Discussion

Set the corresponding value to `YES` to indicate that your browser app supports using an [`ASWebAuthenticationSession.Callback`](../../../AuthenticationServices/aswebauthenticationsession/callback.md) to process authentication redirect URLs.

> ❗ **Important**: If the system doesn’t find this key in the default browser app’s `Info.plist`, it sends the request to Safari instead.

## See Also

### Capabilities
- [IsSupported](./issupported.md)
  A Boolean that indicates whether the app acts as a browser that supports authentication sessions.
- [EphemeralBrowserSessionIsSupported](./ephemeralbrowsersessionissupported.md)
  A Boolean that indicates whether the app supports ephemeral browsing when conducting authentication sessions.
- [AdditionalHeaderFieldsAreSupported](./additionalheaderfieldsaresupported.md)
  A Boolean that indicates whether the app supports additional header fields in requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/callbackurlmatchingissupported)*