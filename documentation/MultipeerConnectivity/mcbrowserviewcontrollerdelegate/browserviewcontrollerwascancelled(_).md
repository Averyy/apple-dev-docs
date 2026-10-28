# browserViewControllerWasCancelled(_:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when the user cancels the browser view controller.

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
func browserViewControllerWasCancelled(_ browserViewController: MCBrowserViewController)
```

```objc
- (void) browserViewControllerWasCancelled:(MCBrowserViewController *) browserViewController;
```

## Discussion

This call is intended to inform your app that the view controller has been dismissed because the user canceled the discovery process and is no longer interested in creating a communication session.

When your app receives this delegate method call, your app must call [`dismiss(animated:completion:)`](../../UIKit/uiviewcontroller/dismiss%28animated,completion%29.md) to dismiss the view controller. Then, your app should handle the cancelation in whatever way is appropriate for your app, and then resume any UI updates that it may have temporarily suspended while the view controller was onscreen.

## Parameters

- `browserViewController`: The browser view controller that was canceled.

## See Also

### User Action Notifications
- [func browserViewControllerDidFinish(MCBrowserViewController)](./browserviewcontrollerdidfinish%28_%29.md)
  Called when the browser view controller is dismissed with peers connected in a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/browserviewcontrollerwascancelled(_:))*