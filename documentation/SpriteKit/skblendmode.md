# SKBlendMode

**Framework**: SpriteKit  
**Kind**: enum

The modes that describe how the source and destination pixel colors are used to calculate the new destination color.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SKBlendMode
```

## Topics

### Constants
- [SKBlendMode.alpha](skblendmode/alpha.md)
  The source and destination colors are blended by multiplying the source alpha value.
- [SKBlendMode.add](skblendmode/add.md)
  The source and destination colors are added together.
- [SKBlendMode.subtract](skblendmode/subtract.md)
  The source color is subtracted from the destination color.
- [SKBlendMode.multiply](skblendmode/multiply.md)
  The source color is multiplied by the destination color.
- [SKBlendMode.multiplyX2](skblendmode/multiplyx2.md)
  The source color is multiplied by the destination color and then doubled.
- [SKBlendMode.screen](skblendmode/screen.md)
  The source color is added to the destination color times the inverted source color.
- [SKBlendMode.replace](skblendmode/replace.md)
  The source color replaces the destination color.
### Enumeration Cases
- [SKBlendMode.multiplyAlpha](skblendmode/multiplyalpha.md)
### Initializers
- [init?(rawValue: Int)](skblendmode/init(rawvalue:).md)

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
- [enum SKNodeFocusBehavior](sknodefocusbehavior.md)
  Options for the focusable states of a SpriteKit node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skblendmode)*