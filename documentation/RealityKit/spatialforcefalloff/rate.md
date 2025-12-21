# rate

**Framework**: RealityKit  
**Kind**: property

The spatial falloff / attenuation rate.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var rate: Double
```

#### Discussion

An exponent that determines how the effect’s strength diminishes with distance. Use a non-negative rate.

- When the rate is , no falloff occurs.
- When the rate is , falloff occurs slower and is sublinear.
- When the rate is , falloff is linear.
- When the rate is , falloff occurs faster and is nonlinear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialforcefalloff/rate)*