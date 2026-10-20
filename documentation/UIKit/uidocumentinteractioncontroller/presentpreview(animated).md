# presentPreview(animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Displays a full-screen preview of the target document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func presentPreview(animated: Bool) -> Bool
```

```objc
- (BOOL) presentPreviewAnimated:(BOOL) animated;
```

#### Return Value

[`true`](../../Swift/true.md) if this method was able to display the document preview or [`false`](../../Swift/false.md) if it was not.

#### Discussion

To use this method, you must first provide a delegate object that implements the [`documentInteractionControllerViewControllerForPreview(_:)`](../uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview%28_%29.md) method. The view controller returned by that method is used to present the document preview modally.

If your delegate implements the [`documentInteractionControllerViewForPreview(_:)`](../uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview%28_%29.md) and [`documentInteractionControllerRectForPreview(_:)`](../uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview%28_%29.md) methods, the view and rectangle returned by those methods is used as the starting point for the animation used to display the document preview. If the animated parameter is [`true`](../../Swift/true.md) but your delegate does not implement the [`documentInteractionControllerViewForPreview(_:)`](../uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview%28_%29.md) method (or that method returns `nil`), the document preview is animated into place using a crossfade transition.

This method displays the document preview asynchronously. The document interaction controller dismisses the document preview automatically in response to appropriate user interactions. You can also dismiss the preview programmatically using the [`dismissPreview(animated:)`](./dismisspreview%28animated%29.md) method.

## Parameters

- `animated`: Specify [`true`](../../Swift/true.md) to animate the appearance of the document preview or [`false`](../../Swift/false.md) to display it immediately.

## See Also

### Presenting and dismissing a document preview
- [func dismissPreview(animated: Bool)](./dismisspreview%28animated%29.md)
  Dismisses the currently active document preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/presentpreview(animated:))*