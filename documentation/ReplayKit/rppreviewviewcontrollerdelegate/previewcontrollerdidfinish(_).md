# previewControllerDidFinish(_:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Indicates that the preview view controller is ready to be dismissed.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use SCRecordingEditor instead

## Declaration

```swift
optional func previewControllerDidFinish(_ previewController: RPPreviewViewController)
```

```objc
- (void) previewControllerDidFinish:(RPPreviewViewController *) previewController;
```

## Discussion

When the user is finished making changes to a screen recording, your app is responsible for dismissing the view controller representing the user interface. Call [`dismiss(animated:completion:)`](../../UIKit/uiviewcontroller/dismiss%28animated,completion%29.md) after getting the message to dismiss the preview view controller.

## Parameters

- `previewController`: The preview view controller to be dismissed.

## See Also

### Dismissing the View Controller
- [func previewController(RPPreviewViewController, didFinishWithActivityTypes: Set<String>)](./previewcontroller%28_,didfinishwithactivitytypes%29.md)
  Indicates that the preview view controller is ready to be dismissed with associated activity types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate/previewcontrollerdidfinish(_:))*