# role

**Framework**: Group Activities  
**Kind**: property  
**Required**: Yes

An optional role you associate with this element.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var role: (any SpatialTemplateRole)? { get }
```

#### Discussion

If you associate a role to a seat, a participant must request that role to sit in the seat. If your template contains seats with roles, include some seats without roles to handle people who are unable to acquire a seat with a role. For example, you might include seats for spectators as well as players of a game.

## See Also

- [var position: SpatialTemplateElementPosition](spatialtemplateelement/position.md)
  The location of the element in the shared coordinate space.
- [var direction: SpatialTemplateElementDirection](spatialtemplateelement/direction.md)
  The initial orientation of the element in the shared coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateelement/role)*