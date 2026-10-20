# contacts(of:)

**Framework**: TabletopKit  
**Kind**: method

Returns all contacts for the current update of the physics simulation for a specified equipment type.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func contacts<E>(of type: E.Type) -> some Sequence<TableVisualState.Contact> where E : Equipment
```

## See Also

- [var contacts: some Sequence<TableVisualState.Contact>](tablevisualstate/contacts.md)
  Returns all contacts for the current update of the physics simulation.
- [TableVisualState.Contact](tablevisualstate/contact.md)
  An object that represents the contact of a collision during a simulation of tossable equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/contacts(of:))*