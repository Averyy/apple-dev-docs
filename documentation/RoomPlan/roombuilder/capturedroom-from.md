# capturedRoom(from:)

**Framework**: RoomPlan  
**Kind**: method

Processes the specified raw scan results and returns a detailed representation of the room.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
func capturedRoom(from capturedRoomData: CapturedRoomData) async throws -> CapturedRoom
```

#### Return Value

A captured-room object that provides the key details of a scanned room.

#### Discussion

You retrieve the argument `capturedRoomData` in one of the following ways:

- The [`captureView(shouldPresent:error:)`](roomcaptureviewdelegate/captureview(shouldpresent:error:).md) callback for an app that scans rooms using the framework-provided view ([`RoomCaptureView`](roomcaptureview.md)).
- The [`captureSession(_:didEndWith:error:)`](roomcapturesessiondelegate/capturesession(_:didendwith:error:).md) callback for an app that implements its own room-scanning view.

## Parameters

- `capturedRoomData`: A data object that contains raw scan results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roombuilder/capturedroom(from:))*