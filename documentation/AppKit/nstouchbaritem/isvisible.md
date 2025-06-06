# isVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value that reflects whether or not the item is visible.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var isVisible: Bool { get }
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/swift/true), this item is shown in a currently visible bar. This property is always [`false`](https://developer.apple.com/documentation/swift/false) for spaces, proxy items, and groups.

This property is key-value observable.

## See Also

- [var visibilityPriority: NSTouchBarItem.Priority](nstouchbaritem/visibilitypriority.md)
  Determines which items are shown in a bar when space is limited.
- [NSTouchBarItem.Priority](nstouchbaritem/priority.md)
  Priorities for the visibility of a Touch Bar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/isvisible)*