# HMZone

**Framework**: HomeKit  
**Kind**: class

A collection of rooms that users think of as a single area, like upstairs or downstairs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMZone
```

#### Overview

An [`HMZone`](hmzone.md) instance is an optional grouping of rooms in a home, with names like “upstairs” and “downstairs”. Zones are optional—rooms don’t need to be in a zone. By adding rooms to a zone, the user can give commands to Siri like “Siri, turn on all of the lights downstairs.” A single room can be in multiple zones—for example, “kitchen” might be in both the “downstairs” and “entertainment area” zones.

You create new zones using the [`addZone(withName:completionHandler:)`](hmhome/addzone(withname:completionhandler:).md) method of [`HMHome`](hmhome.md). A zone can’t span homes—that is, you can’t create a zone that includes rooms from more than one home.

## Topics

### Identifying a Zone
- [var name: String](hmzone/name.md)
  The name of the zone.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmzone/updatename(_:completionhandler:).md)
  Updates the name of the zone.
- [var uniqueIdentifier: UUID](hmzone/uniqueidentifier.md)
  The unique identifier for a zone.
### Assigning Rooms to a Zone
- [var rooms: [HMRoom]](hmzone/rooms.md)
  Array of rooms in the zone.
- [func addRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](hmzone/addroom(_:completionhandler:).md)
  Adds a room to the zone.
- [func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](hmzone/removeroom(_:completionhandler:).md)
  Removes a room from the zone.

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

- [var zones: [HMZone]](hmhome/zones.md)
  An array of all the zones in the home.
- [func addZone(withName: String, completionHandler: (HMZone?, (any Error)?) -> Void)](hmhome/addzone(withname:completionhandler:).md)
  Adds a new zone to the home.
- [func removeZone(HMZone, completionHandler: ((any Error)?) -> Void)](hmhome/removezone(_:completionhandler:).md)
  Removes a zone from the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmzone)*