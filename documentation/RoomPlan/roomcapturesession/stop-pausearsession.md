# stop(pauseARSession:)

**Framework**: RoomPlan  
**Kind**: method

Stops the room-capture session and indicates whether the app pauses the underlying AR session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS ?+

## Declaration

```swift
func stop(pauseARSession: Bool = true)
```

## Mentions

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

## Parameters

- `pauseARSession`: A Boolean value that indicates whether the framework automatically pauses the underlying AR session by calling  . The default value is  . If you pass  , the AR session continues to run.

## See Also

- [func run(configuration: RoomCaptureSession.Configuration)](roomcapturesession/run(configuration:).md)
  Starts a room-capture session with the specified configuration.
- [RoomCaptureSession.Configuration](roomcapturesession/configuration.md)
  Settings that configure the room-scanning process.
- [func stop()](roomcapturesession/stop.md)
  Stops the room-capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/stop(pausearsession:))*