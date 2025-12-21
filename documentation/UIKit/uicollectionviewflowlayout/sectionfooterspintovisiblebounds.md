# sectionFootersPinToVisibleBounds

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether footers pin to the bottom of the collection view bounds during scrolling.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sectionFootersPinToVisibleBounds: Bool { get set }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/Swift/true), section footer views scroll with content until they reach the bottom of the screen, at which point they are pinned to the lower bounds of the collection view. Each new footer view that scrolls to the bottom of the screen pushes the previously pinned footer view offscreen.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var sectionHeadersPinToVisibleBounds: Bool](uicollectionviewflowlayout/sectionheaderspintovisiblebounds.md)
  A Boolean value that indicates whether headers pin to the top of the collection view bounds during scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/sectionfooterspintovisiblebounds)*