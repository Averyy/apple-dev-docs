# sectionHeadersPinToVisibleBounds

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether headers pin to the top of the collection view bounds during scrolling.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sectionHeadersPinToVisibleBounds: Bool { get set }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/swift/true), section header views scroll with content until they reach the top of the screen, at which point they are pinned to the upper bounds of the collection view. Each new header view that scrolls to the top of the screen pushes the previously pinned header view offscreen.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var sectionFootersPinToVisibleBounds: Bool](uicollectionviewflowlayout/sectionfooterspintovisiblebounds.md)
  A Boolean value that indicates whether footers pin to the bottom of the collection view bounds during scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/sectionheaderspintovisiblebounds)*