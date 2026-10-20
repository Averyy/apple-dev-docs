# popoverPresentationControllerShouldDismissPopover(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the popover should be dismissed.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
optional func popoverPresentationControllerShouldDismissPopover(_ popoverPresentationController: UIPopoverPresentationController) -> Bool
```

```objc
- (BOOL) popoverPresentationControllerShouldDismissPopover:(UIPopoverPresentationController *) popoverPresentationController;
```

#### Return Value

[`true`](../../Swift/true.md) if the popover should be dismissed or [`false`](../../Swift/false.md) if it should not.

#### Discussion

The popover presentation controller calls this method in response to user-initiated attempts to dismiss the popover. It is not called when you dismiss the popover programmatically using the [`dismissModalViewControllerAnimated:`](../uiviewcontroller/dismissmodalviewcontrolleranimated_.md) method.

If you do not implement this method in your delegate, the default return value is assumed to be [`true`](../../Swift/true.md).

## Parameters

- `popoverPresentationController`: The popover presentation controller that is managing the popover interface.

## See Also

### Presenting and dismissing the popover
- [func prepareForPopoverPresentation(UIPopoverPresentationController)](./prepareforpopoverpresentation%28_%29.md)
  Notifies the delegate that the popover is about to be presented.
- [func popoverPresentationControllerDidDismissPopover(UIPopoverPresentationController)](./popoverpresentationcontrollerdiddismisspopover%28_%29.md)
  Tells the delegate that the popover was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollershoulddismisspopover(_:))*