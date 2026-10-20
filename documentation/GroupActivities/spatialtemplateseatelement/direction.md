# direction

**Framework**: Group Activities  
**Kind**: property  
**Role**: Instance Property

The initial orientation of the element in the shared coordinate space.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
let direction: SpatialTemplateElementDirection
```

#### Discussion

The direction you specify rotates the participant’s spatial Persona around the y-axis. This direction becomes the starting point for any further movements the person makes.

## See Also

### Getting the element details
- [let position: SpatialTemplateElementPosition](./position.md)
  The location of the element in the shared coordinate space.
- [let role: (any SpatialTemplateRole)?](./role.md)
  An optional role you associate with this element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateseatelement/direction)*