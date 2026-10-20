# threshold

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The alpha threshold for clipping the stroke rendering for supported inks.

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

Only pixels with an alpha greater than the threshold are drawn. A threshold of `0` has no effect on rendering; a threshold of `1` draws nothing. Thresholds apply only to some inks, such as `.reed`.

## See Also

### Getting the point’s drawing data
- [var size: CGSize](./size.md)
  The size of this point.
- [var opacity: CGFloat](./opacity.md)
  Opacity of the point.
- [var secondaryScale: CGFloat](./secondaryscale.md)
- [var lateralJitter: CGFloat](./lateraljitter.md)
  The amount of lateral particle jitter at the stroke edge for supported inks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepoint-swift.struct/threshold)*