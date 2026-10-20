# CPNowPlayingSportsEventStatus

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

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

```objc
@interface CPNowPlayingSportsEventStatus : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./cpnowplayingsportseventstatus/init%28coder%29.md)
- [init(eventStatusText: [String]?, eventStatusImage: UIImage?, eventClock: CPNowPlayingSportsClock?)](./cpnowplayingsportseventstatus/init%28eventstatustext,eventstatusimage,eventclock%29.md)
  Initialize an event status with optional event status text, an optional event status image, and an optional event clock.
### Instance Properties
- [var eventClock: CPNowPlayingSportsClock?](./cpnowplayingsportseventstatus/eventclock.md)
  The event timer, if it applies to this event. See @c CPNowPlayingSportsClock.
- [var eventStatusImage: UIImage?](./cpnowplayingsportseventstatus/eventstatusimage.md)
  An optional event status image for this event, if it applies to this event. For example, a baseball game could display a representation of the bases and outs, indicating how many bases are loaded and the number of outs in the current inning.
- [var eventStatusText: [String]?](./cpnowplayingsportseventstatus/eventstatustext.md)
  Up to three separate strings for event status may be displayed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportseventstatus)*