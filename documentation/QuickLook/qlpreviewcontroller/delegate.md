# delegate

**Framework**: Quick Look  
**Kind**: property

The preview controller’s delegate object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any QLPreviewControllerDelegate)? { get set }
```

#### Discussion

The delegate determines whether to open URLs that the user taps in a preview. See [`QLPreviewControllerDelegate`](qlpreviewcontrollerdelegate.md) to learn more.

## See Also

- [var dataSource: (any QLPreviewControllerDataSource)?](qlpreviewcontroller/datasource.md)
  The preview controller’s data source.
- [protocol QLPreviewControllerDataSource](qlpreviewcontrollerdatasource.md)
  The protocol that a data source for a preview controller needs to adopt to provide preview items to the controller.
- [protocol QLPreviewControllerDelegate](qlpreviewcontrollerdelegate.md)
  The protocol that a delegate of a preview controller needs to adopt to handle Quick Look previews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/delegate)*