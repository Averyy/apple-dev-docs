# proposedDestination

**Framework**: TabletopKit  
**Kind**: property  
**Role**: Instance Property

The proposed destination of the main interaction object, computed from the current pose of the object. During a toss simulation, the proposed destination is only updated if there is only one tossed equipment and it is the currently controlled equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var proposedDestination: TabletopInteraction.Destination? { get }
```

## See Also

### Getting the proposed locations
- [var proposedFlip: Bool](./proposedflip.md)
  Was the object flipped from the start of this interaction


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/value-swift.struct/proposeddestination)*