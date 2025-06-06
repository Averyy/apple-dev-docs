# HMDurationEvent

**Framework**: HomeKit  
**Kind**: class

An event that ends after the specified time duration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HMDurationEvent
```

#### Overview

Use a duration event to specify that a different event should end after a period of time.

## Topics

### Creating a duration event
- [init(duration: TimeInterval)](hmdurationevent/init(duration:).md)
  Creates a duration event with the specified time duration.
### Inspecting a duration event
- [var duration: TimeInterval](hmdurationevent/duration.md)
  The event’s duration, in seconds.

## Relationships

### Inherits From
- [HMTimeEvent](hmtimeevent.md)
### Inherited By
- [HMMutableDurationEvent](hmmutabledurationevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class HMMutableDurationEvent](hmmutabledurationevent.md)
  A mutable event that fires after the specified time duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmdurationevent)*