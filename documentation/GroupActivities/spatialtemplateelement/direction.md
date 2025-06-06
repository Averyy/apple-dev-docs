# direction

**Framework**: Group Activities  
**Kind**: property  
**Required**: Yes

The initial orientation of the element in the shared coordinate space.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var direction: SpatialTemplateElementDirection { get }
```

#### Discussion

The direction you specify rotates the participant’s spatial Persona around the y-axis. This direction becomes the starting point for any further movements the person makes.

## See Also

- [var position: SpatialTemplateElementPosition](spatialtemplateelement/position.md)
  The location of the element in the shared coordinate space.
- [var role: (any SpatialTemplateRole)?](spatialtemplateelement/role.md)
  An optional role you associate with this element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateelement/direction)*