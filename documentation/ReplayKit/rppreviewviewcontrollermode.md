# RPPreviewViewControllerMode

**Framework**: ReplayKit  
**Kind**: enum

The modes used to determine whether the preview view controller or the share screen appears when editing a replay.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
enum RPPreviewViewControllerMode
```

## Topics

### Constants
- [RPPreviewViewControllerMode.preview](rppreviewviewcontrollermode/preview.md)
  Preview screen displayed when editing a replay.
- [RPPreviewViewControllerMode.share](rppreviewviewcontrollermode/share.md)
  Share/AirDrop screen displayed when editing a replay.
### Initializers
- [init?(rawValue: Int)](rppreviewviewcontrollermode/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](rppreviewviewcontrollermode/equatable-implementations.md)
- [RawRepresentable Implementations](rppreviewviewcontrollermode/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var mode: RPPreviewViewControllerMode](rppreviewviewcontroller/mode.md)
  The type of screen that appears when the view is presented.
- [var previewControllerDelegate: (any RPPreviewViewControllerDelegate)?](rppreviewviewcontroller/previewcontrollerdelegate.md)
  The preview view controller’s delegate.
- [protocol RPPreviewViewControllerDelegate](rppreviewviewcontrollerdelegate.md)
  The protocol you implement to respond to changes to a screen-recording user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rppreviewviewcontrollermode)*