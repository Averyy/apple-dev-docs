# popoverPresentationControllerShouldDismissPopover(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the popover should be dismissed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func popoverPresentationControllerShouldDismissPopover(_ popoverPresentationController: UIPopoverPresentationController) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the popover should be dismissed or [`false`](https://developer.apple.com/documentation/Swift/false) if it should not.

#### Discussion

The popover presentation controller calls this method in response to user-initiated attempts to dismiss the popover. It is not called when you dismiss the popover programmatically using the [`dismissModalViewControllerAnimated:`](uiviewcontroller/dismissmodalviewcontrolleranimated:.md) method.

If you do not implement this method in your delegate, the default return value is assumed to be [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `popoverPresentationController`: The popover presentation controller that is managing the popover interface.

## See Also

- [func prepareForPopoverPresentation(UIPopoverPresentationController)](uipopoverpresentationcontrollerdelegate/prepareforpopoverpresentation(_:).md)
  Notifies the delegate that the popover is about to be presented.
- [func popoverPresentationControllerDidDismissPopover(UIPopoverPresentationController)](uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollerdiddismisspopover(_:).md)
  Tells the delegate that the popover was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollershoulddismisspopover(_:))*