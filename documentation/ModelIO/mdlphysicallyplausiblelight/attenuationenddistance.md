# attenuationEndDistance

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The distance from the light source, in units of local coordinate space, at which its illumination becomes zero.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var attenuationEndDistance: Float { get set }
```

```objc
@property (nonatomic, readwrite) float attenuationEndDistance;
```

## Discussion

At distances less than the start distance, the light’s illumination is at full intensity. At distances greater than the end distance, the light provides no illumination. At distances in between the start and end distance, the attenuationFalloffExponent property defines the transition from full illumination to no illumination.

The default distance is `2.0`.

## See Also

### Managing Attenuation
- [var attenuationStartDistance: Float](./attenuationstartdistance.md)
  The distance from the light source, in units of local coordinate space, at which its illumination begins to diminish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblelight/attenuationenddistance)*