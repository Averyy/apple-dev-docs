# presentPreview(animated:)

**Framework**: UIKit  
**Kind**: method

Displays a full-screen preview of the target document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentPreview(animated: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if this method was able to display the document preview or [`false`](https://developer.apple.com/documentation/swift/false) if it was not.

#### Discussion

To use this method, you must first provide a delegate object that implements the [`documentInteractionControllerViewControllerForPreview(_:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview(_:).md) method. The view controller returned by that method is used to present the document preview modally.

If your delegate implements the [`documentInteractionControllerViewForPreview(_:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(_:).md) and [`documentInteractionControllerRectForPreview(_:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview(_:).md) methods, the view and rectangle returned by those methods is used as the starting point for the animation used to display the document preview. If the animated parameter is [`true`](https://developer.apple.com/documentation/swift/true) but your delegate does not implement the [`documentInteractionControllerViewForPreview(_:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(_:).md) method (or that method returns `nil`), the document preview is animated into place using a crossfade transition.

This method displays the document preview asynchronously. The document interaction controller dismisses the document preview automatically in response to appropriate user interactions. You can also dismiss the preview programmatically using the [`dismissPreview(animated:)`](uidocumentinteractioncontroller/dismisspreview(animated:).md) method.

## Parameters

- `animated`: Specify   to animate the appearance of the document preview or   to display it immediately.

## See Also

- [func dismissPreview(animated: Bool)](uidocumentinteractioncontroller/dismisspreview(animated:).md)
  Dismisses the currently active document preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/presentpreview(animated:))*