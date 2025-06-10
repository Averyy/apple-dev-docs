# CPNowPlayingSportsEventStatus

**Framework**: CarPlay  
**Kind**: class

A representation of the status of a sporting event.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
class CPNowPlayingSportsEventStatus
```

## Topics

### Initializers
- [init(eventStatusText: [String]?, eventStatusImage: UIImage?, eventClock: CPNowPlayingSportsClock?)](cpnowplayingsportseventstatus/init(eventstatustext:eventstatusimage:eventclock:).md)
  Initialize an event status with optional event status text, an optional event status image, and an optional event clock.
### Instance Properties
- [var eventClock: CPNowPlayingSportsClock?](cpnowplayingsportseventstatus/eventclock.md)
  The event timer, if it applies to this event. See @c CPNowPlayingSportsClock.
- [var eventStatusImage: UIImage?](cpnowplayingsportseventstatus/eventstatusimage.md)
  An optional event status image for this event, if it applies to this event. For example, a baseball game could display a representation of the bases and outs, indicating how many bases are loaded and the number of outs in the current inning.
- [var eventStatusText: [String]?](cpnowplayingsportseventstatus/eventstatustext.md)
  Up to three separate strings for event status may be displayed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportseventstatus)*