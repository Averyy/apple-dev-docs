# browser

**Framework**: Multipeer Connectivity  
**Kind**: property  
**Role**: Instance Property

The browser object that is used for discovering peers.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var browser: MCNearbyServiceBrowser? { get }
```

*macOS*

```swift
var browser: MCNearbyServiceBrowser { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly, nullable) MCNearbyServiceBrowser * browser;
```

*macOS*

```objc
@property (atomic, readonly) MCNearbyServiceBrowser * browser;
```

#### Discussion

This value is set when you initialize the object, and cannot be changed later.

## See Also

### Initializing a Browser View Controller
- [convenience init(serviceType: String, session: MCSession)](./init%28servicetype,session%29.md)
  Initializes a browser view controller using the provided service type and session.
- [init(browser: MCNearbyServiceBrowser, session: MCSession)](./init%28browser,session%29.md)
  Initializes a browser view controller with the provided browser and session.
- [var delegate: (any MCBrowserViewControllerDelegate)?](./delegate.md)
  The delegate object that handles browser-view-controller-related events.
- [var session: MCSession](./session.md)
  The multipeer session to which the invited peers are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/browser)*