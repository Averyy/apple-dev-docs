# supportsDragAndDrop

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Specifies the drag-and-drop support state for the image view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var supportsDragAndDrop: Bool { get set }
```

```objc
@property BOOL supportsDragAndDrop;
```

## See Also

### Getting and Setting Image View Characteristics
- [var delegate: AnyObject!](./delegate.md)
  Specifies the delegate object of the receiver.
- [var zoomFactor: CGFloat](./zoomfactor.md)
  Specifies the zoom factor for the image view.
- [var rotationAngle: CGFloat](./rotationangle.md)
  Specifies the rotation angle for the image view.
- [var currentToolMode: String!](./currenttoolmode.md)
  Specifies the current tool mode for the image view.
- [var autoresizes: Bool](./autoresizes.md)
  Specifies the automatic resizing state for the image view.
- [var hasHorizontalScroller: Bool](./hashorizontalscroller.md)
  Specifies the horizontal scroll bar state for the image view.
- [var hasVerticalScroller: Bool](./hasverticalscroller.md)
  Specifies the vertical scroll bar state for the image view.
- [var autohidesScrollers: Bool](./autohidesscrollers.md)
  Specifies the automatic-hiding scroll bar state for the image view.
- [var editable: Bool](./editable.md)
  Specifies the editable state for the image view.
- [var doubleClickOpensImageEditPanel: Bool](./doubleclickopensimageeditpanel.md)
  Specifies the image-opening state of the editing pane in the image view.
- [var imageCorrection: CIFilter!](./imagecorrection.md)
  Specifies a Core Image filter for image correction.
- [var backgroundColor: NSColor!](./backgroundcolor.md)
  Specifies the background color for the image view.
- [func imageSize() -> NSSize](./imagesize%28%29.md)
  Returns the size of the image in the image view.
- [func imageProperties() -> [AnyHashable : Any]!](./imageproperties%28%29.md)
  Returns the metadata for the image in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/supportsdraganddrop)*