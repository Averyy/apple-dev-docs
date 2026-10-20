# delegate

**Framework**: Quick Look  
**Kind**: property  
**Role**: Instance Property

The preview controller’s delegate object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any QLPreviewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<QLPreviewControllerDelegate> delegate;
```

#### Discussion

The delegate determines whether to open URLs that the user taps in a preview. See [`QLPreviewControllerDelegate`](../qlpreviewcontrollerdelegate.md) to learn more.

## See Also

### Configuring a preview controller
- [var dataSource: (any QLPreviewControllerDataSource)?](./datasource.md)
  The preview controller’s data source.
- [protocol QLPreviewControllerDataSource](../qlpreviewcontrollerdatasource.md)
  The protocol that a data source for a preview controller needs to adopt to provide preview items to the controller.
- [protocol QLPreviewControllerDelegate](../qlpreviewcontrollerdelegate.md)
  The protocol that a delegate of a preview controller needs to adopt to handle Quick Look previews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/delegate)*