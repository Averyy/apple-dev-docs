# delegate

**Framework**: Quartz  
**Kind**: property

Specifies the delegate object of the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@IBOutlet
@MainActor unowned(unsafe) var delegate: AnyObject! { get set }
```

#### Discussion

An `IKImageView` object’s delegate is inserted in the responder chain after the image view itself and is informed of various actions by the image view through delegation messages.

## See Also

- [var zoomFactor: CGFloat](ikimageview/zoomfactor.md)
  Specifies the zoom factor for the image view.
- [var rotationAngle: CGFloat](ikimageview/rotationangle.md)
  Specifies the rotation angle for the image view.
- [var currentToolMode: String!](ikimageview/currenttoolmode.md)
  Specifies the current tool mode for the image view.
- [var autoresizes: Bool](ikimageview/autoresizes.md)
  Specifies the automatic resizing state for the image view.
- [var hasHorizontalScroller: Bool](ikimageview/hashorizontalscroller.md)
  Specifies the horizontal scroll bar state for the image view.
- [var hasVerticalScroller: Bool](ikimageview/hasverticalscroller.md)
  Specifies the vertical scroll bar state for the image view.
- [var autohidesScrollers: Bool](ikimageview/autohidesscrollers.md)
  Specifies the automatic-hiding scroll bar state for the image view.
- [var supportsDragAndDrop: Bool](ikimageview/supportsdraganddrop.md)
  Specifies the drag-and-drop support state for the image view.
- [var editable: Bool](ikimageview/editable.md)
  Specifies the editable state for the image view.
- [var doubleClickOpensImageEditPanel: Bool](ikimageview/doubleclickopensimageeditpanel.md)
  Specifies the image-opening state of the editing pane in the image view.
- [var imageCorrection: CIFilter!](ikimageview/imagecorrection.md)
  Specifies a Core Image filter for image correction.
- [var backgroundColor: NSColor!](ikimageview/backgroundcolor.md)
  Specifies the background color for the image view.
- [func imageSize() -> NSSize](ikimageview/imagesize.md)
  Returns the size of the image in the image view.
- [func imageProperties() -> [AnyHashable : Any]!](ikimageview/imageproperties.md)
  Returns the metadata for the image in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/delegate)*