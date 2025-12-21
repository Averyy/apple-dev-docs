# previewController(_:didFinishWithActivityTypes:)

**Framework**: ReplayKit  
**Kind**: method

Indicates that the preview view controller is ready to be dismissed with associated activity types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
optional func previewController(_ previewController: RPPreviewViewController, didFinishWithActivityTypes activityTypes: Set<String>)
```

#### Discussion

When the user is finished making changes to a screen recording, your app is responsible for dismissing the view controller representing the user interface. Call [`dismiss(animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/dismiss(animated:completion:)) after getting the message to dismiss the preview view controller.

## Parameters

- `previewController`: The preview view controller to be dismissed.
- `activityTypes`: A set of activity types as listed in  .

## See Also

- [func previewControllerDidFinish(RPPreviewViewController)](rppreviewviewcontrollerdelegate/previewcontrollerdidfinish(_:).md)
  Indicates that the preview view controller is ready to be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate/previewcontroller(_:didfinishwithactivitytypes:))*