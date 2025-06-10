# delegate

**Framework**: RoomPlan  
**Kind**: property

An object that determines whether to post-process the results of a scan.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency weak var delegate: (any RoomCaptureViewDelegate)?
```

## See Also

- [var captureSession: RoomCaptureSession!](roomcaptureview/capturesession.md)
  An object that notifies a delegate of particular events in the room-scanning life cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/delegate)*