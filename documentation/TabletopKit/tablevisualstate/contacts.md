# contacts

**Framework**: TabletopKit  
**Kind**: property

Returns all contacts for the current update of the physics simulation.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var contacts: some Sequence<TableVisualState.Contact> { get }
```

## See Also

- [func contacts<E>(of: E.Type) -> some Sequence<TableVisualState.Contact>
](tablevisualstate/contacts(of:).md)
  Returns all contacts for the current update of the physics simulation for a specified equipment type.
- [TableVisualState.Contact](tablevisualstate/contact.md)
  An object that represents the contact of a collision during a simulation of tossable equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/contacts)*