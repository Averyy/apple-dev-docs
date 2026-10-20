# TableVisualState.Contact

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An object that represents the contact of a collision during a simulation of tossable equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Contact
```

## Topics

### Getting collision objects
- [let collider: any Equipment](./contact/collider.md)
  A dynamic equipment that is in contact with either another equipment or the game’s boundary.
- [let collidedWithEquipment: EquipmentIdentifier?](./contact/collidedwithequipment.md)
  The other equipment identifier in contact or `nil` if in contact with the game’s boundary.
### Getting collision metrics
- [let impulse: Float](./contact/impulse.md)
  Impulse, the force over time of the collision, in newton-seconds.
- [let normal: Vector3D](./contact/normal.md)
  The normal of the contacting surfaces at the contact point. The normal direction points from the second shape to the first shape.
- [let position: Point3D](./contact/position.md)
  A position representing the estimated point of contact.

## See Also

### Representing collision states
- [var contacts: some Sequence<TableVisualState.Contact>](./contacts.md)
  Returns all contacts for the current update of the physics simulation.
- [func contacts<E>(of: E.Type) -> some Sequence<TableVisualState.Contact>
](./contacts%28of%29.md)
  Returns all contacts for the current update of the physics simulation for a specified equipment type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/contact)*