# captureSession(_:didEndWith:error:)

**Framework**: RoomPlan  
**Kind**: method  
**Required**: Yes

Notifies the delegate of completion with either scan results or an error.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

## Declaration

```swift
func captureSession(_ session: RoomCaptureSession, didEndWith data: CapturedRoomData, error: (any Error)?)
```

## Mentions

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

## Parameters

- `session`: An object that manages the room-scanning process.
- `data`: A data object that contains the raw scan results.
- `error`: An object that describes the problem when an error occurs; otherwise,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate/capturesession(_:didendwith:error:))*