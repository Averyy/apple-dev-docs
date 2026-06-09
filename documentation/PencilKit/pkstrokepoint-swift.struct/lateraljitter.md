# lateralJitter

**Framework**: PencilKit  
**Kind**: property

The amount of lateral particle jitter at the stroke edge for supported inks.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var lateralJitter: CGFloat { get }
```

#### Discussion

Lateral jitter applies only to some inks, such as `.pencil`.

## See Also

- [var size: CGSize](pkstrokepoint-swift.struct/size.md)
  The size of this point.
- [var opacity: CGFloat](pkstrokepoint-swift.struct/opacity.md)
  Opacity of the point.
- [var secondaryScale: CGFloat](pkstrokepoint-swift.struct/secondaryscale.md)
- [var threshold: CGFloat](pkstrokepoint-swift.struct/threshold.md)
  The alpha threshold for clipping the stroke rendering for supported inks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepoint-swift.struct/lateraljitter)*