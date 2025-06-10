# TabletopInteraction.HoverAlignmentBehavior

**Framework**: TabletopKit  
**Kind**: enum

An object that describes how the controlled equipment should behave when approaching a target.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum HoverAlignmentBehavior
```

## Topics

### Enumeration Cases
- [case align(TabletopInteraction.HoverAlignmentSource, with: TabletopInteraction.CollisionTargets)](tabletopinteraction/hoveralignmentbehavior/align(_:with:).md)
  `align` indicates that the equipment should orient itself to align the closest `source` to the target. The equipment’s movement is also limited to prevent it from penetrating the target.
- [TabletopInteraction.HoverAlignmentBehavior.automatic(targets:)](tabletopinteraction/hoveralignmentbehavior/automatic(targets:).md)
  `automatic` picks a strategy based on the equipment size.
- [TabletopInteraction.HoverAlignmentBehavior.disabled](tabletopinteraction/hoveralignmentbehavior/disabled.md)
  Use this value to disable the behavior.
- [TabletopInteraction.HoverAlignmentBehavior.stop(at:)](tabletopinteraction/hoveralignmentbehavior/stop(at:).md)
  `stop` indicates that the equipment movement should stop when pushed into the target, to avoid penetration. The orientation of the equipment is not affected.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/hoveralignmentbehavior)*