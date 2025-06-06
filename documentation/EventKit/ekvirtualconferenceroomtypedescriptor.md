# EKVirtualConferenceRoomTypeDescriptor

**Framework**: EventKit  
**Kind**: class

Details about a room where virtual conferences take place.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class EKVirtualConferenceRoomTypeDescriptor
```

#### Overview

To present a list of rooms where a virtual conference takes place, your virtual conference provider creates one or more room type descriptors. Each descriptor contains a user-visible title and an identifier of your choosing. When users create events using one of the rooms you provide, EventKit calls [`fetchVirtualConference(identifier:completionHandler:)`](ekvirtualconferenceprovider/fetchvirtualconference(identifier:completionhandler:).md) and passes the room’s identifier.

## Topics

### Creating Room Type Descriptors
- [init(title: String, identifier: EKVirtualConferenceRoomTypeIdentifier)](ekvirtualconferenceroomtypedescriptor/init(title:identifier:).md)
  Creates an object that describes a location where a virtual conference takes place.
### Configuring Room Type Descriptors
- [var title: String](ekvirtualconferenceroomtypedescriptor/title.md)
  The user-visible name of a room where virtual conferences take place, such as Personal Room or Team Room.
- [var identifier: EKVirtualConferenceRoomTypeIdentifier](ekvirtualconferenceroomtypedescriptor/identifier.md)
  A unique string you choose that identifies the room.
- [typealias EKVirtualConferenceRoomTypeIdentifier](ekvirtualconferenceroomtypeidentifier.md)
  The type for a room type identifier.

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

## See Also

- [class EKVirtualConferenceProvider](ekvirtualconferenceprovider.md)
  An object that associates virtual conferencing details with an event object in a user’s calendar.
- [class EKVirtualConferenceDescriptor](ekvirtualconferencedescriptor.md)
  Details about a virtual conference that uses a custom room type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekvirtualconferenceroomtypedescriptor)*