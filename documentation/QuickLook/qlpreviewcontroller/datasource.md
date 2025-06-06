# dataSource

**Framework**: Quick Look  
**Kind**: property

The preview controller’s data source.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var dataSource: (any QLPreviewControllerDataSource)? { get set }
```

#### Discussion

To use a Quick Look preview controller, you need to implement a data source. The data source is responsible for providing items for display by the controller, and for telling it how many items to include in the preview navigation list. To learn more about implementing a data source, see [`QLPreviewControllerDataSource`](qlpreviewcontrollerdatasource.md).

## See Also

- [protocol QLPreviewControllerDataSource](qlpreviewcontrollerdatasource.md)
  The protocol that a data source for a preview controller needs to adopt to provide preview items to the controller.
- [var delegate: (any QLPreviewControllerDelegate)?](qlpreviewcontroller/delegate.md)
  The preview controller’s delegate object.
- [protocol QLPreviewControllerDelegate](qlpreviewcontrollerdelegate.md)
  The protocol that a delegate of a preview controller needs to adopt to handle Quick Look previews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/datasource)*