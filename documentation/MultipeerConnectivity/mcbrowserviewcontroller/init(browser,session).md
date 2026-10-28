# init(browser:session:)

**Framework**: Multipeer Connectivity  
**Kind**: init  
**Role**: Initializer

Initializes a browser view controller with the provided browser and session.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
init(browser: MCNearbyServiceBrowser, session: MCSession)
```

```objc
- (instancetype) initWithBrowser:(MCNearbyServiceBrowser *) browser session:(MCSession *) session;
```

## Return Value

Returns an initialized object, or `nil` if an error occurred.

## Discussion

This method throws an exception if the `browser` or `session` parameters do not contain valid objects.

## Parameters

- `browser`: An object that the browser view controller uses for browsing. This is usually an instance of `MCNearbyServiceBrowser`. However, if your app is using a custom discovery scheme, you can instead pass any custom subclass that calls the methods defined in the [`MCNearbyServiceBrowserDelegate`](../mcnearbyservicebrowserdelegate.md) protocol on its delegate when peers are found and lost.

  > ❗ **Important**:  If you want the browser view controller to manage the browsing process, the browser object must not be actively browsing, and its delegate must be `nil`.
- `session`: The multipeer session into which the invited peers are connected.

## See Also

### Initializing a Browser View Controller
- [convenience init(serviceType: String, session: MCSession)](./init%28servicetype,session%29.md)
  Initializes a browser view controller using the provided service type and session.
- [var delegate: (any MCBrowserViewControllerDelegate)?](./delegate.md)
  The delegate object that handles browser-view-controller-related events.
- [var browser: MCNearbyServiceBrowser?](./browser.md)
  The browser object that is used for discovering peers.
- [var session: MCSession](./session.md)
  The multipeer session to which the invited peers are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/init(browser:session:))*