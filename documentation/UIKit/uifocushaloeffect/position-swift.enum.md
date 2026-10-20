# UIFocusHaloEffect.Position

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe positions for drawing the halo focus effect.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
enum Position
```

```c
enum UIFocusHaloEffectPosition : NSInteger;
```

## Topics

### Constants
- [UIFocusHaloEffect.Position.automatic](./position-swift.enum/automatic.md)
  A constant that automatically chooses a position for drawing the halo effect depending on the focus item and its containing view hierarchy.
- [UIFocusHaloEffect.Position.outside](./position-swift.enum/outside.md)
  A constant that draws the halo effect around the shape.
- [UIFocusHaloEffect.Position.inside](./position-swift.enum/inside.md)
  A constant that draws the halo effect inside the shape.
### Initializers
- [init?(rawValue: Int)](./position-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Focus effects
- [class UIFocusEffect](../uifocuseffect.md)
  The base class for defining a visual focus effect.
- [class UIFocusHaloEffect](../uifocushaloeffect.md)
  A visual focus effect that draws a halo around the focus item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocushaloeffect/position-swift.enum)*