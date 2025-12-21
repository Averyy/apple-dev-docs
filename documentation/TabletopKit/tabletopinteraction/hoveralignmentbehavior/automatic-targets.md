# TabletopInteraction.HoverAlignmentBehavior.automatic(targets:)

**Framework**: TabletopKit  
**Kind**: case

`automatic` picks a strategy based on the equipment size.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
case automatic(targets: TabletopInteraction.CollisionTargets)
```

## See Also

- [case align(TabletopInteraction.HoverAlignmentSource, with: TabletopInteraction.CollisionTargets)](tabletopinteraction/hoveralignmentbehavior/align(_:with:).md)
  `align` indicates that the equipment should orient itself to align the closest `source` to the target. The equipment’s movement is also limited to prevent it from penetrating the target.
- [TabletopInteraction.HoverAlignmentBehavior.disabled](tabletopinteraction/hoveralignmentbehavior/disabled.md)
  Use this value to disable the behavior.
- [TabletopInteraction.HoverAlignmentBehavior.stop(at:)](tabletopinteraction/hoveralignmentbehavior/stop(at:).md)
  `stop` indicates that the equipment movement should stop when pushed into the target, to avoid penetration. The orientation of the equipment is not affected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/hoveralignmentbehavior/automatic(targets:))*