# previewControllerDidDismiss(_:)

**Framework**: Quick Look  
**Kind**: method

Tells the delegate that the preview was closed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func previewControllerDidDismiss(_ controller: QLPreviewController)
```

## Parameters

- `controller`: The   that just closed.

## See Also

- [func previewController(QLPreviewController, frameFor: any QLPreviewItem, inSourceView: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect](qlpreviewcontrollerdelegate/previewcontroller(_:framefor:insourceview:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a zoom effect.
- [func previewController(QLPreviewController, transitionImageFor: any QLPreviewItem, contentRect: UnsafeMutablePointer<CGRect>) -> UIImage?](qlpreviewcontrollerdelegate/previewcontroller(_:transitionimagefor:contentrect:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewController(QLPreviewController, transitionViewFor: any QLPreviewItem) -> UIView?](qlpreviewcontrollerdelegate/previewcontroller(_:transitionviewfor:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewControllerWillDismiss(QLPreviewController)](qlpreviewcontrollerdelegate/previewcontrollerwilldismiss(_:).md)
  Tells the delegate that the preview is about to close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/previewcontrollerdiddismiss(_:))*