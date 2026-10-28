# encode(with:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Serializes the view to the specified coder.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func encode(with coder: NSCoder)
```

## Overview

This property inherits from [`UIView`](../../UIKit/uiview.md).

## Parameters

- `coder`: An object that the view serializes to.

## See Also

### Accessing view features
- [var subviews: [UIView]](./subviews.md)
  An array that contains the view’s subviews.
- [func layoutSubviews()](./layoutsubviews%28%29.md)
  Instructs the view’s subviews to position within the view.
- [func traitCollectionDidChange(UITraitCollection?)](./traitcollectiondidchange%28_%29.md)
  Notifies the view when the device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/encode(with:))*