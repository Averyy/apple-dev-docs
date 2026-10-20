# setTitle(_:ofColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the title of the given column.

**Availability**:
- macOS

## Declaration

```swift
func setTitle(_ string: String, ofColumn column: Int)
```

```objc
- (void) setTitle:(NSString *) string ofColumn:(NSInteger) column;
```

## Parameters

- `string`: The title of the column.
- `column`: The index of the column whose title should be set.

## See Also

### Accessing Column Titles
- [func title(ofColumn: Int) -> String?](./title%28ofcolumn%29.md)
  Returns the title displayed for the given column.
- [var isTitled: Bool](./istitled.md)
  A Boolean that indicates whether columns display titles.
- [func drawTitle(ofColumn: Int, in: NSRect)](./drawtitle%28ofcolumn,in%29.md)
  Draws the title for the specified column within the given rectangle.
- [var titleHeight: CGFloat](./titleheight.md)
  The height of the column titles for the browser.
- [func titleFrame(ofColumn: Int) -> NSRect](./titleframe%28ofcolumn%29.md)
  Returns the bounds of the title frame for the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/settitle(_:ofcolumn:))*