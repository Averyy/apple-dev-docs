# browser

**Framework**: Multipeer Connectivity  
**Kind**: property

The browser object that is used for discovering peers.

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
var browser: MCNearbyServiceBrowser? { get }
```

#### Discussion

This value is set when you initialize the object, and cannot be changed later.

## See Also

- [convenience init(serviceType: String, session: MCSession)](mcbrowserviewcontroller/init(servicetype:session:).md)
  Initializes a browser view controller using the provided service type and session.
- [init(browser: MCNearbyServiceBrowser, session: MCSession)](mcbrowserviewcontroller/init(browser:session:).md)
  Initializes a browser view controller with the provided browser and session.
- [var delegate: (any MCBrowserViewControllerDelegate)?](mcbrowserviewcontroller/delegate.md)
  The delegate object that handles browser-view-controller-related events.
- [var session: MCSession](mcbrowserviewcontroller/session.md)
  The multipeer session to which the invited peers are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/browser)*