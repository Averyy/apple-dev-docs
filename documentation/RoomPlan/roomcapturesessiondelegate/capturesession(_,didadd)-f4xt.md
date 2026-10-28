# captureSession(_:didAdd:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Provides a default, blank implementation for when the capture session adds surfaces and objects to the scan results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didAdd room: CapturedRoom)
```

## Discussion

The system calls this implementation if your app doesn’t implement [`captureSession(_:didAdd:)`](./capturesession%28_,didadd%29.md).

## Parameters

- `session`: An object that manages the room-scanning process.
- `room`: A structure that contains the newest surfaces and objects that the framework identifies during the scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didadd:)-f4xt)*