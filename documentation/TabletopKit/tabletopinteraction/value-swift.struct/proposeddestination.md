# proposedDestination

**Framework**: TabletopKit  
**Kind**: property

The proposed destination of the main interaction object, computed from the current pose of the object. During a toss simulation, the proposed destination is only updated if there is only one tossed equipment and it is the currently controlled equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var proposedDestination: TabletopInteraction.Destination? { get }
```

## See Also

- [var proposedFlip: Bool](tabletopinteraction/value-swift.struct/proposedflip.md)
  Was the object flipped from the start of this interaction


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/value-swift.struct/proposeddestination)*