# threshold

**Framework**: RealityKit  
**Kind**: property

The brightness threshold for bloom activation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var threshold: Float
```

#### Discussion

Only pixels with luminance values above this threshold will contribute to the bloom effect. The value is typically in the range `[0.0, 1.x]`:

- `0.0` makes all pixels contribute to bloom
- `1.0` standard threshold for HDR content (default)
- `>1` only very bright highlights will bloom

Higher thresholds create more selective bloom that only affects the brightest elements in the scene.

## See Also

- [var strength: Float](bloomsettingscomponent/strength.md)
  The intensity of the bloom effect.
- [var blurRadius: Float](bloomsettingscomponent/blurradius.md)
  The width of the bloom blur kernel as a percentage of screen width


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bloomsettingscomponent/threshold)*