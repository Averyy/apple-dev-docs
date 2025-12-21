# falloff

**Framework**: SpriteKit  
**Kind**: property

The exponent that defines the rate of decay for the strength of the field as the distance increases between the node and the physics body being affected.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var falloff: Float { get set }
```

## Mentions

- [Adding Physics Fields to a Scene](adding-physics-fields-to-a-scene.md)

#### Discussion

When the force of a field node is calculated, the force is multiplied by `pow(distance - minRadius, -falloff)`. The default falloff value is `0`, which indicates that no attenuation takes place. Some types of field nodes ignore the falloff parameter entirely, while others change the default value to something that is more logical for that type of field node.

## See Also

- [var strength: Float](skfieldnode/strength.md)
  The strength of the field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode/falloff)*