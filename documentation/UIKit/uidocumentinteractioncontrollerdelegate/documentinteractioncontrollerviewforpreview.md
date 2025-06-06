# documentInteractionControllerViewForPreview(_:)

**Framework**: UIKit  
**Kind**: method

Called when a document interaction controller needs the starting point for animating the display of a document preview.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionControllerViewForPreview(_ controller: UIDocumentInteractionController) -> UIView?
```

#### Return Value

The view to use as the starting point for the animation or `nil` if you want the document preview to fade into place.

#### Discussion

By default, the starting rectangle for the animation is set to the bounds of the returned view. To specify a different starting rectangle, you must also override the [`documentInteractionControllerRectForPreview(_:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview(_:).md) method.

## Parameters

- `controller`: The document interaction controller requesting the starting view.

## See Also

- [func documentInteractionControllerViewControllerForPreview(UIDocumentInteractionController) -> UIViewController](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview(_:).md)
  Called when a document interaction controller needs a view controller for presenting a document preview.
- [func documentInteractionControllerRectForPreview(UIDocumentInteractionController) -> CGRect](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview(_:).md)
  Called when a document interaction controller needs the rectangle to use as the starting point for animating the display of a document preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(_:))*