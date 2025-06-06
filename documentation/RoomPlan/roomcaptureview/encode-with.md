# encode(with:)

**Framework**: RoomPlan  
**Kind**: method

Serializes the view to the specified coder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func encode(with coder: NSCoder)
```

#### Overview

This property inherits from [`UIView`](https://developer.apple.com/documentation/UIKit/UIView).

## Parameters

- `coder`: An object that the view serializes to.

## See Also

- [var subviews: [UIView]](roomcaptureview/subviews.md)
  An array that contains the view’s subviews.
- [func layoutSubviews()](roomcaptureview/layoutsubviews.md)
  Instructs the view’s subviews to position within the view.
- [func traitCollectionDidChange(UITraitCollection?)](roomcaptureview/traitcollectiondidchange(_:).md)
  Notifies the view when the device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/encode(with:))*