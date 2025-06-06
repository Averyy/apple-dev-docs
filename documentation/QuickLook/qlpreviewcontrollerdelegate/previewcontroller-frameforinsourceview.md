# previewController(_:frameFor:inSourceView:)

**Framework**: Quick Look  
**Kind**: method

Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a zoom effect.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func previewController(_ controller: QLPreviewController, frameFor item: any QLPreviewItem, inSourceView view: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect
```

#### Return Value

A [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) object defining the frame rectangle for the preview item as it appears in your app.

#### Discussion

Use this delegate method to configure a zoom animation for presenting and dismissing a preview. The zoom proceeds between your own representation of the item and full screen.

> **Note**:  Starting with macOS 11, animated transitions are available for Mac apps built with Mac Catalyst. On Mac computers running a version earlier than macOS 11, the system doesn’t call this delegate method.

 Starting with macOS 11, animated transitions are available for Mac apps built with Mac Catalyst. On Mac computers running a version earlier than macOS 11, the system doesn’t call this delegate method.

The system only invokes this method when your app uses the animation option for presentation or dismissal. Specifically, the following statements result in invocation of this method:

```objc
[parentController presentModaViewController: myPreviewController animated: YES];
 // ...
[parentController dismissModalViewControllerAnimated: YES];
```

If you use Boolean [`false`](https://developer.apple.com/documentation/swift/false) in these statements, the [`QLPreviewController`](qlpreviewcontroller.md) displays the preview full screen immediately, with no transition effect.

The preview item, and its origin point, can change while displaying a preview. For example, the user may navigate to a different item using the controller, or may rotate the device. Return the correct origin point when zooming to full screen, and when zooming back to your representation of the item.

> **Note**:  Zoom animation is most effective on large-screen devices. On iPhone and iPod touch, use a [`UINavigationController`](https://developer.apple.com/documentation/UIKit/UINavigationController) object to push the [`QLPreviewController`](qlpreviewcontroller.md) into view. When using a navigation controller to push a preview, the system doesn’t invoke this method.

 Zoom animation is most effective on large-screen devices. On iPhone and iPod touch, use a [`UINavigationController`](https://developer.apple.com/documentation/UIKit/UINavigationController) object to push the [`QLPreviewController`](qlpreviewcontroller.md) into view. When using a navigation controller to push a preview, the system doesn’t invoke this method.

To produce a zoom animation, return a [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) object that represents the frame for the preview item as it appears in your app. Use coordinates relative to the [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) object that contains the item, and specify that view in the `view` parameter.

Alternatively, you can use screen coordinates for the returned [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) object. In this case, you need to specify [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) in the `view` parameter.

To produce a full-screen fade animation rather than a zoom, return a value of [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero), or don’t implement this method.

## Parameters

- `controller`: The   that’s requesting the frame for the preview item.
- `item`: The item to preview or dismiss.
- `view`: Provide   in this parameter to indicate that you’re specifying the   origin point in screen coordinates.

## See Also

- [func previewController(QLPreviewController, transitionImageFor: any QLPreviewItem, contentRect: UnsafeMutablePointer<CGRect>) -> UIImage?](qlpreviewcontrollerdelegate/previewcontroller(_:transitionimagefor:contentrect:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewController(QLPreviewController, transitionViewFor: any QLPreviewItem) -> UIView?](qlpreviewcontrollerdelegate/previewcontroller(_:transitionviewfor:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewControllerWillDismiss(QLPreviewController)](qlpreviewcontrollerdelegate/previewcontrollerwilldismiss(_:).md)
  Tells the delegate that the preview is about to close.
- [func previewControllerDidDismiss(QLPreviewController)](qlpreviewcontrollerdelegate/previewcontrollerdiddismiss(_:).md)
  Tells the delegate that the preview was closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/previewcontroller(_:framefor:insourceview:))*