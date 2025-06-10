# RoomCaptureSession.Configuration

**Framework**: RoomPlan  
**Kind**: struct

Settings that configure the room-scanning process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
struct Configuration
```

#### Overview

The `configuration` argument of a room-capture session’s  [`run(configuration:)`](roomcapturesession/run(configuration:).md) function is of this type.

## Topics

### Creating a configuration
- [init()](roomcapturesession/configuration/init.md)
  Creates a configuration.
### Configuring a session
- [var isCoachingEnabled: Bool](roomcapturesession/configuration/iscoachingenabled.md)
  An option that indicates that the session periodically provides user instructions.

## See Also

- [func run(configuration: RoomCaptureSession.Configuration)](roomcapturesession/run(configuration:).md)
  Starts a room-capture session with the specified configuration.
- [func stop()](roomcapturesession/stop.md)
  Stops the room-capture session.
- [func stop(pauseARSession: Bool)](roomcapturesession/stop(pausearsession:).md)
  Stops the room-capture session and indicates whether the app pauses the underlying AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/configuration)*