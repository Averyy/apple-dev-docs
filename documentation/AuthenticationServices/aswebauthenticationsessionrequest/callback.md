# callback

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The callback to listen for, which completes the request.

**Availability**:
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
var callback: ASWebAuthenticationSession.Callback? { get }
```

```objc
@property (nonatomic, readonly, nullable) ASWebAuthenticationSessionCallback * callback;
```

#### Discussion

You create a callback with the type methods [`customScheme(_:)`](../aswebauthenticationsession/callback/customscheme%28_%29.md) or [`https(host:path:)`](../aswebauthenticationsession/callback/https%28host,path%29.md).

Use this callback to check all main frame URLs that load during the request. When it matches, invoke [`complete(withCallbackURL:)`](./complete%28withcallbackurl%29.md) with that URL.

> ❗ **Important**: Your browser app needs to add [`CallbackURLMatchingIsSupported`](../../BundleResources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/callbackurlmatchingissupported.md) with the value `YES` to the [`ASWebAuthenticationSessionWebBrowserSupportCapabilities`](../../BundleResources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities.md) dictionary in your app’s information property list to use this API. If the system doesn’t find this key in the default browser app, it sends the request to Safari instead.

## See Also

### Finishing a request
- [ASWebAuthenticationSession.Callback](../aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.
- [func complete(withCallbackURL: URL)](./complete%28withcallbackurl%29.md)
  Indicates that the browser successfully completed the authentication attempt.
- [func cancelWithError(any Error)](./cancelwitherror%28_%29.md)
  Indicates that the browser canceled the authentication attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/callback)*