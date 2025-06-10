# TabletopInteraction.HoverAlignmentBehavior.align(_:with:)

**Framework**: TabletopKit  
**Kind**: case

`align` indicates that the equipment should orient itself to align the closest `source` to the target. The equipment’s movement is also limited to prevent it from penetrating the target.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
case align(TabletopInteraction.HoverAlignmentSource, with: TabletopInteraction.CollisionTargets)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/hoveralignmentbehavior/align(_:with:))*