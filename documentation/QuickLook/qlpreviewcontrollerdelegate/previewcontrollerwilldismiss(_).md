# previewControllerWillDismiss(_:)

**Framework**: Quick Look  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) previewControllerWillDismiss:(QLPreviewController *) controller;
```

## Parameters

- `controller`: The [`QLPreviewController`](../qlpreviewcontroller.md) that’s about to close.

## See Also

### Responding to preview requests
- [func previewController(QLPreviewController, frameFor: any QLPreviewItem, inSourceView: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect](./previewcontroller%28_,framefor,insourceview%29.md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a zoom effect.
- [func previewController(QLPreviewController, transitionImageFor: any QLPreviewItem, contentRect: UnsafeMutablePointer<CGRect>) -> UIImage?](./previewcontroller%28_,transitionimagefor,contentrect%29.md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewController(QLPreviewController, transitionViewFor: any QLPreviewItem) -> UIView?](./previewcontroller%28_,transitionviewfor%29.md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewControllerDidDismiss(QLPreviewController)](./previewcontrollerdiddismiss%28_%29.md)
  Tells the delegate that the preview was closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/previewcontrollerwilldismiss(_:))*