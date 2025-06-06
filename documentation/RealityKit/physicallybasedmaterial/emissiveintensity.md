# emissiveIntensity

**Framework**: RealityKit  
**Kind**: property

The intensity of light emitted by the entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var emissiveIntensity: Float { get set }
```

#### Discussion

To make a material  and appear to emit light, set this property to a value greater than zero and set [`emissiveColor`](physicallybasedmaterial/emissivecolor-swift.property.md) to a value other than black. RealityKit multiplies [`emissiveColor`](physicallybasedmaterial/emissivecolor-swift.property.md) by this value, so the higher the value, the more intense the entity’s emission of light.

You can set this property to values greater than `1.0`.

## See Also

- [var emissiveColor: PhysicallyBasedMaterial.EmissiveColor](physicallybasedmaterial/emissivecolor-swift.property.md)
  The color of the light the entity emits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/emissiveintensity)*