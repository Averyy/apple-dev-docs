# prepareForPopoverPresentation(_:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate that the popover is about to be presented.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func prepareForPopoverPresentation(_ popoverPresentationController: UIPopoverPresentationController)
```

#### Discussion

Use this method to perform any last minute customizations of the popover appearance and behavior. At the time this method is called, the popover is not yet on the screen. You can use this method to modify the configuration of the popover presentation controller or perform any other actions that your app requires.

## Parameters

- `popoverPresentationController`: The popover presentation controller that is about to display the popover.

## See Also

- [func popoverPresentationControllerShouldDismissPopover(UIPopoverPresentationController) -> Bool](uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollershoulddismisspopover(_:).md)
  Asks the delegate if the popover should be dismissed.
- [func popoverPresentationControllerDidDismissPopover(UIPopoverPresentationController)](uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollerdiddismisspopover(_:).md)
  Tells the delegate that the popover was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/prepareforpopoverpresentation(_:))*