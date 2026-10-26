# autoresizingMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Allows the table column to resize automatically in response to resizing the table view. The resizing behavior for the table view is set using the `NSTableView` method [`columnAutoresizingStyle`](../../nstableview/columnautoresizingstyle-swift.property.md).

**Availability**:
- macOS

## Declaration

```swift
static var autoresizingMask: NSTableColumn.ResizingOptions { get }
```

```c
NSTableColumnAutoresizingMask
```

## See Also

### Constants
- [static var userResizingMask: NSTableColumn.ResizingOptions](./userresizingmask.md)
  Allows the table column to be resized by the user.
- [NSTableColumnNoResizing](../../nstablecolumnresizingoptions/nstablecolumnnoresizing.md)
  Prevents the table column from resizing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/resizingoptions/autoresizingmask)*