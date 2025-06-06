# usesPredominantAxisScrolling

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the scroll view uses a predominant scrolling axis for content.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var usesPredominantAxisScrolling: Bool { get set }
```

#### Discussion

Some content is scrollable in both the horizontal and vertical axes, but is predominantly scrolled one axis at a time. Other content (such as a drawing canvas) should scroll freely in both axes.

Traditionally this is not an issue with scroll wheels since they can only scroll in one direction at a time. With scroll balls and touch surfaces, it becomes more difficult to determine the user’s intention.

This property helps a scroll view determine the user’s intention by specifying if there is a predominant scrolling axis for content.

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the scroll view uses a predominant scrolling access. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/usespredominantaxisscrolling)*