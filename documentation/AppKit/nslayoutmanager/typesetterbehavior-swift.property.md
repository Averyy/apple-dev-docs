# typesetterBehavior

**Framework**: AppKit  
**Kind**: property

The default typesetter behavior.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var typesetterBehavior: NSLayoutManager.TypesetterBehavior { get set }
```

#### Discussion

The typesetter behavior affects glyph spacing and line height.

## See Also

- [var typesetter: NSTypesetter](nslayoutmanager/typesetter.md)
  The current typesetter.
- [NSLayoutManager.TypesetterBehavior](nslayoutmanager/typesetterbehavior-swift.enum.md)
  Constants that determine the layout manager’s behavior during layout.
- [func defaultLineHeight(for: NSFont) -> CGFloat](nslayoutmanager/defaultlineheight(for:).md)
  Returns the default line height for a line of text that uses a specified font.
- [func defaultBaselineOffset(for: NSFont) -> CGFloat](nslayoutmanager/defaultbaselineoffset(for:).md)
  Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/typesetterbehavior-swift.property)*