# opacity

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

Opacity of the point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var opacity: CGFloat { get }
```

#### Discussion

The opacity of a [`PKStrokePoint`](../pkstrokepoint-swift.struct.md) has a range of `0-2`, which is a multiplier of the [`PKInk`](../pkink-swift.struct.md) opacity.

## See Also

### Getting the point’s drawing data
- [var size: CGSize](./size.md)
  The size of this point.
- [var secondaryScale: CGFloat](./secondaryscale.md)
- [var threshold: CGFloat](./threshold.md)
  The alpha threshold for clipping the stroke rendering for supported inks.
- [var lateralJitter: CGFloat](./lateraljitter.md)
  The amount of lateral particle jitter at the stroke edge for supported inks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepoint-swift.struct/opacity)*