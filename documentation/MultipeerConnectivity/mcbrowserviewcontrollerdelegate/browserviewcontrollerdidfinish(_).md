# browserViewControllerDidFinish(_:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when the browser view controller is dismissed with peers connected in a session.

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
func browserViewControllerDidFinish(_ browserViewController: MCBrowserViewController)
```

```objc
- (void) browserViewControllerDidFinish:(MCBrowserViewController *) browserViewController;
```

#### Discussion

This call is intended to inform your app that the user has connected with nearby peers in a session and that the browser view controller has been dismissed. Upon receiving this delegate method call, your app must call [`dismiss(animated:completion:)`](../../UIKit/uiviewcontroller/dismiss%28animated,completion%29.md) to dismiss the view controller. Your app can also begin sending data to any connected peers, and should resume any UI updates that it may have temporarily suspended while the view controller was onscreen.

## Parameters

- `browserViewController`: The view controller that was dismissed.

## See Also

### User Action Notifications
- [func browserViewControllerWasCancelled(MCBrowserViewController)](./browserviewcontrollerwascancelled%28_%29.md)
  Called when the user cancels the browser view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/browserviewcontrollerdidfinish(_:))*