# frame(ofRow:inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the frame of the cell at the specified location, including the expandable arrow.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func frame(ofRow row: Int, inColumn column: Int) -> NSRect
```

```objc
- (NSRect) frameOfRow:(NSInteger) row inColumn:(NSInteger) column;
```

#### Return Value

The frame of the cell, in the [`NSBrowser`](../nsbrowser.md) coordinate space.

## Parameters

- `row`: The row of the cell.
- `column`: The column of the cell.

## See Also

### Getting Row Frames
- [func getRow(UnsafeMutablePointer<Int>?, column: UnsafeMutablePointer<Int>?, for: NSPoint) -> Bool](./getrow%28_,column,for%29.md)
  Gets the row and column coordinates for the specified point, if a cell exists at that point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/frame(ofrow:incolumn:))*