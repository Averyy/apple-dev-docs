# tabStops

**Framework**: AppKit  
**Kind**: property

The text tab objects that represent the paragraph’s tab stops.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var tabStops: [NSTextTab] { get }
```

#### Discussion

The [`NSTextTab`](nstexttab.md) objects, sorted by location, define the tab stops for the paragraph style. The default value is an array of 12 left-aligned tabs at 28-point intervals.

## See Also

- [var defaultTabInterval: CGFloat](nsparagraphstyle/defaulttabinterval.md)
  The documentwide default tab interval.
- [NSParagraphStyle.TextTabType](nsparagraphstyle/texttabtype.md)
  Constants that specify the type of tab stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/tabstops)*