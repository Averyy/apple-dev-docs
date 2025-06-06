# delegate

**Framework**: UIKit  
**Kind**: property

The delegate that handles popover-related messages.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIPopoverPresentationControllerDelegate)? { get set }
```

#### Discussion

At various points during the presentation process, the popover presentation controller calls methods of its delegate to give that object a chance to respond. You might use a delegate to further configure the popover presentation controller or to respond to user-initiated actions relating to the popover. For example, immediately prior to displaying the popover, the presentation controller calls the [`prepareForPopoverPresentation(_:)`](uipopoverpresentationcontrollerdelegate/prepareforpopoverpresentation(_:).md) method of the delegate object.

For more information about the methods that you can implement in your delegate object, see [`UIPopoverPresentationControllerDelegate`](uipopoverpresentationcontrollerdelegate.md).

## See Also

- [protocol UIPopoverPresentationControllerDelegate](uipopoverpresentationcontrollerdelegate.md)
  The interface for a popover presentation delegate, which lets you customize the behavior of a popover-based presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/delegate)*