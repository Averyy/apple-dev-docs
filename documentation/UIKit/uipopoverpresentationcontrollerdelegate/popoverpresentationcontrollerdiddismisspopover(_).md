# popoverPresentationControllerDidDismissPopover(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the popover was dismissed.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
optional func popoverPresentationControllerDidDismissPopover(_ popoverPresentationController: UIPopoverPresentationController)
```

```objc
- (void) popoverPresentationControllerDidDismissPopover:(UIPopoverPresentationController *) popoverPresentationController;
```

## Discussion

The popover presentation controller calls this method after dismissing the popover to let you know that it is no longer onscreen. The presentation controller calls this method only in response to user actions. It does not call this method if you dismiss the popover programmatically.

Use this method to incorporate any changes from the popover’s content view controller back into your app.

## Parameters

- `popoverPresentationController`: The popover presentation controller that is managing the popover interface.

## See Also

### Presenting and dismissing the popover
- [func prepareForPopoverPresentation(UIPopoverPresentationController)](./prepareforpopoverpresentation%28_%29.md)
  Notifies the delegate that the popover is about to be presented.
- [func popoverPresentationControllerShouldDismissPopover(UIPopoverPresentationController) -> Bool](./popoverpresentationcontrollershoulddismisspopover%28_%29.md)
  Asks the delegate if the popover should be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollerdiddismisspopover(_:))*