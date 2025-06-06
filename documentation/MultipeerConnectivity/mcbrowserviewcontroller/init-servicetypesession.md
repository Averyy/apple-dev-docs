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
@MainActor
convenience init(serviceType: String, session: MCSession)
```

#### Return Value

Returns an initialized object, or `nil` if an error occurred.

#### Discussion

This method throws an exception if the `session` or `serviceType` parameters do not contain valid objects or the specified Bonjour service type is not valid.

## Parameters

- `serviceType`: For more details, read  .
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