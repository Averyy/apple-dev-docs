# stop(pauseARSession:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Stops the room-capture session and indicates whether the app pauses the underlying AR session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func stop(pauseARSession: Bool = true)
```

## Mentions

- [Scanning the rooms of a single structure](../scanning-the-rooms-of-a-single-structure.md)

## Parameters

- `pauseARSession`: A Boolean value that indicates whether the framework automatically pauses the underlying AR session by calling [`pause()`](../../ARKit/arsession/pause%28%29.md). The default value is `true`. If you pass `false`, the AR session continues to run.

## See Also

### Controlling a session
- [func run(configuration: RoomCaptureSession.Configuration)](./run%28configuration%29.md)
  Starts a room-capture session with the specified configuration.
- [RoomCaptureSession.Configuration](./configuration.md)
  Settings that configure the room-scanning process.
- [func stop()](./stop%28%29.md)
  Stops the room-capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/stop(pausearsession:))*