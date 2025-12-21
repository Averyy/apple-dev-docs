# callback

**Framework**: Authentication Services  
**Kind**: property

The callback to listen for, which completes the request.

**Availability**:
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
var callback: ASWebAuthenticationSession.Callback? { get }
```

#### Discussion

You create a callback with the type methods [`customScheme(_:)`](aswebauthenticationsession/callback/customscheme(_:).md) or [`https(host:path:)`](aswebauthenticationsession/callback/https(host:path:).md).

Use this callback to check all main frame URLs that load during the request. When it matches, invoke [`complete(withCallbackURL:)`](aswebauthenticationsessionrequest/complete(withcallbackurl:).md) with that URL.

> ❗ **Important**: Your browser app needs to add [`CallbackURLMatchingIsSupported`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ASWebAuthenticationSessionWebBrowserSupportCapabilities/CallbackURLMatchingIsSupported) with the value `YES` to the [`ASWebAuthenticationSessionWebBrowserSupportCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ASWebAuthenticationSessionWebBrowserSupportCapabilities) dictionary in your app’s information property list to use this API. If the system doesn’t find this key in the default browser app, it sends the request to Safari instead.

## See Also

- [ASWebAuthenticationSession.Callback](aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.
- [func complete(withCallbackURL: URL)](aswebauthenticationsessionrequest/complete(withcallbackurl:).md)
  Indicates that the browser successfully completed the authentication attempt.
- [func cancelWithError(any Error)](aswebauthenticationsessionrequest/cancelwitherror(_:).md)
  Indicates that the browser canceled the authentication attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/callback)*