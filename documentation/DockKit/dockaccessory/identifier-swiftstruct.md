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