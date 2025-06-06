# previewController(_:transitionViewFor:)

**Framework**: Quick Look  
**Kind**: method

Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func previewController(_ controller: QLPreviewController, transitionViewFor item: any QLPreviewItem) -> UIView?
```

#### Return Value

A [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) object that the preview controller cross-fades with when zooming.

#### Discussion

Starting with macOS 11, animated transitions are available for Mac apps built with Mac Catalyst. On Mac computers running a version earlier than macOS 11, the system doesn’t call this delegate method.

## Parameters

- `controller`: The   that’s requesting the view for the preview item.
- `item`: The item to preview or dismiss.

## See Also

- [func previewController(QLPreviewController, frameFor: any QLPreviewItem, inSourceView: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect](qlpreviewcontrollerdelegate/previewcontroller(_:framefor:insourceview:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a zoom effect.
- [func previewController(QLPreviewController, transitionImageFor: any QLPreviewItem, contentRect: UnsafeMutablePointer<CGRect>) -> UIImage?](qlpreviewcontrollerdelegate/previewcontroller(_:transitionimagefor:contentrect:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewControllerWillDismiss(QLPreviewController)](qlpreviewcontrollerdelegate/previewcontrollerwilldismiss(_:).md)
  Tells the delegate that the preview is about to close.
- [func previewControllerDidDismiss(QLPreviewController)](qlpreviewcontrollerdelegate/previewcontrollerdiddismiss(_:).md)
  Tells the delegate that the preview was closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/previewcontroller(_:transitionviewfor:))*