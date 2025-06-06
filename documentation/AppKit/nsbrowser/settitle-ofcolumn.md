# setTitle(_:ofColumn:)

**Framework**: AppKit  
**Kind**: method

Sets the title of the given column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setTitle(_ string: String, ofColumn column: Int)
```

## Parameters

- `string`: The title of the column.
- `column`: The index of the column whose title should be set.

## See Also

- [func title(ofColumn: Int) -> String?](nsbrowser/title(ofcolumn:).md)
  Returns the title displayed for the given column.
- [var isTitled: Bool](nsbrowser/istitled.md)
  A Boolean that indicates whether columns display titles.
- [func drawTitle(ofColumn: Int, in: NSRect)](nsbrowser/drawtitle(ofcolumn:in:).md)
  Draws the title for the specified column within the given rectangle.
- [var titleHeight: CGFloat](nsbrowser/titleheight.md)
  The height of the column titles for the browser.
- [func titleFrame(ofColumn: Int) -> NSRect](nsbrowser/titleframe(ofcolumn:).md)
  Returns the bounds of the title frame for the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/settitle(_:ofcolumn:))*