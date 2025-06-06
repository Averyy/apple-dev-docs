# QLPreviewControllerDataSource

**Framework**: Quick Look  
**Kind**: protocol

The protocol that a data source for a preview controller needs to adopt to provide preview items to the controller.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol QLPreviewControllerDataSource
```

#### Overview

Besides providing a [`QLPreviewController`](qlpreviewcontroller.md) with items to preview, this protocol is responsible for telling the preview controller how many items it needs to include in a preview item navigation list.

## Topics

### Providing data to a preview controller
- [func numberOfPreviewItems(in: QLPreviewController) -> Int](qlpreviewcontrollerdatasource/numberofpreviewitems(in:).md)
  Returns the number of preview items to include in the preview navigation list.
- [func previewController(QLPreviewController, previewItemAt: Int) -> any QLPreviewItem](qlpreviewcontrollerdatasource/previewcontroller(_:previewitemat:).md)
  Returns the preview item that the controller displays for the specified index.

## See Also

- [var dataSource: (any QLPreviewControllerDataSource)?](qlpreviewcontroller/datasource.md)
  The preview controller’s data source.
- [var delegate: (any QLPreviewControllerDelegate)?](qlpreviewcontroller/delegate.md)
  The preview controller’s delegate object.
- [protocol QLPreviewControllerDelegate](qlpreviewcontrollerdelegate.md)
  The protocol that a delegate of a preview controller needs to adopt to handle Quick Look previews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdatasource)*