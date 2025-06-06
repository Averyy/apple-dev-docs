# delegate

**Framework**: UIKit  
**Kind**: property

The delegate object for managing adaptive presentations.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIAdaptivePresentationControllerDelegate)? { get set }
```

#### Discussion

When the app’s size changes, the presentation controller works with this delegate object to determine an appropriate response. View controllers presented using the [`UIModalPresentationStyle.formSheet`](uimodalpresentationstyle/formsheet.md), [`UIModalPresentationStyle.popover`](uimodalpresentationstyle/popover.md), or [`UIModalPresentationStyle.custom`](uimodalpresentationstyle/custom.md) style must change to use one of the full-screen presentation styles instead. The delegate can also opt to change the presented view controller entirely.

The object you assign to this property must conform to the [`UIAdaptivePresentationControllerDelegate`](uiadaptivepresentationcontrollerdelegate.md) protocol.

## See Also

- [protocol UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/delegate)*