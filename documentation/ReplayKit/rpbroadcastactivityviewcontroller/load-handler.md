# load(handler:)

**Framework**: Replaykit  
**Kind**: method

Loads a broadcast activity view controller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func load(handler: @escaping (RPBroadcastActivityViewController?, (any Error)?) -> Void)
```

#### Discussion

Present the view controller using [`present(_:animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/present(_:animated:completion:)). Dismiss the view controller when the delegate’s [`broadcastActivityViewController(_:didFinishWith:error:)`](rpbroadcastactivityviewcontrollerdelegate/broadcastactivityviewcontroller(_:didfinishwith:error:).md) method is called.

> **Note**:  On the iPad, the default presentation style for view controllers is a popover. For an instance of `RPBroadcastActivityViewController` to present properly on iPad, insure the popover presentation controller’s [`sourceRect`](https://developer.apple.com/documentation/UIKit/UIPopoverPresentationController/sourceRect) and [`sourceView`](https://developer.apple.com/documentation/UIKit/UIPopoverPresentationController/sourceView) are configured.

## Parameters

- `handler`: A block that is called after the view controller is loaded.

## See Also

- [class func load(withPreferredExtension: String?, handler: (RPBroadcastActivityViewController?, (any Error)?) -> Void)](rpbroadcastactivityviewcontroller/load(withpreferredextension:handler:).md)
  Loads a broadcast activity view controller with a preferred extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/load(handler:))*