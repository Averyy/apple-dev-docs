# attenuationEndDistance

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The distance from the light at which its intensity is completely diminished. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var attenuationEndDistance: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat attenuationEndDistance;
```

## Discussion

You can apply attenuation to omnidirectional lights and spotlights, causing their intensity to diminish over a specified range of distances. At distances less than the start distance, the light’s illumination is at full intensity. At distances greater than the end distance, the light provides no illumination. At distances in between the start and end distance, the [`attenuationFalloffExponent`](./attenuationfalloffexponent.md) property defines the transition from full illumination to no illumination.

The default value is `0.0`, specifying no attenuation (the light’s intensity is the same at all distances).

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing Light Attenuation
- [var attenuationStartDistance: CGFloat](./attenuationstartdistance.md)
  The distance from the light at which its intensity begins to diminish. Animatable.
- [var attenuationFalloffExponent: CGFloat](./attenuationfalloffexponent.md)
  The transition curve for the light’s intensity between its attenuation start and end distances. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/attenuationenddistance)*