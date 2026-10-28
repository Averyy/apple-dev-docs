# traitCollectionDidChange(_:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Notifies the view when the device orientation changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?)
```

## Overview

This property inherits from [`UIView`](../../UIKit/uiview.md).

## Parameters

- `previousTraitCollection`: The prior state of the trait collection before the change occurs.

## See Also

### Accessing view features
- [var subviews: [UIView]](./subviews.md)
  An array that contains the view’s subviews.
- [func layoutSubviews()](./layoutsubviews%28%29.md)
  Instructs the view’s subviews to position within the view.
- [func encode(with: NSCoder)](./encode%28with%29.md)
  Serializes the view to the specified coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/traitcollectiondidchange(_:))*