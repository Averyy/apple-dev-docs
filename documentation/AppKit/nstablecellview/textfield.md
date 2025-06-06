# textField

**Framework**: AppKit  
**Kind**: property

Text displayed by the cell.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
@MainActor unowned(unsafe) var textField: NSTextField? { get set }
```

#### Discussion

This property is typically configured when the row is created in the [`NSTableViewDelegate`](nstableviewdelegate.md) protocol method [`tableView(_:viewFor:row:)`](nstableviewdelegate/tableview(_:viewfor:row:).md).

## See Also

- [var imageView: NSImageView?](nstablecellview/imageview.md)
  Image displayed by the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecellview/textfield)*