# drawTitle(ofColumn:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the title for the specified column within the given rectangle.

**Availability**:
- macOS

## Declaration

```swift
func drawTitle(ofColumn column: Int, in rect: NSRect)
```

```objc
- (void) drawTitleOfColumn:(NSInteger) column inRect:(NSRect) rect;
```

## Parameters

- `column`: The index of the column for which to draw the title.
- `rect`: The rectangle within which to draw the title.

## See Also

### Accessing Column Titles
- [func title(ofColumn: Int) -> String?](./title%28ofcolumn%29.md)
  Returns the title displayed for the given column.
- [func setTitle(String, ofColumn: Int)](./settitle%28_,ofcolumn%29.md)
  Sets the title of the given column.
- [var isTitled: Bool](./istitled.md)
  A Boolean that indicates whether columns display titles.
- [var titleHeight: CGFloat](./titleheight.md)
  The height of the column titles for the browser.
- [func titleFrame(ofColumn: Int) -> NSRect](./titleframe%28ofcolumn%29.md)
  Returns the bounds of the title frame for the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/drawtitle(ofcolumn:in:))*