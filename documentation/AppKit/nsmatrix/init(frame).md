# init(frame:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated matrix with the specified frame.

**Availability**:
- macOS

## Declaration

```swift
convenience init(frame frameRect: NSRect)
```

```objc
- (instancetype) initWithFrame:(NSRect) frameRect;
```

#### Return Value

The [`NSMatrix`](../nsmatrix.md), initialized with default parameters. The new [`NSMatrix`](../nsmatrix.md) contains no rows or columns. The default mode is `NSRadioModeMatrix`. The default cell class is [`NSActionCell`](../nsactioncell.md).

#### Discussion

See [`NSMatrix`](../nsmatrix.md).

## Parameters

- `frameRect`: The frame with which to initialize the matrix.

## See Also

### Initializing an NSMatrix Object
- [init(frame: NSRect, mode: NSMatrix.Mode, cellClass: AnyClass?, numberOfRows: Int, numberOfColumns: Int)](./init%28frame,mode,cellclass,numberofrows,numberofcolumns%29.md)
  Initializes and returns a newly allocated matrix of the specified size using cells of the given class.
- [init(frame: NSRect, mode: NSMatrix.Mode, prototype: NSCell, numberOfRows: Int, numberOfColumns: Int)](./init%28frame,mode,prototype,numberofrows,numberofcolumns%29.md)
  Initializes and returns a newly allocated matrix of the specified size using the given cell as a prototype.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/init(frame:))*