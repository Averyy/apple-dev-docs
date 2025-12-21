# TabletopInteraction.HoverAlignmentBehavior.align(_:with:)

**Framework**: TabletopKit  
**Kind**: case

`align` indicates that the equipment should orient itself to align the closest `source` to the target. The equipment’s movement is also limited to prevent it from penetrating the target.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
case align(TabletopInteraction.HoverAlignmentSource, with: TabletopInteraction.CollisionTargets)
```

## See Also

- [TabletopInteraction.HoverAlignmentBehavior.automatic(targets:)](tabletopinteraction/hoveralignmentbehavior/automatic(targets:).md)
  `automatic` picks a strategy based on the equipment size.
- [TabletopInteraction.HoverAlignmentBehavior.disabled](tabletopinteraction/hoveralignmentbehavior/disabled.md)
  Use this value to disable the behavior.
- [TabletopInteraction.HoverAlignmentBehavior.stop(at:)](tabletopinteraction/hoveralignmentbehavior/stop(at:).md)
  `stop` indicates that the equipment movement should stop when pushed into the target, to avoid penetration. The orientation of the equipment is not affected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/hoveralignmentbehavior/align(_:with:))*