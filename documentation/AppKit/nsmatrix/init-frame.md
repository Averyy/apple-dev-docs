# init(frame:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated matrix with the specified frame.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
convenience init(frame frameRect: NSRect)
```

#### Return Value

The [`NSMatrix`](nsmatrix.md), initialized with default parameters. The new [`NSMatrix`](nsmatrix.md) contains no rows or columns. The default mode is `NSRadioModeMatrix`. The default cell class is [`NSActionCell`](nsactioncell.md).

#### Discussion

.

## Parameters

- `frameRect`: The frame with which to initialize the matrix.

## See Also

- [Matrix Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Matrix/Matrix.html#//apple_ref/doc/uid/10000022i)
- [init(frame: NSRect, mode: NSMatrix.Mode, cellClass: AnyClass?, numberOfRows: Int, numberOfColumns: Int)](nsmatrix/init(frame:mode:cellclass:numberofrows:numberofcolumns:).md)
  Initializes and returns a newly allocated matrix of the specified size using cells of the given class.
- [init(frame: NSRect, mode: NSMatrix.Mode, prototype: NSCell, numberOfRows: Int, numberOfColumns: Int)](nsmatrix/init(frame:mode:prototype:numberofrows:numberofcolumns:).md)
  Initializes and returns a newly allocated matrix of the specified size using the given cell as a prototype.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/init(frame:))*