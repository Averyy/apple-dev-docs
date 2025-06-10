# HMRoom

**Framework**: HomeKit  
**Kind**: class

The smallest subdivision of a home’s space.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMRoom
```

#### Overview

An [`HMRoom`](hmroom.md) instance is a part of a home representing an individual room in the home. Rooms don’t have any physical characteristics like size or location. Instead, they’re names that are meaningful to the user, like “living room” or “kitchen”. Meaningful room names enable voice commands like “Siri, turn on the kitchen lights.”

You create new rooms using the [`addRoom(withName:completionHandler:)`](hmhome/addroom(withname:completionhandler:).md) method of [`HMHome`](hmhome.md). You can also group rooms into zones using instances of [`HMZone`](hmzone.md). You can assign accessories to rooms, indicating the presence of that accessory in that room.

## Topics

### Identifying a room
- [var name: String](hmroom/name.md)
  The name of the room.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmroom/updatename(_:completionhandler:).md)
  Updates the name of the room.
- [var uniqueIdentifier: UUID](hmroom/uniqueidentifier.md)
  The unique identifier for a room.
### Finding accessories
- [var accessories: [HMAccessory]](hmroom/accessories.md)
  The collection of accessories in the room.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var room: HMRoom?](hmaccessory/room.md)
  The room containing the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmroom)*