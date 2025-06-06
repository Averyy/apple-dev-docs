# init(browser:session:)

**Framework**: Multipeer Connectivity  
**Kind**: init

Initializes a browser view controller with the provided browser and session.

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
init(browser: MCNearbyServiceBrowser, session: MCSession)
```

#### Return Value

Returns an initialized object, or `nil` if an error occurred.

#### Discussion

This method throws an exception if the `browser` or `session` parameters do not contain valid objects.

## Parameters

- `browser`: An object that the browser view controller uses for browsing. This is usually an instance of  . However, if your app is using a custom discovery scheme, you can instead pass any custom subclass that calls the methods defined in the   protocol on its delegate when peers are found and lost.
- `session`: The multipeer session into which the invited peers are connected.

## See Also

- [convenience init(serviceType: String, session: MCSession)](mcbrowserviewcontroller/init(servicetype:session:).md)
  Initializes a browser view controller using the provided service type and session.
- [var delegate: (any MCBrowserViewControllerDelegate)?](mcbrowserviewcontroller/delegate.md)
  The delegate object that handles browser-view-controller-related events.
- [var browser: MCNearbyServiceBrowser?](mcbrowserviewcontroller/browser.md)
  The browser object that is used for discovering peers.
- [var session: MCSession](mcbrowserviewcontroller/session.md)
  The multipeer session to which the invited peers are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/init(browser:session:))*