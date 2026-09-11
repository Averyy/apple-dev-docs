# CMClock.StartTimePattern

**Framework**: Core Media  
**Kind**: struct

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct StartTimePattern
```

## Topics

### Initializers
- [init(clockStartTime: CMTime, hostClockStartTime: CMTime, deltaBetweenPreferredStartTimes: CMTime)](cmclock/starttimepattern/init(clockstarttime:hostclockstarttime:deltabetweenpreferredstarttimes:).md)
### Instance Properties
- [var clockStartTime: CMTime](cmclock/starttimepattern/clockstarttime.md)
  The clock time of the next preferred start time.
- [var deltaBetweenPreferredStartTimes: CMTime](cmclock/starttimepattern/deltabetweenpreferredstarttimes.md)
  The delta between successive preferred start times.
- [var hostClockStartTime: CMTime](cmclock/starttimepattern/hostclockstarttime.md)
  The host clock time of the next preferred start time.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/starttimepattern)*