# adaptivePresentationStyle(for:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the new presentation style to use.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func adaptivePresentationStyle(for controller: UIPresentationController) -> UIModalPresentationStyle
```

#### Return Value

The new presentation style, which must be [`UIModalPresentationStyle.fullScreen`](uimodalpresentationstyle/fullscreen.md), [`UIModalPresentationStyle.overFullScreen`](uimodalpresentationstyle/overfullscreen.md), or [`UIModalPresentationStyle.none`](uimodalpresentationstyle/none.md).

#### Discussion

In iOS 8.3 and later, use the [`adaptivePresentationStyle(for:traitCollection:)`](uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:traitcollection:).md) method to handle all trait changes instead of this method. If you do not implement that method, you can use this method to change the presentation style when transitioning to a horizontally compact environment.

If you do not implement this method or if you return an invalid style, the current presentation controller returns its preferred default style.

## Parameters

- `controller`: The presentation controller that is managing the size change. Use this object to retrieve the view controllers involved in the presentation.

## See Also

- [func adaptivePresentationStyle(for: UIPresentationController, traitCollection: UITraitCollection) -> UIModalPresentationStyle](uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:traitcollection:).md)
  Asks the delegate for the presentation style to use when the specified set of traits are active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:))*