# ASWebAuthenticationSession.Callback

**Framework**: Authentication Services  
**Kind**: class

An object for evaluating navigation events in an authentication session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
class Callback
```

#### Overview

When [`ASWebAuthenticationSession`](aswebauthenticationsession.md) navigates to a matching URL, it passes the URL to the session completion handler.

> ❗ **Important**: Your browser app needs to add [`CallbackURLMatchingIsSupported`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ASWebAuthenticationSessionWebBrowserSupportCapabilities/CallbackURLMatchingIsSupported) with the value `YES` to the [`ASWebAuthenticationSessionWebBrowserSupportCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ASWebAuthenticationSessionWebBrowserSupportCapabilities) dictionary in your app’s information property list to use this API. If the system doesn’t find this key in the default browser app, it sends the request to Safari instead.

## Topics

### Creating callbacks
- [class func customScheme(String) -> Self](aswebauthenticationsession/callback/customscheme(_:).md)
  Creates a callback object that matches against URLs with the given custom scheme.
- [class func https(host: String, path: String) -> Self](aswebauthenticationsession/callback/https(host:path:).md)
  Creates a callback object that matches against HTTPS URLs with the given host and path.
### Evaluating URLs
- [func matchesURL(URL) -> Bool](aswebauthenticationsession/callback/matchesurl(_:).md)
  Checks whether a given URL matches the callback object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(url: URL, callback: ASWebAuthenticationSession.Callback, completionHandler: ASWebAuthenticationSession.CompletionHandler)](aswebauthenticationsession/init(url:callback:completionhandler:).md)
  Creates a web authentication session instance that uses a callback to evaluate a redirection URL.
- [ASWebAuthenticationSession.CompletionHandler](aswebauthenticationsession/completionhandler.md)
  A completion handler for the web authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/callback)*