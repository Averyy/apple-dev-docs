# drawTitle(ofColumn:in:)

**Framework**: AppKit  
**Kind**: method

Draws the title for the specified column within the given rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawTitle(ofColumn column: Int, in rect: NSRect)
```

## Parameters

- `column`: The index of the column for which to draw the title.
- `rect`: The rectangle within which to draw the title.

## See Also

- [func title(ofColumn: Int) -> String?](nsbrowser/title(ofcolumn:).md)
  Returns the title displayed for the given column.
- [func setTitle(String, ofColumn: Int)](nsbrowser/settitle(_:ofcolumn:).md)
  Sets the title of the given column.
- [var isTitled: Bool](nsbrowser/istitled.md)
  A Boolean that indicates whether columns display titles.
- [var titleHeight: CGFloat](nsbrowser/titleheight.md)
  The height of the column titles for the browser.
- [func titleFrame(ofColumn: Int) -> NSRect](nsbrowser/titleframe(ofcolumn:).md)
  Returns the bounds of the title frame for the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/drawtitle(ofcolumn:in:))*