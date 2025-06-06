# title(ofColumn:)

**Framework**: AppKit  
**Kind**: method

Returns the title displayed for the given column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func title(ofColumn column: Int) -> String?
```

#### Return Value

The title of the specified column.

## Parameters

- `column`: The index of the column for which to get the title.

## See Also

- [func setTitle(String, ofColumn: Int)](nsbrowser/settitle(_:ofcolumn:).md)
  Sets the title of the given column.
- [var isTitled: Bool](nsbrowser/istitled.md)
  A Boolean that indicates whether columns display titles.
- [func drawTitle(ofColumn: Int, in: NSRect)](nsbrowser/drawtitle(ofcolumn:in:).md)
  Draws the title for the specified column within the given rectangle.
- [var titleHeight: CGFloat](nsbrowser/titleheight.md)
  The height of the column titles for the browser.
- [func titleFrame(ofColumn: Int) -> NSRect](nsbrowser/titleframe(ofcolumn:).md)
  Returns the bounds of the title frame for the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/title(ofcolumn:))*