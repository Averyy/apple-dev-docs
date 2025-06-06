# defaultTabInterval

**Framework**: UIKit  
**Kind**: property

The documentwide default tab interval.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var defaultTabInterval: CGFloat { get }
```

#### Discussion

This property represents the default tab interval in points. Tabs after the last specified in [`tabStops`](nsparagraphstyle/tabstops.md) are placed at integer multiples of this distance (if positive). Default value is 0.0.

## See Also

- [var tabStops: [NSTextTab]](nsparagraphstyle/tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [NSParagraphStyle.TextTabType](../AppKit/NSParagraphStyle/TextTabType.md)
  Constants that specify the type of tab stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsparagraphstyle/defaulttabinterval)*