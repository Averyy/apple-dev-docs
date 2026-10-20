# run(configuration:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Starts a room-capture session with the specified configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func run(configuration: RoomCaptureSession.Configuration)
```

## Mentions

- [Scanning the rooms of a single structure](../scanning-the-rooms-of-a-single-structure.md)

## Parameters

- `configuration`: An object that customizes the scanning experience.

## See Also

### Controlling a session
- [RoomCaptureSession.Configuration](./configuration.md)
  Settings that configure the room-scanning process.
- [func stop()](./stop%28%29.md)
  Stops the room-capture session.
- [func stop(pauseARSession: Bool)](./stop%28pausearsession%29.md)
  Stops the room-capture session and indicates whether the app pauses the underlying AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/run(configuration:))*