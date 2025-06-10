# DockAccessory.State

**Framework**: DockKit  
**Kind**: enum

The state of a dock accessory.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
enum State
```

## Topics

### Getting properties
- [DockAccessory.State.docked](dockaccessory/state/docked.md)
  The dock accessory doesn’t contain a device.
- [DockAccessory.State.undocked](dockaccessory/state/undocked.md)
  The dock accessory contains a device.
- [var debugDescription: String](dockaccessory/state/debugdescription.md)
  The text description of the dock accessory state.
### Operators
- [static func == (DockAccessory.State, DockAccessory.State) -> Bool](dockaccessory/state/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](dockaccessory/state/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](dockaccessory/state/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](dockaccessory/state/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var firmwareVersion: String?](dockaccessory/firmwareversion.md)
  The firmware version of the dock accessory.
- [var hardwareModel: String?](dockaccessory/hardwaremodel.md)
  The model of the dock accessory.
- [let identifier: DockAccessory.Identifier](dockaccessory/identifier-swift.property.md)
  The name and unique identifer of the dock accessory.
- [DockAccessory.Identifier](dockaccessory/identifier-swift.struct.md)
  Information that uniquely identifies the dock accessory.
- [DockAccessory.Category](dockaccessory/category.md)
  Types of supported dock accesories.
- [DockAccessory.StateChange](dockaccessory/statechange.md)
  An event that indicates a change in the state of a dock accessory.
- [DockAccessory.StateChanges](dockaccessory/statechanges.md)
  An asynchronous sequence of dock accessory state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/state)*