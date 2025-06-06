# tabStops

**Framework**: UIKit  
**Kind**: property

The text tab objects that represent the paragraph’s tab stops.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var tabStops: [NSTextTab] { get }
```

#### Discussion

The [`NSTextTab`](nstexttab.md) objects, sorted by location, define the tab stops for the paragraph style. The default value is an array of 12 left-aligned tabs at 28-point intervals.

## See Also

- [NSParagraphStyle.TextTabType](../AppKit/NSParagraphStyle/TextTabType.md)
  Constants that specify the type of tab stop.
- [var defaultTabInterval: CGFloat](nsparagraphstyle/defaulttabinterval.md)
  The documentwide default tab interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsparagraphstyle/tabstops)*