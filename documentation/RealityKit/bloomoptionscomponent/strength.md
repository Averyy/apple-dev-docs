# strength

**Framework**: RealityKit  
**Kind**: property

The intensity of the bloom effect.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var strength: Float
```

#### Discussion

Higher values create a more pronounced glow effect. The values can be be in the range `[0.0, 2.0]`, where:

- `0.0` disables the bloom effect entirely
- `0.25` provides a subtle bloom (default)
- `1.0` creates a strong, dramatic bloom effect
- `>1` extremely intense effects but may have some visual artifacts

## See Also

- [var threshold: Float](bloomoptionscomponent/threshold.md)
  The brightness threshold for bloom activation.
- [var blurRadius: Float](bloomoptionscomponent/blurradius.md)
  The width of the bloom blur kernel as a percentage of viewport height


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bloomoptionscomponent/strength)*