# init(coder:)

**Framework**: RoomPlan  
**Kind**: init

Creates a view by deserializing from the specified coder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency required dynamic init?(coder: NSCoder)
```

#### Overview

This property inherits from [`UIView`](https://developer.apple.com/documentation/UIKit/UIView).

## Parameters

- `coder`: An object from which the view deserializes.

## See Also

- [init(frame: CGRect, arSession: ARSession)](roomcaptureview/init(frame:arsession:).md)
  Creates a room-capture view with the given AR session.
- [init(frame: CGRect)](roomcaptureview/init(frame:).md)
  Creates a view that sizes to the specified frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/init(coder:))*