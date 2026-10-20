# ASWebAuthenticationSession.Callback

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASWebAuthenticationSessionCallback : NSObject
```

#### Overview

When [`ASWebAuthenticationSession`](../aswebauthenticationsession.md) navigates to a matching URL, it passes the URL to the session completion handler.

> ❗ **Important**: Your browser app needs to add [`CallbackURLMatchingIsSupported`](../../BundleResources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities/callbackurlmatchingissupported.md) with the value `YES` to the [`ASWebAuthenticationSessionWebBrowserSupportCapabilities`](../../BundleResources/information-property-list/aswebauthenticationsessionwebbrowsersupportcapabilities.md) dictionary in your app’s information property list to use this API. If the system doesn’t find this key in the default browser app, it sends the request to Safari instead.

## Topics

### Creating callbacks
- [class func customScheme(String) -> Self](./callback/customscheme%28_%29.md)
  Creates a callback object that matches against URLs with the given custom scheme.
- [class func https(host: String, path: String) -> Self](./callback/https%28host,path%29.md)
  Creates a callback object that matches against HTTPS URLs with the given host and path.
### Evaluating URLs
- [func matchesURL(URL) -> Bool](./callback/matchesurl%28_%29.md)
  Checks whether a given URL matches the callback object.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a session
- [init(url: URL, callback: ASWebAuthenticationSession.Callback, completionHandler: ASWebAuthenticationSession.CompletionHandler)](./init%28url,callback,completionhandler%29-6nut7.md)
  Creates a web authentication session instance that uses a callback to evaluate a redirection URL.
- [ASWebAuthenticationSession.CompletionHandler](./completionhandler.md)
  A completion handler for the web authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/callback)*