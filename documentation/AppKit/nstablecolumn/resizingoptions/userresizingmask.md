# userResizingMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Allows the table column to be resized by the user.

**Availability**:
- macOS

## Declaration

```swift
static var userResizingMask: NSTableColumn.ResizingOptions { get }
```

```c
NSTableColumnUserResizingMask
```

## See Also

### Constants
- [static var autoresizingMask: NSTableColumn.ResizingOptions](./autoresizingmask.md)
  Allows the table column to resize automatically in response to resizing the table view. The resizing behavior for the table view is set using the `NSTableView` method [`columnAutoresizingStyle`](../../nstableview/columnautoresizingstyle-swift.property.md).
- [NSTableColumnNoResizing](../../nstablecolumnresizingoptions/nstablecolumnnoresizing.md)
  Prevents the table column from resizing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/resizingoptions/userresizingmask)*