# UIPencilInteraction.Phase

**Framework**: UIKit  
**Kind**: enum

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

## Topics

### Phases
- [UIPencilInteraction.Phase.began](uipencilinteraction/phase/began.md)
  A continuous gesture on the pencil began
- [UIPencilInteraction.Phase.cancelled](uipencilinteraction/phase/cancelled.md)
  A continuous gesture on the pencil was cancelled
- [UIPencilInteraction.Phase.changed](uipencilinteraction/phase/changed.md)
  A continuous gesture on the pencil changed
- [UIPencilInteraction.Phase.ended](uipencilinteraction/phase/ended.md)
  A continuous gesture on the pencil ended, or a discrete gesture on the pencil recognized
### Initializers
- [init?(rawValue: UInt)](uipencilinteraction/phase/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class UIPencilInteraction](uipencilinteraction.md)
  An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [protocol UIPencilInteractionDelegate](uipencilinteractiondelegate.md)
  The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [UIPencilInteraction.Tap](uipencilinteraction/tap.md)
  An interaction that represents a double tap on Apple Pencil.
- [UIPencilInteraction.Squeeze](uipencilinteraction/squeeze.md)
  An interaction that represents a squeeze on Apple Pencil.
- [class UIPencilHoverPose](uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction/phase)*