# threshold

**Framework**: PencilKit  
**Kind**: property

The threshold for clipping the stroke rendering.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var threshold: CGFloat { get }
```

#### Discussion

When rendering only pixels with an alpha greater than the threshold are drawn. A threshold of 0 has no affect on rendering, a threshold of 1 does not draw anything. Thresholds are only used for some inks, eg. `.reed`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepoint-swift.struct/threshold)*