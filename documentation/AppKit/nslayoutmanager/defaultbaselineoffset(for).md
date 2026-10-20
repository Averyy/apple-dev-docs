# defaultBaselineOffset(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func defaultBaselineOffset(for theFont: NSFont) -> CGFloat
```

```objc
- (CGFloat) defaultBaselineOffsetForFont:(NSFont *) theFont;
```

#### Return Value

The default baseline offset for a line of text drawn using `theFont`.

#### Discussion

The value returned may vary according to the layout manager’s typesetter behavior.

## Parameters

- `theFont`: The font for which to return the default baseline offset.

## See Also

### Managing the typesetter
- [var typesetter: NSTypesetter](./typesetter.md)
  The current typesetter.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](./typesetterbehavior-swift.property.md)
  The default typesetter behavior.
- [NSLayoutManager.TypesetterBehavior](./typesetterbehavior-swift.enum.md)
  Constants that determine the layout manager’s behavior during layout.
- [func defaultLineHeight(for: NSFont) -> CGFloat](./defaultlineheight%28for%29.md)
  Returns the default line height for a line of text that uses a specified font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/defaultbaselineoffset(for:))*