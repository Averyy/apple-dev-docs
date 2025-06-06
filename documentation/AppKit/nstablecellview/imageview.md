# imageView

**Framework**: AppKit  
**Kind**: property

Image displayed by the cell.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
@MainActor unowned(unsafe) var imageView: NSImageView? { get set }
```

#### Discussion

This property is typically configured when the row is created in the [`NSTableViewDataSource`](nstableviewdatasource.md) protocol method [`tableView(_:viewFor:row:)`](nstableviewdelegate/tableview(_:viewfor:row:).md).

## See Also

- [var textField: NSTextField?](nstablecellview/textfield.md)
  Text displayed by the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecellview/imageview)*