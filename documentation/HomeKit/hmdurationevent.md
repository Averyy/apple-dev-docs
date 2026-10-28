# HMDurationEvent

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMDurationEvent : HMTimeEvent
```

## Overview

Use a duration event to specify that a different event should end after a period of time.

## Topics

### Creating a duration event
- [init(duration: TimeInterval)](./hmdurationevent/init%28duration%29.md)
  Creates a duration event with the specified time duration.
### Inspecting a duration event
- [var duration: TimeInterval](./hmdurationevent/duration.md)
  The event’s duration, in seconds.

## Relationships

### Inherits From
- [HMTimeEvent](./hmtimeevent.md)
### Inherited By
- [HMMutableDurationEvent](./hmmutabledurationevent.md)
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

### Durations
- [class HMMutableDurationEvent](./hmmutabledurationevent.md)
  A mutable event that fires after the specified time duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmdurationevent)*