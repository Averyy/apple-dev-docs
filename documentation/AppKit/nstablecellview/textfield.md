# textField

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Text displayed by the cell.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
unowned(unsafe) var textField: NSTextField? { get set }
```

```objc
@property (assign, nullable) NSTextField * textField;
```

#### Discussion

This property is typically configured when the row is created in the [`NSTableViewDelegate`](../nstableviewdelegate.md) protocol method [`tableView(_:viewFor:row:)`](../nstableviewdelegate/tableview%28_,viewfor,row%29.md).

## See Also

### Displayed Items
- [var imageView: NSImageView?](./imageview.md)
  Image displayed by the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecellview/textfield)*