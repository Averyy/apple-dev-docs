# defaultTabInterval

**Framework**: AppKit  
**Kind**: property

The documentwide default tab interval.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var defaultTabInterval: CGFloat { get }
```

#### Discussion

This property represents the default tab interval in points. Tabs after the last specified in [`tabStops`](nsparagraphstyle/tabstops.md) are placed at integer multiples of this distance (if positive). Default value is 0.0.

## See Also

- [var tabStops: [NSTextTab]](nsparagraphstyle/tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [NSParagraphStyle.TextTabType](nsparagraphstyle/texttabtype.md)
  Constants that specify the type of tab stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/defaulttabinterval)*