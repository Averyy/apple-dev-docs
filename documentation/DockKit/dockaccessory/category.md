# DockAccessory.Category

**Framework**: DockKit  
**Kind**: enum  
**Role**: Enumeration

Types of supported dock accesories.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
enum Category
```

## Topics

### Getting properties
- [DockAccessory.Category.trackingStand](./category/trackingstand.md)
  The dock accessory is a tracking stand.
- [var debugDescription: String](./category/debugdescription.md)
  The text description of the dock accessory state.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting accessory information
- [var firmwareVersion: String?](./firmwareversion.md)
  The firmware version of the dock accessory.
- [var hardwareModel: String?](./hardwaremodel.md)
  The model of the dock accessory.
- [let identifier: DockAccessory.Identifier](./identifier-swift.property.md)
  The name and unique identifer of the dock accessory.
- [DockAccessory.Identifier](./identifier-swift.struct.md)
  Information that uniquely identifies the dock accessory.
- [DockAccessory.State](./state.md)
  The state of a dock accessory.
- [DockAccessory.StateChange](./statechange.md)
  An event that indicates a change in the state of a dock accessory.
- [DockAccessory.StateChanges](./statechanges.md)
  An asynchronous sequence of dock accessory state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/category)*