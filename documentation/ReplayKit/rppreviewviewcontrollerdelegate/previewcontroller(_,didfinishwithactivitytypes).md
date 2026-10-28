# previewController(_:didFinishWithActivityTypes:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Indicates that the preview view controller is ready to be dismissed with associated activity types.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use SCRecordingEditor instead

## Declaration

```swift
optional func previewController(_ previewController: RPPreviewViewController, didFinishWithActivityTypes activityTypes: Set<String>)
```

```objc
- (void) previewController:(RPPreviewViewController *) previewController didFinishWithActivityTypes:(NSSet<NSString *> *) activityTypes;
```

## Discussion

When the user is finished making changes to a screen recording, your app is responsible for dismissing the view controller representing the user interface. Call [`dismiss(animated:completion:)`](../../UIKit/uiviewcontroller/dismiss%28animated,completion%29.md) after getting the message to dismiss the preview view controller.

## Parameters

- `previewController`: The preview view controller to be dismissed.
- `activityTypes`: A set of activity types as listed in [`UIActivity`](../../UIKit/uiactivity.md).

## See Also

### Dismissing the View Controller
- [func previewControllerDidFinish(RPPreviewViewController)](./previewcontrollerdidfinish%28_%29.md)
  Indicates that the preview view controller is ready to be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate/previewcontroller(_:didfinishwithactivitytypes:))*