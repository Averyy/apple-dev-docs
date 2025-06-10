# previewController(_:transitionImageFor:contentRect:)

**Framework**: Quick Look  
**Kind**: method

Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func previewController(_ controller: QLPreviewController, transitionImageFor item: any QLPreviewItem, contentRect: UnsafeMutablePointer<CGRect>) -> UIImage?
```

#### Return Value

A [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) object that the preview controller cross-fades with when zooming.

#### Discussion

> **Note**:  Starting with macOS 11, animated transitions are available for Mac apps built with Mac Catalyst. On Mac computers running a version earlier than macOS 11, the system doesn’t call this delegate method.

## Parameters

- `controller`: The   that’s requesting the image for the preview item.
- `item`: The item to preview or dismiss.
- `contentRect`: The rectangle within the image that represents the document content. For icons, for example, the document content rectangle is typically smaller than the icon rectangle itself.

## See Also

- [func previewController(QLPreviewController, frameFor: any QLPreviewItem, inSourceView: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect](qlpreviewcontrollerdelegate/previewcontroller(_:framefor:insourceview:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a zoom effect.
- [func previewController(QLPreviewController, transitionViewFor: any QLPreviewItem) -> UIView?](qlpreviewcontrollerdelegate/previewcontroller(_:transitionviewfor:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewControllerWillDismiss(QLPreviewController)](qlpreviewcontrollerdelegate/previewcontrollerwilldismiss(_:).md)
  Tells the delegate that the preview is about to close.
- [func previewControllerDidDismiss(QLPreviewController)](qlpreviewcontrollerdelegate/previewcontrollerdiddismiss(_:).md)
  Tells the delegate that the preview was closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/previewcontroller(_:transitionimagefor:contentrect:))*