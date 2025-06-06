# adaptivePresentationStyle(for:traitCollection:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the presentation style to use when the specified set of traits are active.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func adaptivePresentationStyle(for controller: UIPresentationController, traitCollection: UITraitCollection) -> UIModalPresentationStyle
```

#### Return Value

The new presentation style, which must be [`UIModalPresentationStyle.fullScreen`](uimodalpresentationstyle/fullscreen.md), [`UIModalPresentationStyle.overFullScreen`](uimodalpresentationstyle/overfullscreen.md), [`UIModalPresentationStyle.formSheet`](uimodalpresentationstyle/formsheet.md), or [`UIModalPresentationStyle.none`](uimodalpresentationstyle/none.md).

#### Discussion

The presentation controller calls this method when the traits of the current environment are about to change. Your implementation of this method can return the preferred presentation style to use for the specified traits. If you do not return one of the allowed styles, the presentation controller uses its preferred default style.

If you do not implement this method in your delegate, UIKit calls the [`adaptivePresentationStyle(for:)`](uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:).md) method instead.

## Parameters

- `controller`: The presentation controller that is managing the size change. Use this object to retrieve the view controllers involved in the presentation.
- `traitCollection`: The traits representing the target environment.

## See Also

- [func adaptivePresentationStyle(for: UIPresentationController) -> UIModalPresentationStyle](uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:).md)
  Asks the delegate for the new presentation style to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:traitcollection:))*