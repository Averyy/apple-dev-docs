# TableVisualState.Contact

**Framework**: TabletopKit  
**Kind**: struct

An object that represents the contact of a collision during a simulation of tossable equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Contact
```

## Topics

### Getting collision objects
- [let collider: any Equipment](tablevisualstate/contact/collider.md)
  A dynamic equipment that is in contact with either another equipment or the game’s boundary.
- [let collidedWithEquipment: EquipmentIdentifier?](tablevisualstate/contact/collidedwithequipment.md)
  The other equipment identifier in contact or `nil` if in contact with the game’s boundary.
### Getting collision metrics
- [let impulse: Float](tablevisualstate/contact/impulse.md)
  Impulse, the force over time of the collision, in newton-seconds.
- [let normal: Vector3D](tablevisualstate/contact/normal.md)
  The normal of the contacting surfaces at the contact point. The normal direction points from the second shape to the first shape.
- [let position: Point3D](tablevisualstate/contact/position.md)
  A position representing the estimated point of contact.

## See Also

- [var contacts: some Sequence<TableVisualState.Contact>](tablevisualstate/contacts.md)
  Returns all contacts for the current update of the physics simulation.
- [func contacts<E>(of: E.Type) -> some Sequence<TableVisualState.Contact>
](tablevisualstate/contacts(of:).md)
  Returns all contacts for the current update of the physics simulation for a specified equipment type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/contact)*