# RoomCaptureSession.Configuration

**Framework**: RoomPlan  
**Kind**: struct  
**Role**: Structure

Settings that configure the room-scanning process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Configuration
```

#### Overview

The `configuration` argument of a room-capture session’s  [`run(configuration:)`](./run%28configuration%29.md) function is of this type.

## Topics

### Creating a configuration
- [init()](./configuration/init%28%29.md)
  Creates a configuration.
### Configuring a session
- [var isCoachingEnabled: Bool](./configuration/iscoachingenabled.md)
  An option that indicates that the session periodically provides user instructions.

## See Also

### Controlling a session
- [func run(configuration: RoomCaptureSession.Configuration)](./run%28configuration%29.md)
  Starts a room-capture session with the specified configuration.
- [func stop()](./stop%28%29.md)
  Stops the room-capture session.
- [func stop(pauseARSession: Bool)](./stop%28pausearsession%29.md)
  Stops the room-capture session and indicates whether the app pauses the underlying AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/configuration)*