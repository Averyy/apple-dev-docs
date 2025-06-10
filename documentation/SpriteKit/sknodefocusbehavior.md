# SKNodeFocusBehavior

**Framework**: SpriteKit  
**Kind**: enum

Options for the focusable states of a SpriteKit node.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum SKNodeFocusBehavior
```

## Topics

### Enumeration Cases
- [SKNodeFocusBehavior.none](sknodefocusbehavior/none.md)
  Node is not focusable.
- [SKNodeFocusBehavior.occluding](sknodefocusbehavior/occluding.md)
  Node is not focusable and prevents nodes that it visually obscures from becoming focusable.
- [SKNodeFocusBehavior.focusable](sknodefocusbehavior/focusable.md)
  Node is focusable and prevents nodes that it visually obscures from becoming focusable.
### Initializers
- [init?(rawValue: Int)](sknodefocusbehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [enum SKParticleRenderOrder](skparticlerenderorder.md)
  The order to use when the emitter’s particles are rendered.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknodefocusbehavior)*