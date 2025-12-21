# RPPreviewViewControllerDelegate

**Framework**: ReplayKit  
**Kind**: protocol

The protocol you implement to respond to changes to a screen-recording user interface.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol RPPreviewViewControllerDelegate : NSObjectProtocol
```

#### Overview

Use this class to respond to changes to a screen-recording user interface, represented by an [`RPBroadcastActivityViewController`](rpbroadcastactivityviewcontroller.md) object.

## Topics

### Dismissing the View Controller
- [func previewControllerDidFinish(RPPreviewViewController)](rppreviewviewcontrollerdelegate/previewcontrollerdidfinish(_:).md)
  Indicates that the preview view controller is ready to be dismissed.
- [func previewController(RPPreviewViewController, didFinishWithActivityTypes: Set<String>)](rppreviewviewcontrollerdelegate/previewcontroller(_:didfinishwithactivitytypes:).md)
  Indicates that the preview view controller is ready to be dismissed with associated activity types.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var mode: RPPreviewViewControllerMode](rppreviewviewcontroller/mode.md)
  The type of screen that appears when the view is presented.
- [enum RPPreviewViewControllerMode](rppreviewviewcontrollermode.md)
  The modes used to determine whether the preview view controller or the share screen appears when editing a replay.
- [var previewControllerDelegate: (any RPPreviewViewControllerDelegate)?](rppreviewviewcontroller/previewcontrollerdelegate.md)
  The preview view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollerdelegate)*