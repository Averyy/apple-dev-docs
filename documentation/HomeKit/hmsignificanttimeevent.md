# HMSignificantTimeEvent

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

An event that fires at a time offset from a significant time-based event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HMSignificantTimeEvent
```

```objc
@interface HMSignificantTimeEvent : HMTimeEvent
```

## Overview

Use this class to represent an event that fires at a time relative to a significant event, for example “30 minutes before sunset”.

## Topics

### Creating a significant time event
- [init(significantEvent: HMSignificantEvent, offset: DateComponents?)](./hmsignificanttimeevent/init%28significantevent,offset%29.md)
  Creates a new significant time event with the specified significant event and offset.
### Inspecting a significant time event
- [var significantEvent: HMSignificantEvent](./hmsignificanttimeevent/significantevent.md)
  The significant time-based event that is used to calculate when the event fires.
- [var offset: DateComponents?](./hmsignificanttimeevent/offset.md)
  The offset from the significant event that the event fires at.

## Relationships

### Inherits From
- [HMTimeEvent](./hmtimeevent.md)
### Inherited By
- [HMMutableSignificantTimeEvent](./hmmutablesignificanttimeevent.md)
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

### Significant events
- [struct HMSignificantEvent](./hmsignificantevent.md)
  An event that represents significant time-based events, including sunrise and sunset.
- [class HMMutableSignificantTimeEvent](./hmmutablesignificanttimeevent.md)
  A mutable event that fires at the specified temporal offset to a significant event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmsignificanttimeevent)*