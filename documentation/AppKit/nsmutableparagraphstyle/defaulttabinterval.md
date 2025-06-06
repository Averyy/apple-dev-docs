# defaultTabInterval

**Framework**: AppKit  
**Kind**: property

A number used as the document’s default tab spacing.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var defaultTabInterval: CGFloat { get set }
```

#### Discussion

This property represents the default tab interval in points. The system places tabs after the last specified in [`tabStops`](https://developer.apple.comhttps://developer.apple.com/library/archive/#id(tabStops)) at integer multiples of this distance (if positive). Default value is `0.0`.

## See Also

- [func addTabStop(NSTextTab)](nsmutableparagraphstyle/addtabstop(_:).md)
  Adds the specified tab stop to the paragraph.
- [func removeTabStop(NSTextTab)](nsmutableparagraphstyle/removetabstop(_:).md)
  Removes the first text tab with a location and type equal to the specified tab stop.
- [var tabStops: [NSTextTab]!](nsmutableparagraphstyle/tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/defaulttabinterval)*