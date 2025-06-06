# titleHeight

**Framework**: AppKit  
**Kind**: property

The height of the column titles for the browser.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var titleHeight: CGFloat { get }
```

## See Also

- [func title(ofColumn: Int) -> String?](nsbrowser/title(ofcolumn:).md)
  Returns the title displayed for the given column.
- [func setTitle(String, ofColumn: Int)](nsbrowser/settitle(_:ofcolumn:).md)
  Sets the title of the given column.
- [var isTitled: Bool](nsbrowser/istitled.md)
  A Boolean that indicates whether columns display titles.
- [func drawTitle(ofColumn: Int, in: NSRect)](nsbrowser/drawtitle(ofcolumn:in:).md)
  Draws the title for the specified column within the given rectangle.
- [func titleFrame(ofColumn: Int) -> NSRect](nsbrowser/titleframe(ofcolumn:).md)
  Returns the bounds of the title frame for the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/titleheight)*