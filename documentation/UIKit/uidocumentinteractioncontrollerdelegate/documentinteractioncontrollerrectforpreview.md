# documentInteractionControllerRectForPreview(_:)

**Framework**: UIKit  
**Kind**: method

Called when a document interaction controller needs the rectangle to use as the starting point for animating the display of a document preview.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionControllerRectForPreview(_ controller: UIDocumentInteractionController) -> CGRect
```

#### Return Value

A rectangle in the coordinate system of the view returned by the [`documentInteractionControllerViewForPreview(_:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(_:).md) method.

#### Discussion

If you do not implement the [`documentInteractionControllerViewForPreview(_:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(_:).md) method, or if you do implement it but return a `nil` value, this method is not called. If you do not implement this method, the starting rectangle is assumed to be the bounds of the view returned by the [`documentInteractionControllerViewForPreview(_:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(_:).md) method.

## Parameters

- `controller`: The document interaction controller requesting the starting rectangle.

## See Also

- [func documentInteractionControllerViewControllerForPreview(UIDocumentInteractionController) -> UIViewController](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview(_:).md)
  Called when a document interaction controller needs a view controller for presenting a document preview.
- [func documentInteractionControllerViewForPreview(UIDocumentInteractionController) -> UIView?](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(_:).md)
  Called when a document interaction controller needs the starting point for animating the display of a document preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview(_:))*