# rooms

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

Array of rooms in the zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var rooms: [HMRoom] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<HMRoom *> * rooms;
```

## See Also

### Assigning Rooms to a Zone
- [func addRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](./addroom%28_,completionhandler%29.md)
  Adds a room to the zone.
- [func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](./removeroom%28_,completionhandler%29.md)
  Removes a room from the zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmzone/rooms)*