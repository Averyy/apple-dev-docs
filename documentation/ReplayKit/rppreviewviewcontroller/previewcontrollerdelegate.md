# previewControllerDelegate

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

The preview view controller’s delegate.

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
weak var previewControllerDelegate: (any RPPreviewViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<RPPreviewViewControllerDelegate> previewControllerDelegate;
```

## Discussion

Before displaying the preview view controller, your app must set a delegate in order to respond to changes in the view controller. Implement the methods described in [`RPPreviewViewControllerDelegate`](../rppreviewviewcontrollerdelegate.md).

## See Also

### Displaying the Preview UI
- [var mode: RPPreviewViewControllerMode](./mode.md)
  The type of screen that appears when the view is presented.
- [enum RPPreviewViewControllerMode](../rppreviewviewcontrollermode.md)
  The modes used to determine whether the preview view controller or the share screen appears when editing a replay.
- [protocol RPPreviewViewControllerDelegate](../rppreviewviewcontrollerdelegate.md)
  The protocol you implement to respond to changes to a screen-recording user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller/previewcontrollerdelegate)*