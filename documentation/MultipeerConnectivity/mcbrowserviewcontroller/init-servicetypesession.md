# init(serviceType:session:)

**Framework**: Multipeer Connectivity  
**Kind**: init

Initializes a browser view controller using the provided service type and session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(serviceType: String, session: MCSession)
```

#### Return Value

Returns an initialized object, or `nil` if an error occurred.

#### Discussion

This method throws an exception if the `session` or `serviceType` parameters do not contain valid objects or the specified Bonjour service type is not valid.

## Parameters

- `serviceType`: The type of service to search for. This should be a *short* text string that describes the app’s networking protocol, in the same format as a Bonjour service type (without the transport protocol) and meeting the restrictions of [`RFC 6335`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6335) (section 5.1) governing Service Name Syntax. In particular, the string: - Must be 1–15 characters long
- Can contain only ASCII lowercase letters, numbers, and hyphens
- Must contain at least one ASCII letter
- Must not begin or end with a hyphen
- Must not contain hyphens adjacent to other hyphens. This name should be easily distinguished from unrelated services. For example, a text chat app made by ABC company could use the service type `abc-txtchat`. For more details, read [`Domain Naming Conventions`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Articles/domainnames.html#//apple_ref/doc/uid/TP40002460).
- `session`: The multipeer session that any user-chosen peers should be invited to join.

## See Also

- [init(browser: MCNearbyServiceBrowser, session: MCSession)](mcbrowserviewcontroller/init(browser:session:).md)
  Initializes a browser view controller with the provided browser and session.
- [var delegate: (any MCBrowserViewControllerDelegate)?](mcbrowserviewcontroller/delegate.md)
  The delegate object that handles browser-view-controller-related events.
- [var browser: MCNearbyServiceBrowser?](mcbrowserviewcontroller/browser.md)
  The browser object that is used for discovering peers.
- [var session: MCSession](mcbrowserviewcontroller/session.md)
  The multipeer session to which the invited peers are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/init(servicetype:session:))*