# HMLocationEvent

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

An event that is evaluated based on entry to or exit from a region.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- watchOS 2.0+

## Declaration

```swift
class HMLocationEvent
```

```objc
@interface HMLocationEvent : HMEvent
```

## Topics

### Creating a Location Event
- [init(region: CLRegion)](./hmlocationevent/init%28region%29.md)
  Creates a new location event with the specified region.
### Inspecting the Region
- [var region: CLRegion?](./hmlocationevent/region.md)
  The region on which events are triggered.
### Configuring the Region
- [func updateRegion(CLRegion, completionHandler: ((any Error)?) -> Void)](./hmlocationevent/updateregion%28_,completionhandler%29.md)
  Changes the region associated with this event.

## Relationships

### Inherits From
- [HMEvent](./hmevent.md)
### Inherited By
- [HMMutableLocationEvent](./hmmutablelocationevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Locations
- [class HMMutableLocationEvent](./hmmutablelocationevent.md)
  A mutable event that is evaluated based on entry to or exit from a region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmlocationevent)*