# isTitled

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether columns display titles.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isTitled: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the columns in a browser display titles.

## See Also

- [func title(ofColumn: Int) -> String?](nsbrowser/title(ofcolumn:).md)
  Returns the title displayed for the given column.
- [func setTitle(String, ofColumn: Int)](nsbrowser/settitle(_:ofcolumn:).md)
  Sets the title of the given column.
- [func drawTitle(ofColumn: Int, in: NSRect)](nsbrowser/drawtitle(ofcolumn:in:).md)
  Draws the title for the specified column within the given rectangle.
- [var titleHeight: CGFloat](nsbrowser/titleheight.md)
  The height of the column titles for the browser.
- [func titleFrame(ofColumn: Int) -> NSRect](nsbrowser/titleframe(ofcolumn:).md)
  Returns the bounds of the title frame for the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/istitled)*