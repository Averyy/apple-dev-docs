# init(frame:)

**Framework**: RoomPlan  
**Kind**: init  
**Role**: Initializer

Creates a view that sizes to the specified frame.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic init(frame: CGRect)
```

## Overview

This property inherits from [`UIView`](../../UIKit/uiview.md).

The system invokes this initializer if you omit the `arSession` argument to [`init(frame:arSession:)`](./init%28frame,arsession%29.md). RoomPlan creates its own `ARSession` instance, which you can access through the [`captureSession`](./capturesession.md) property’s [`arSession`](../roomcapturesession/arsession.md).

## Parameters

- `frame`: A structure that positions and shapes the view.

## See Also

### Creating a room-capture view
- [init(frame: CGRect, arSession: ARSession)](./init%28frame,arsession%29.md)
  Creates a room-capture view with the given AR session.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a view by deserializing from the specified coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/init(frame:))*