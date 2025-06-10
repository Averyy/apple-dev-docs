# init(frame:)

**Framework**: RoomPlan  
**Kind**: init

Creates a view that sizes to the specified frame.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic init(frame: CGRect)
```

#### Overview

This property inherits from [`UIView`](https://developer.apple.com/documentation/UIKit/UIView).

The system invokes this initializer if you omit the `arSession` argument to [`init(frame:arSession:)`](roomcaptureview/init(frame:arsession:).md). RoomPlan creates its own `ARSession` instance, which you can access through the [`captureSession`](roomcaptureview/capturesession.md) property’s [`arSession`](roomcapturesession/arsession.md).

## Parameters

- `frame`: A structure that positions and shapes the view.

## See Also

- [init(frame: CGRect, arSession: ARSession)](roomcaptureview/init(frame:arsession:).md)
  Creates a room-capture view with the given AR session.
- [init?(coder: NSCoder)](roomcaptureview/init(coder:).md)
  Creates a view by deserializing from the specified coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/init(frame:))*