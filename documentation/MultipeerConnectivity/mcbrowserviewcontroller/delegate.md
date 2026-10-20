# delegate

**Framework**: Multipeer Connectivity  
**Kind**: property  
**Role**: Instance Property

The delegate object that handles browser-view-controller-related events.

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
weak var delegate: (any MCBrowserViewControllerDelegate)? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, weak, nullable) id<MCBrowserViewControllerDelegate> delegate;
```

*macOS*

```objc
@property (atomic, weak, nullable) id<MCBrowserViewControllerDelegate> delegate;
```

#### Discussion

A browser view controller notifies the delegate:

- When the user presses the “Done” button, which is enabled when the specified minimum number of peers are connected in a session.
- When the user cancels the view controller.

Also, as new peers are discovered, the delegate can choose whether to present them in the user interface.

## See Also

### Initializing a Browser View Controller
- [convenience init(serviceType: String, session: MCSession)](./init%28servicetype,session%29.md)
  Initializes a browser view controller using the provided service type and session.
- [init(browser: MCNearbyServiceBrowser, session: MCSession)](./init%28browser,session%29.md)
  Initializes a browser view controller with the provided browser and session.
- [var browser: MCNearbyServiceBrowser?](./browser.md)
  The browser object that is used for discovering peers.
- [var session: MCSession](./session.md)
  The multipeer session to which the invited peers are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/delegate)*