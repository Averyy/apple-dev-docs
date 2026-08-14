# AudioAccessoryHeadTracking.Handler

**Framework**: AudioAccessoryKit  
**Kind**: protocol

**Availability**:
- iOS 27.0+ (Beta)

## Declaration

```swift
protocol Handler : Sendable
```

## Topics

### Instance Methods
- [func activate(for: AudioAccessoryHeadTracking.Session)](audioaccessoryheadtracking/handler/activate(for:).md)
  Called when a head-tracking session has been established with the host.
- [func handleAccessorySensorMessage(TransportMessage)](audioaccessoryheadtracking/handler/handleaccessorysensormessage(_:).md)
  Called when a `TransportMessage` arrives from the accessory’s transport extension on the inbound channel.
- [func headTrackingStateDidChange(isActive: Bool)](audioaccessoryheadtracking/handler/headtrackingstatedidchange(isactive:).md)
  Called when the user-facing Head Tracking state for this accessory changes (e.g. via Settings or Control Center).
- [func invalidate()](audioaccessoryheadtracking/handler/invalidate.md)
  Called when the head-tracking session has been invalidated.

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/handler)*