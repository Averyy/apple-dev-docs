# browserViewControllerDidFinish(_:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Required**: Yes

Called when the browser view controller is dismissed with peers connected in a session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func browserViewControllerDidFinish(_ browserViewController: MCBrowserViewController)
```

#### Discussion

This call is intended to inform your app that the user has connected with nearby peers in a session and that the browser view controller has been dismissed. Upon receiving this delegate method call, your app must call [`dismiss(animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/dismiss(animated:completion:)) to dismiss the view controller. Your app can also begin sending data to any connected peers, and should resume any UI updates that it may have temporarily suspended while the view controller was onscreen.

## Parameters

- `browserViewController`: The view controller that was dismissed.

## See Also

- [func browserViewControllerWasCancelled(MCBrowserViewController)](mcbrowserviewcontrollerdelegate/browserviewcontrollerwascancelled(_:).md)
  Called when the user cancels the browser view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/browserviewcontrollerdidfinish(_:))*