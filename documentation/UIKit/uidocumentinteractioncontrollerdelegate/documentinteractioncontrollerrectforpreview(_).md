# documentInteractionControllerRectForPreview(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (CGRect) documentInteractionControllerRectForPreview:(UIDocumentInteractionController *) controller;
```

## Return Value

A rectangle in the coordinate system of the view returned by the [`documentInteractionControllerViewForPreview(_:)`](./documentinteractioncontrollerviewforpreview%28_%29.md) method.

## Discussion

If you do not implement the [`documentInteractionControllerViewForPreview(_:)`](./documentinteractioncontrollerviewforpreview%28_%29.md) method, or if you do implement it but return a `nil` value, this method is not called. If you do not implement this method, the starting rectangle is assumed to be the bounds of the view returned by the [`documentInteractionControllerViewForPreview(_:)`](./documentinteractioncontrollerviewforpreview%28_%29.md) method.

## Parameters

- `controller`: The document interaction controller requesting the starting rectangle.

## See Also

### Configuring the parent view controller
- [func documentInteractionControllerViewControllerForPreview(UIDocumentInteractionController) -> UIViewController](./documentinteractioncontrollerviewcontrollerforpreview%28_%29.md)
  Called when a document interaction controller needs a view controller for presenting a document preview.
- [func documentInteractionControllerViewForPreview(UIDocumentInteractionController) -> UIView?](./documentinteractioncontrollerviewforpreview%28_%29.md)
  Called when a document interaction controller needs the starting point for animating the display of a document preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview(_:))*