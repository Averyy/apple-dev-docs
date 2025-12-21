# threshold

**Framework**: PencilKit  
**Kind**: property

The threshold for clipping the stroke rendering.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var threshold: CGFloat { get }
```

#### Discussion

When rendering only pixels with an alpha greater than the threshold are drawn. A threshold of 0 has no affect on rendering, a threshold of 1 does not draw anything. Thresholds are only used for some inks, eg. `.reed`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepoint-swift.struct/threshold)*