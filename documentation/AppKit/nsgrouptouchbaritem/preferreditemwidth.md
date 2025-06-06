# preferredItemWidth

**Framework**: AppKit  
**Kind**: property

The preferred width for items in the group when [`prefersEqualWidths`](nsgrouptouchbaritem/prefersequalwidths.md) is [`true`](https://developer.apple.com/documentation/swift/true).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
@MainActor
var preferredItemWidth: CGFloat { get set }
```

#### Discussion

This is the width that items are set to if there is enough room, and if the items don’t clip.

This value is ignored if it is negative. The default value is `-1`.

## See Also

- [var prefersEqualWidths: Bool](nsgrouptouchbaritem/prefersequalwidths.md)
  A Boolean value that specifies that items should have equal widths when possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/preferreditemwidth)*