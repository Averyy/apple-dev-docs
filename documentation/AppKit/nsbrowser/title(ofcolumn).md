# title(ofColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the title displayed for the given column.

**Availability**:
- macOS

## Declaration

```swift
func title(ofColumn column: Int) -> String?
```

```objc
- (NSString *) titleOfColumn:(NSInteger) column;
```

## Return Value

The title of the specified column.

## Parameters

- `column`: The index of the column for which to get the title.

## See Also

### Accessing Column Titles
- [func setTitle(String, ofColumn: Int)](./settitle%28_,ofcolumn%29.md)
  Sets the title of the given column.
- [var isTitled: Bool](./istitled.md)
  A Boolean that indicates whether columns display titles.
- [func drawTitle(ofColumn: Int, in: NSRect)](./drawtitle%28ofcolumn,in%29.md)
  Draws the title for the specified column within the given rectangle.
- [var titleHeight: CGFloat](./titleheight.md)
  The height of the column titles for the browser.
- [func titleFrame(ofColumn: Int) -> NSRect](./titleframe%28ofcolumn%29.md)
  Returns the bounds of the title frame for the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/title(ofcolumn:))*