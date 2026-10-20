# captureSession(_:didProvide:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the delegate of an instruction to display to the user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didProvide instruction: RoomCaptureSession.Instruction)
```

## Parameters

- `session`: An object that manages the room-scanning process.
- `instruction`: A specific recommendation the framework makes for the user to complete the scan.

## Default Implementations

### RoomCaptureSessionDelegate Implementations
- [func captureSession(RoomCaptureSession, didProvide: RoomCaptureSession.Instruction)](./capturesession%28_,didprovide%29-5hvhl.md)
  Provides a default, blank implementation for when the capture session provides a user instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didprovide:))*