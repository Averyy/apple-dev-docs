# imageView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Image displayed by the cell.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
unowned(unsafe) var imageView: NSImageView? { get set }
```

```objc
@property (assign, nullable) NSImageView * imageView;
```

## Discussion

This property is typically configured when the row is created in the [`NSTableViewDataSource`](../nstableviewdatasource.md) protocol method [`tableView(_:viewFor:row:)`](../nstableviewdelegate/tableview%28_,viewfor,row%29.md).

## See Also

### Displayed Items
- [var textField: NSTextField?](./textfield.md)
  Text displayed by the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecellview/imageview)*