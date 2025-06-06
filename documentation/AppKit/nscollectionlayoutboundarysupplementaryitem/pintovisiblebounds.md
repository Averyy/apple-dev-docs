# pinToVisibleBounds

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether a header or footer is pinned to the top or bottom visible boundary of the section or layout it’s attached to.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
var pinToVisibleBounds: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false), which means that the boundary supplementary item (header or footer) remains in its original position during scrolling, and moves offscreen as its section or layout scrolls. Set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) to pin the boundary supplementary item to the visible bounds of the section or layout it’s attached to. This way, the boundary supplementary item is shown while any portion of the section or layout it’s attached to is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutboundarysupplementaryitem/pintovisiblebounds)*