# traitCollectionDidChange(_:)

**Framework**: RoomPlan  
**Kind**: method

Notifies the view when the device orientation changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?)
```

#### Overview

This property inherits from [`UIView`](https://developer.apple.com/documentation/UIKit/UIView).

## Parameters

- `previousTraitCollection`: The prior state of the trait collection before the change occurs.

## See Also

- [var subviews: [UIView]](roomcaptureview/subviews.md)
  An array that contains the view’s subviews.
- [func layoutSubviews()](roomcaptureview/layoutsubviews.md)
  Instructs the view’s subviews to position within the view.
- [func encode(with: NSCoder)](roomcaptureview/encode(with:).md)
  Serializes the view to the specified coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/traitcollectiondidchange(_:))*