# init(coder:)

**Framework**: RoomPlan  
**Kind**: init  
**Role**: Initializer

Creates a view by deserializing from the specified coder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
@preconcurrency required dynamic init?(coder: NSCoder)
```

## Overview

This property inherits from [`UIView`](../../UIKit/uiview.md).

## Parameters

- `coder`: An object from which the view deserializes.

## See Also

### Creating a room-capture view
- [init(frame: CGRect, arSession: ARSession)](./init%28frame,arsession%29.md)
  Creates a room-capture view with the given AR session.
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates a view that sizes to the specified frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/init(coder:))*