# previewControllerWillDismiss(_:)

**Framework**: Quick Look  
**Kind**: method

Tells the delegate that the preview is about to close.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func previewControllerWillDismiss(_ controller: QLPreviewController)
```

## Parameters

- `controller`: The   that’s about to close.

## See Also

- [func previewController(QLPreviewController, frameFor: any QLPreviewItem, inSourceView: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect](qlpreviewcontrollerdelegate/previewcontroller(_:framefor:insourceview:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a zoom effect.
- [func previewController(QLPreviewController, transitionImageFor: any QLPreviewItem, contentRect: UnsafeMutablePointer<CGRect>) -> UIImage?](qlpreviewcontrollerdelegate/previewcontroller(_:transitionimagefor:contentrect:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewController(QLPreviewController, transitionViewFor: any QLPreviewItem) -> UIView?](qlpreviewcontrollerdelegate/previewcontroller(_:transitionviewfor:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewControllerDidDismiss(QLPreviewController)](qlpreviewcontrollerdelegate/previewcontrollerdiddismiss(_:).md)
  Tells the delegate that the preview was closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/previewcontrollerwilldismiss(_:))*