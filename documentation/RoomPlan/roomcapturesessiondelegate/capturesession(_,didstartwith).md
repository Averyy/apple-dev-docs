# captureSession(_:didStartWith:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the delegate when the session starts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didStartWith configuration: RoomCaptureSession.Configuration)
```

## Parameters

- `session`: An object that manages the room-scanning process.
- `configuration`: An object that customizes the scanning experience.

## Default Implementations

### RoomCaptureSessionDelegate Implementations
- [func captureSession(RoomCaptureSession, didStartWith: RoomCaptureSession.Configuration)](./capturesession%28_,didstartwith%29-3c74n.md)
  Provides a default, blank implementation for when the session starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didstartwith:))*