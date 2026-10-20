# TabletopInteraction.HoverAlignmentBehavior.disabled

**Framework**: TabletopKit  
**Kind**: case  
**Role**: Case

Use this value to disable the behavior.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
case disabled
```

## See Also

### Alignment Behaviors
- [case align(TabletopInteraction.HoverAlignmentSource, with: TabletopInteraction.CollisionTargets)](./align%28_,with%29.md)
  `align` indicates that the equipment should orient itself to align the closest `source` to the target. The equipment’s movement is also limited to prevent it from penetrating the target.
- [TabletopInteraction.HoverAlignmentBehavior.automatic(targets:)](./automatic%28targets%29.md)
  `automatic` picks a strategy based on the equipment size.
- [TabletopInteraction.HoverAlignmentBehavior.stop(at:)](./stop%28at%29.md)
  `stop` indicates that the equipment movement should stop when pushed into the target, to avoid penetration. The orientation of the equipment is not affected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/hoveralignmentbehavior/disabled)*