# HMMutableSignificantTimeEvent

**Framework**: HomeKit  
**Kind**: class

A mutable event that fires at the specified temporal offset to a significant event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HMMutableSignificantTimeEvent
```

## Topics

### Configuring a significant time event
- [var significantEvent: HMSignificantEvent](hmmutablesignificanttimeevent/significantevent.md)
  The significant time-based event that is used to calculate when the event fires.
- [var offset: DateComponents](hmmutablesignificanttimeevent/offset.md)
  The offset from the significant event that this event fires at.

## Relationships

### Inherits From
- [HMSignificantTimeEvent](hmsignificanttimeevent.md)
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

- [struct HMSignificantEvent](hmsignificantevent.md)
  An event that represents significant time-based events, including sunrise and sunset.
- [class HMSignificantTimeEvent](hmsignificanttimeevent.md)
  An event that fires at a time offset from a significant time-based event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablesignificanttimeevent)*