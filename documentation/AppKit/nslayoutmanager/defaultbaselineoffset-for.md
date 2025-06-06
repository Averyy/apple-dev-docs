# defaultBaselineOffset(for:)

**Framework**: AppKit  
**Kind**: method

Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func defaultBaselineOffset(for theFont: NSFont) -> CGFloat
```

#### Return Value

The default baseline offset for a line of text drawn using `theFont`.

#### Discussion

The value returned may vary according to the layout manager’s typesetter behavior.

## Parameters

- `theFont`: The font for which to return the default baseline offset.

## See Also

- [var typesetter: NSTypesetter](nslayoutmanager/typesetter.md)
  The current typesetter.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](nslayoutmanager/typesetterbehavior-swift.property.md)
  The default typesetter behavior.
- [NSLayoutManager.TypesetterBehavior](nslayoutmanager/typesetterbehavior-swift.enum.md)
  Constants that determine the layout manager’s behavior during layout.
- [func defaultLineHeight(for: NSFont) -> CGFloat](nslayoutmanager/defaultlineheight(for:).md)
  Returns the default line height for a line of text that uses a specified font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/defaultbaselineoffset(for:))*