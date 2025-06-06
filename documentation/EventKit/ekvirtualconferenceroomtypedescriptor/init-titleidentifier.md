# init(title:identifier:)

**Framework**: EventKit  
**Kind**: init

Creates an object that describes a location where a virtual conference takes place.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(title: String, identifier: EKVirtualConferenceRoomTypeIdentifier)
```

#### Return Value

An object that describes a location where a virtual conference takes place.

## Parameters

- `title`: The user-visible name of a room where virtual conferences take place, such as Personal Room or Team Room.
- `identifier`: A unique string you choose that identifies the room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekvirtualconferenceroomtypedescriptor/init(title:identifier:))*