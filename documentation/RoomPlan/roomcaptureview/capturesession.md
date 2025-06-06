# captureSession

**Framework**: RoomPlan  
**Kind**: property

An object that notifies a delegate of particular events in the room-scanning life cycle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency var captureSession: RoomCaptureSession! { get }
```

## Mentions

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

## See Also

- [var delegate: (any RoomCaptureViewDelegate)?](roomcaptureview/delegate.md)
  An object that determines whether to post-process the results of a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/capturesession)*