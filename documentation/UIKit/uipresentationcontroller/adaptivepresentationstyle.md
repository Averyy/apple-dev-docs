# adaptivePresentationStyle

**Framework**: UIKit  
**Kind**: property

Returns the presentation style to use when the presented view controller becomes horizontally compact.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var adaptivePresentationStyle: UIModalPresentationStyle { get }
```

#### Return Value

The value provided by the presentation controller’s delegate or [`UIModalPresentationStyle.none`](uimodalpresentationstyle/none.md) if a delegate was not provided or does not return a valid value.

#### Discussion

After the content managed by the presentation controller is onscreen, this method returns the presentation style to use when transitioning to a horizontally compact environment. This method is not meant to be overridden. The implementation consults its delegate object and returns the value provided by that object’s [`adaptivePresentationStyle(for:)`](uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:).md) method. Some system-supplied presentation controllers may also provide a new style that is more suited for a compact environment. For example, presentation controllers that manage popovers and form sheets return the [`UIModalPresentationStyle.fullScreen`](uimodalpresentationstyle/fullscreen.md) value.

This method only returns the presentation style to use in a horizontally compact environment. It does not initiate a transition to the new style. The system initiates the transition to the new style when the size class actually changes. When transitioning to a new style, the actual presentation controller object may change. As a result, do not cache the presentation controller object in your code. Always retrieve it from your view controller’s [`presentationController`](uiviewcontroller/presentationcontroller.md) property.

In iOS 8.3 and later, UIKit calls the [`adaptivePresentationStyle(for:)`](uipresentationcontroller/adaptivepresentationstyle(for:).md) method to retrieve presentation styles instead of this one.

## See Also

- [var presentationStyle: UIModalPresentationStyle](uipresentationcontroller/presentationstyle.md)
  The presentation style of the presented view controller.
- [func adaptivePresentationStyle(for: UITraitCollection) -> UIModalPresentationStyle](uipresentationcontroller/adaptivepresentationstyle(for:).md)
  Returns the presentation style to use for the specified set of traits.
- [var shouldPresentInFullscreen: Bool](uipresentationcontroller/shouldpresentinfullscreen.md)
  A Boolean value indicating whether the presentation covers the entire screen.
- [var shouldRemovePresentersView: Bool](uipresentationcontroller/shouldremovepresentersview.md)
  A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/adaptivepresentationstyle)*