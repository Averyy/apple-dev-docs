# prefersEqualWidths

**Framework**: AppKit  
**Kind**: property

A Boolean value that specifies that items should have equal widths when possible.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
@MainActor
var prefersEqualWidths: Bool { get set }
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/Swift/true), items in the [`groupTouchBar`](nsgrouptouchbaritem/grouptouchbar.md) are sized to have equal widths when possible.

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var preferredItemWidth: CGFloat](nsgrouptouchbaritem/preferreditemwidth.md)
  The preferred width for items in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/prefersequalwidths)*