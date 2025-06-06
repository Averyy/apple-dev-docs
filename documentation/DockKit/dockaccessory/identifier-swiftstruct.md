# DockAccessory.Identifier

**Framework**: DockKit  
**Kind**: struct

Information that uniquely identifies the dock accessory.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct Identifier
```

## Topics

### Getting properties
- [let name: String](dockaccessory/identifier-swift.struct/name.md)
  The dock accessory’s name.
- [let category: DockAccessory.Category](dockaccessory/identifier-swift.struct/category.md)
  The dock accessory’s category.
- [let uuid: UUID](dockaccessory/identifier-swift.struct/uuid.md)
  The dock accessory’s unique identifier.
- [var debugDescription: String](dockaccessory/identifier-swift.struct/debugdescription.md)
  The text description of the dock accessory state.
### Operators
- [static func == (DockAccessory.Identifier, DockAccessory.Identifier) -> Bool](dockaccessory/identifier-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](dockaccessory/identifier-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](dockaccessory/identifier-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](dockaccessory/identifier-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var firmwareVersion: String?](dockaccessory/firmwareversion.md)
  The firmware version of the dock accessory.
- [var hardwareModel: String?](dockaccessory/hardwaremodel.md)
  The model of the dock accessory.
- [let identifier: DockAccessory.Identifier](dockaccessory/identifier-swift.property.md)
  The name and unique identifer of the dock accessory.
- [DockAccessory.Category](dockaccessory/category.md)
  Types of supported dock accesories.
- [DockAccessory.State](dockaccessory/state.md)
  The state of a dock accessory.
- [DockAccessory.StateChange](dockaccessory/statechange.md)
  An event that indicates a change in the state of a dock accessory.
- [DockAccessory.StateChanges](dockaccessory/statechanges.md)
  An asynchronous sequence of dock accessory state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/identifier-swift.struct)*