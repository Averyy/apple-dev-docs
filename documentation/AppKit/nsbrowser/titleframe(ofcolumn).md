# titleFrame(ofColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the bounds of the title frame for the specified column.

**Availability**:
- macOS

## Declaration

```swift
func titleFrame(ofColumn column: Int) -> NSRect
```

```objc
- (NSRect) titleFrameOfColumn:(NSInteger) column;
```

## Return Value

The rectangle specifying the bounds of the column’s title frame.

## Parameters

- `column`: The index of the column for which to return the title frame.

## See Also

### Accessing Column Titles
- [func title(ofColumn: Int) -> String?](./title%28ofcolumn%29.md)
  Returns the title displayed for the given column.
- [func setTitle(String, ofColumn: Int)](./settitle%28_,ofcolumn%29.md)
  Sets the title of the given column.
- [var isTitled: Bool](./istitled.md)
  A Boolean that indicates whether columns display titles.
- [func drawTitle(ofColumn: Int, in: NSRect)](./drawtitle%28ofcolumn,in%29.md)
  Draws the title for the specified column within the given rectangle.
- [var titleHeight: CGFloat](./titleheight.md)
  The height of the column titles for the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/titleframe(ofcolumn:))*