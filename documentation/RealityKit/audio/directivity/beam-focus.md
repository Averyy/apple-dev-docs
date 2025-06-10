# Audio.Directivity.beam(focus:)

**Framework**: RealityKit  
**Kind**: case

A parametric frequency-dependent radiation pattern, where the `focus` determines the width of a beam.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
case beam(focus: Double)
```

#### Discussion

The `focus` parameter is in the range `0...1` where `0` is the default. The default `.beam(focus: 0)` projects sound of all frequencies evenly in all directions, where the rotation of the spatial audio source has no impact on the tonality of the sound. A `focus` of `0` is commonly referred to as “omnidirectional”.

Increasing the `focus` parameter up to `1` will constrain the projection to increasingly narrow beam patterns, with high frequencies being more directional than low frequencies. A spatial audio source with a non-zero `focus` will sound “darker” when auditioning the source from the rear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/directivity/beam(focus:))*