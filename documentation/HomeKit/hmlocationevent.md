# HMLocationEvent

**Framework**: HomeKit  
**Kind**: class

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

## Topics

### Creating a Location Event
- [init(region: CLRegion)](hmlocationevent/init(region:).md)
  Creates a new location event with the specified region.
### Inspecting the Region
- [var region: CLRegion?](hmlocationevent/region.md)
  The region on which events are triggered.
### Configuring the Region
- [func updateRegion(CLRegion, completionHandler: ((any Error)?) -> Void)](hmlocationevent/updateregion(_:completionhandler:).md)
  Changes the region associated with this event.

## Relationships

### Inherits From
- [HMEvent](hmevent.md)
### Inherited By
- [HMMutableLocationEvent](hmmutablelocationevent.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSMutableCopying](../foundation/nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class HMMutableLocationEvent](hmmutablelocationevent.md)
  A mutable event that is evaluated based on entry to or exit from a region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmlocationevent)*