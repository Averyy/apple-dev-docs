# previewControllerDelegate

**Framework**: ReplayKit  
**Kind**: property

The preview view controller’s delegate.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
weak var previewControllerDelegate: (any RPPreviewViewControllerDelegate)? { get set }
```

#### Discussion

Before displaying the preview view controller, your app must set a delegate in order to respond to changes in the view controller. Implement the methods described in [`RPPreviewViewControllerDelegate`](rppreviewviewcontrollerdelegate.md).

## See Also

- [var mode: RPPreviewViewControllerMode](rppreviewviewcontroller/mode.md)
  The type of screen that appears when the view is presented.
- [enum RPPreviewViewControllerMode](rppreviewviewcontrollermode.md)
  The modes used to determine whether the preview view controller or the share screen appears when editing a replay.
- [protocol RPPreviewViewControllerDelegate](rppreviewviewcontrollerdelegate.md)
  The protocol you implement to respond to changes to a screen-recording user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller/previewcontrollerdelegate)*