# CMClock.StartTimePattern

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

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
- [init(clockStartTime: CMTime, hostClockStartTime: CMTime, deltaBetweenPreferredStartTimes: CMTime)](./starttimepattern/init%28clockstarttime,hostclockstarttime,deltabetweenpreferredstarttimes%29.md)
### Instance Properties
- [var clockStartTime: CMTime](./starttimepattern/clockstarttime.md)
  The clock time of the next preferred start time.
- [var deltaBetweenPreferredStartTimes: CMTime](./starttimepattern/deltabetweenpreferredstarttimes.md)
  The delta between successive preferred start times.
- [var hostClockStartTime: CMTime](./starttimepattern/hostclockstarttime.md)
  The host clock time of the next preferred start time.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/starttimepattern)*