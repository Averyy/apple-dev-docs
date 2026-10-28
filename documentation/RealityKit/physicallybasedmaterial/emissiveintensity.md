# emissiveIntensity

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The intensity of light emitted by the entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var emissiveIntensity: Float { get set }
```

## Discussion

To make a material *emissive* and appear to emit light, set this property to a value greater than zero and set [`emissiveColor`](./emissivecolor-swift.property.md) to a value other than black. RealityKit multiplies [`emissiveColor`](./emissivecolor-swift.property.md) by this value, so the higher the value, the more intense the entity’s emission of light.

You can set this property to values greater than `1.0`.

## See Also

### Adding light emission
- [var emissiveColor: PhysicallyBasedMaterial.EmissiveColor](./emissivecolor-swift.property.md)
  The color of the light the entity emits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/emissiveintensity)*