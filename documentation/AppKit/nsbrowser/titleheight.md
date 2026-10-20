# titleHeight

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The height of the column titles for the browser.

**Availability**:
- macOS

## Declaration

```swift
var titleHeight: CGFloat { get }
```

```objc
@property (readonly) CGFloat titleHeight;
```

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
- [func titleFrame(ofColumn: Int) -> NSRect](./titleframe%28ofcolumn%29.md)
  Returns the bounds of the title frame for the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/titleheight)*