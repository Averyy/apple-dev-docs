# mode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The selection mode of the receiver.

**Availability**:
- macOS

## Declaration

```swift
var mode: NSMatrix.Mode { get set }
```

```objc
@property NSMatrixMode mode;
```

#### Discussion

See [`NSMatrix.Mode`](./mode-swift.enum.md) for possible values.

## See Also

### Related Documentation
- [init(frame: NSRect, mode: NSMatrix.Mode, cellClass: AnyClass?, numberOfRows: Int, numberOfColumns: Int)](./init%28frame,mode,cellclass,numberofrows,numberofcolumns%29.md)
  Initializes and returns a newly allocated matrix of the specified size using cells of the given class.
- [init(frame: NSRect, mode: NSMatrix.Mode, prototype: NSCell, numberOfRows: Int, numberOfColumns: Int)](./init%28frame,mode,prototype,numberofrows,numberofcolumns%29.md)
  Initializes and returns a newly allocated matrix of the specified size using the given cell as a prototype.
### Configuring the Matrix Object
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean that indicates whether a radio-mode matrix supports an empty selection.
- [var isSelectionByRect: Bool](./isselectionbyrect.md)
  A Boolean that indicates whether the user can select a rectangle of cells in the receiver by dragging the cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mode-swift.property)*