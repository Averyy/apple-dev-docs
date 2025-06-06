# SKParticleRenderOrder

**Framework**: SpriteKit  
**Kind**: enum

The order to use when the emitter’s particles are rendered.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SKParticleRenderOrder
```

## Topics

### Constants
- [SKParticleRenderOrder.oldestLast](skparticlerenderorder/oldestlast.md)
  The particles are rendered from newest to oldest. This is the default value.
- [SKParticleRenderOrder.oldestFirst](skparticlerenderorder/oldestfirst.md)
  The particles are rendered from oldest to newest.
- [SKParticleRenderOrder.dontCare](skparticlerenderorder/dontcare.md)
  The particles can be rendered in any order. SpriteKit may choose to reorder the particles to improve rendering performance.
### Initializers
- [init?(rawValue: UInt)](skparticlerenderorder/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum SKActionTimingMode](skactiontimingmode.md)
  The modes that an action can use to adjust the apparent timing of the action.
- [enum SKAttributeType](skattributetype.md)
  Options that specify an attribute’s data type.
- [enum SKBlendMode](skblendmode.md)
  The modes that describe how the source and destination pixel colors are used to calculate the new destination color.
- [enum SKInterpolationMode](skinterpolationmode.md)
  The modes used to interpolate between keyframes in the sequence.
- [enum SKLabelHorizontalAlignmentMode](sklabelhorizontalalignmentmode.md)
  Options for aligning text horizontally.
- [enum SKLabelVerticalAlignmentMode](sklabelverticalalignmentmode.md)
  Options for aligning text vertically.
- [enum SKRepeatMode](skrepeatmode.md)
  The modes used to determine how the sequence repeats.
- [enum SKSceneScaleMode](skscenescalemode.md)
  The modes that determine how the scene’s area is mapped to the view that presents it.
- [enum SKTextureFilteringMode](sktexturefilteringmode.md)
  Texture filtering modes to use when the texture is drawn in a size other than its native size.
- [struct SKTileAdjacencyMask](sktileadjacencymask.md)
  An enumeration defining how neighboring tiles are automatically placed next to each other.
- [enum SKTileDefinitionRotation](sktiledefinitionrotation.md)
  The allowed rotations for a given tile.
- [enum SKTileSetType](sktilesettype.md)
  An enumeration defining how tiles are arranged.
- [enum SKTransitionDirection](sktransitiondirection.md)
  For some transitions, the direction in which the transition is performed.
- [enum SKUniformType](skuniformtype.md)
  An enumerated type to identify the type of a uniform object.
- [enum SKNodeFocusBehavior](sknodefocusbehavior.md)
  Options for the focusable states of a SpriteKit node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skparticlerenderorder)*