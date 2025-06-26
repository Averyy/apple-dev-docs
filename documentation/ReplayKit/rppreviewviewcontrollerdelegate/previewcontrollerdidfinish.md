# previewControllerDidFinish(_:)

**Framework**: ReplayKit  
**Kind**: method  
**Required**: Yes

Indicates that the preview view controller is ready to be dismissed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func previewControllerDidFinish(_ previewController: RPPreviewViewController)
```

#### Discussion

When the user is finished making changes to a screen recording, your app is responsible for dismissing the view controller representing the user interface. Call [`dismiss(animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/dismiss(animated:completion:)) after getting the message to dismiss the preview view controller.

## Parameters

- `previewController`: The preview view controller to be dismissed.

## See Also

- [func previewController(RPPreviewViewController, didFinishWithActivityTypes: Set<String>)](rppreviewviewcontrollerdelegate/previewcontroller(_:didfinishwithactivitytypes:).md)
  Indicates that the preview view controller is ready to be dismissed with associated activity types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate/previewcontrollerdidfinish(_:))*