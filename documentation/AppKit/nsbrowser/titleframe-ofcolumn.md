# titleFrame(ofColumn:)

**Framework**: AppKit  
**Kind**: method

Returns the bounds of the title frame for the specified column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func titleFrame(ofColumn column: Int) -> NSRect
```

#### Return Value

The rectangle specifying the bounds of the column’s title frame.

## Parameters

- `column`: The index of the column for which to return the title frame.

## See Also

- [func title(ofColumn: Int) -> String?](nsbrowser/title(ofcolumn:).md)
  Returns the title displayed for the given column.
- [func setTitle(String, ofColumn: Int)](nsbrowser/settitle(_:ofcolumn:).md)
  Sets the title of the given column.
- [var isTitled: Bool](nsbrowser/istitled.md)
  A Boolean that indicates whether columns display titles.
- [func drawTitle(ofColumn: Int, in: NSRect)](nsbrowser/drawtitle(ofcolumn:in:).md)
  Draws the title for the specified column within the given rectangle.
- [var titleHeight: CGFloat](nsbrowser/titleheight.md)
  The height of the column titles for the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/titleframe(ofcolumn:))*