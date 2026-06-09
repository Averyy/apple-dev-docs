# AudioAccessoryHeadTracking.Handler

**Framework**: AudioAccessoryKit  
**Kind**: protocol

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
protocol Handler : Sendable
```

## Topics

### Instance Methods
- [func activate(for: AudioAccessoryHeadTracking.Session)](audioaccessoryheadtracking/handler/activate(for:).md)
  Called when a notification session has been established.
- [func didReceiveAccessorySensorMessage(TransportMessage)](audioaccessoryheadtracking/handler/didreceiveaccessorysensormessage(_:).md)
- [func headTrackingStateDidChange(isActive: Bool)](audioaccessoryheadtracking/handler/headtrackingstatedidchange(isactive:).md)
- [func invalidate()](audioaccessoryheadtracking/handler/invalidate.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/handler)*