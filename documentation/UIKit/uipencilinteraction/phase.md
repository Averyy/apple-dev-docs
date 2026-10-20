# UIPencilInteraction.Phase

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the phases of an interaction on Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 26.2+

## Declaration

```swift
enum Phase
```

```c
enum UIPencilInteractionPhase : NSUInteger;
```

## Topics

### Phases
- [UIPencilInteraction.Phase.began](./phase/began.md)
  A continuous gesture on the pencil began
- [UIPencilInteraction.Phase.cancelled](./phase/cancelled.md)
  A continuous gesture on the pencil was cancelled
- [UIPencilInteraction.Phase.changed](./phase/changed.md)
  A continuous gesture on the pencil changed
- [UIPencilInteraction.Phase.ended](./phase/ended.md)
  A continuous gesture on the pencil ended, or a discrete gesture on the pencil recognized
### Initializers
- [init?(rawValue: UInt)](./phase/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Apple Pencil interactions in UIKit
- [class UIPencilInteraction](../uipencilinteraction.md)
  An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [protocol UIPencilInteractionDelegate](../uipencilinteractiondelegate.md)
  The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [UIPencilInteraction.Tap](./tap.md)
  An interaction that represents a double tap on Apple Pencil.
- [UIPencilInteraction.Squeeze](./squeeze.md)
  An interaction that represents a squeeze on Apple Pencil.
- [class UIPencilHoverPose](../uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction/phase)*