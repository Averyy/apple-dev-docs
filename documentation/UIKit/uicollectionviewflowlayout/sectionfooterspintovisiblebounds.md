# sectionFootersPinToVisibleBounds

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether footers pin to the bottom of the collection view bounds during scrolling.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sectionFootersPinToVisibleBounds: Bool { get set }
```

```objc
@property (nonatomic) BOOL sectionFootersPinToVisibleBounds;
```

## Discussion

When this property is [`true`](../../Swift/true.md), section footer views scroll with content until they reach the bottom of the screen, at which point they are pinned to the lower bounds of the collection view. Each new footer view that scrolls to the bottom of the screen pushes the previously pinned footer view offscreen.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Pinning headers and footers
- [var sectionHeadersPinToVisibleBounds: Bool](./sectionheaderspintovisiblebounds.md)
  A Boolean value that indicates whether headers pin to the top of the collection view bounds during scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/sectionfooterspintovisiblebounds)*