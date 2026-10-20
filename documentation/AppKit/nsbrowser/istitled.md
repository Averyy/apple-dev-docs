# isTitled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether columns display titles.

**Availability**:
- macOS

## Declaration

```swift
var isTitled: Bool { get set }
```

```objc
@property (getter=isTitled) BOOL titled;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the columns in a browser display titles.

## See Also

### Accessing Column Titles
- [func title(ofColumn: Int) -> String?](./title%28ofcolumn%29.md)
  Returns the title displayed for the given column.
- [func setTitle(String, ofColumn: Int)](./settitle%28_,ofcolumn%29.md)
  Sets the title of the given column.
- [func drawTitle(ofColumn: Int, in: NSRect)](./drawtitle%28ofcolumn,in%29.md)
  Draws the title for the specified column within the given rectangle.
- [var titleHeight: CGFloat](./titleheight.md)
  The height of the column titles for the browser.
- [func titleFrame(ofColumn: Int) -> NSRect](./titleframe%28ofcolumn%29.md)
  Returns the bounds of the title frame for the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/istitled)*