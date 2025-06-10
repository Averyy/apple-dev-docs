# captureSession(_:didProvide:)

**Framework**: RoomPlan  
**Kind**: method  
**Required**: Yes

Notifies the delegate of an instruction to display to the user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didProvide instruction: RoomCaptureSession.Instruction)
```

## Parameters

- `session`: An object that manages the room-scanning process.
- `instruction`: A specific recommendation the framework makes for the user to complete the scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didprovide:))*