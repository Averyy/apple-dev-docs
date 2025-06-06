# tabStops

**Framework**: AppKit  
**Kind**: property

The text tab objects that represent the paragraph’s tab stops.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var tabStops: [NSTextTab]! { get set }
```

#### Discussion

The [`NSTextTab`](nstexttab.md) objects, sorted by location, define the tab stops for the paragraph style. The default value is an array of 12 left-aligned tabs at 28-point intervals.

## See Also

- [func addTabStop(NSTextTab)](nsmutableparagraphstyle/addtabstop(_:).md)
  Adds the specified tab stop to the paragraph.
- [func removeTabStop(NSTextTab)](nsmutableparagraphstyle/removetabstop(_:).md)
  Removes the first text tab with a location and type equal to the specified tab stop.
- [var defaultTabInterval: CGFloat](nsmutableparagraphstyle/defaulttabinterval.md)
  A number used as the document’s default tab spacing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/tabstops)*