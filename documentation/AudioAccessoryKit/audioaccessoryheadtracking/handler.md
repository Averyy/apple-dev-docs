# AudioAccessoryHeadTracking.Handler

**Framework**: AudioAccessoryKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 27.0+

## Declaration

```swift
protocol Handler : Sendable
```

## Topics

### Instance Methods
- [func activate(for: AudioAccessoryHeadTracking.Session)](./handler/activate%28for%29.md)
  Called when a head-tracking session has been established with the host.
- [func handleAccessorySensorMessage(TransportMessage)](./handler/handleaccessorysensormessage%28_%29.md)
  Called when a `TransportMessage` arrives from the accessory’s transport extension on the inbound channel.
- [func headTrackingStateDidChange(isActive: Bool)](./handler/headtrackingstatedidchange%28isactive%29.md)
  Called when the user-facing Head Tracking state for this accessory changes (e.g. via Settings or Control Center).
- [func invalidate()](./handler/invalidate%28%29.md)
  Called when the head-tracking session has been invalidated.

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/handler)*