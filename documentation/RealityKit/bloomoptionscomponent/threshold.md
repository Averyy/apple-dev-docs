# threshold

**Framework**: RealityKit  
**Kind**: property

The brightness threshold for bloom activation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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

- [var strength: Float](bloomoptionscomponent/strength.md)
  The intensity of the bloom effect.
- [var blurRadius: Float](bloomoptionscomponent/blurradius.md)
  The width of the bloom blur kernel as a percentage of viewport height


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bloomoptionscomponent/threshold)*