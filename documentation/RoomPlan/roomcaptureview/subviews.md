# subviews

**Framework**: RoomPlan  
**Kind**: property  
**Role**: Instance Property

An array that contains the view’s subviews.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic var subviews: [UIView] { get }
```

## Overview

This property inherits from [`UIView`](../../UIKit/uiview.md).

## See Also

### Accessing view features
- [func layoutSubviews()](./layoutsubviews%28%29.md)
  Instructs the view’s subviews to position within the view.
- [func encode(with: NSCoder)](./encode%28with%29.md)
  Serializes the view to the specified coder.
- [func traitCollectionDidChange(UITraitCollection?)](./traitcollectiondidchange%28_%29.md)
  Notifies the view when the device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcaptureview/subviews)*