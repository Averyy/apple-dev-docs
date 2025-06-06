# IKImageView

**Framework**: Quartz  
**Kind**: class

A view that allows displaying and minor editing of an image.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
class IKImageView
```

#### Overview

The `IKImageView` class provides an efficient way to display images in a view while at the same time supporting a number of image editing operations such as rotating, zooming, and cropping. If possible, image rendering uses hardware acceleration to achieve optimal performance. The `IKImageView` class is implemented as a subclass of [`NSView`](https://developer.apple.com/documentation/AppKit/NSView). Similar to [`NSImageView`](https://developer.apple.com/documentation/AppKit/NSImageView), the `IKImageView` class is used to display a single image.

You can provide an images for the view in any of these formats:

- File reference ([`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL), [`CFURL`](https://developer.apple.com/documentation/CoreFoundation/CFURL), or a path)
- [`CGImageSource`](https://developer.apple.com/documentation/ImageIO/CGImageSource)
- Data ([`NSData`](https://developer.apple.com/documentation/Foundation/NSData) or [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData))
- Image ([`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) or [`CIImage`](https://developer.apple.com/documentation/coreimage/ciimage))

Providing a file reference is the preferred way to set the the image for a view because in addition to the actual image data, `IKImageView` also handles the image metadata embedded in the file. The image view automatically fetches the metadata from a file reference, whereas for the other sources (except for a [`CGImageSource`](https://developer.apple.com/documentation/ImageIO/CGImageSource) source), it cannot. For images set from other sources, you need to set the metadata separately.

`IKImageView` supports multi-frame images (TIFF, GIF, and so forth) and animated images.

## Topics

### Getting and Setting Image View Characteristics
- [var delegate: AnyObject!](ikimageview/delegate.md)
  Specifies the delegate object of the receiver.
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
### Getting and Setting Images
- [func image() -> Unmanaged<CGImage>!](ikimageview/image.md)
  Returns the image associated with the view, after any image corrections.
- [func setImage(CGImage!, imageProperties: [AnyHashable : Any]!)](ikimageview/setimage(_:imageproperties:).md)
  Sets the image to display in an image view.
- [func setImageWith(URL!)](ikimageview/setimagewith(_:).md)
  Initializes an image view with the image specified by a URL.
### Manipulating the Image in a View
- [func setRotationAngle(CGFloat, center: NSPoint)](ikimageview/setrotationangle(_:center:).md)
  Sets the rotation angle at the provided origin.
- [func setImageZoomFactor(CGFloat, center: NSPoint)](ikimageview/setimagezoomfactor(_:center:).md)
  Sets the zoom factor at the provided origin.
- [func zoomImageToFit(Any!)](ikimageview/zoomimagetofit(_:).md)
  Zooms the image so that it fits in the image view.
- [func zoomImageToActualSize(Any!)](ikimageview/zoomimagetoactualsize(_:).md)
  Zooms the image so that it is displayed using its true size.
- [func zoomImage(to: NSRect)](ikimageview/zoomimage(to:).md)
  Zooms the image so that it fits in the specified rectangle.
- [func zoomIn(Any!)](ikimageview/zoomin(_:).md)
  Zooms the image in.
- [func zoomOut(Any!)](ikimageview/zoomout(_:).md)
  Zooms the image out.
- [func crop(Any!)](ikimageview/crop(_:).md)
  Crops the image using the current selection.
- [func flipImageHorizontal(Any!)](ikimageview/flipimagehorizontal(_:).md)
  Flips an image along the horizontal axis.
- [func flipImageVertical(Any!)](ikimageview/flipimagevertical(_:).md)
  Flips an image along the vertical axis.
- [func rotateImageLeft(Any!)](ikimageview/rotateimageleft(_:).md)
  Rotates the image left (counter-clockwise).
- [func rotateImageRight(Any!)](ikimageview/rotateimageright(_:).md)
  Rotates the image right (clockwise).
### Working With Core Animation
- [func setOverlay(CALayer!, forType: String!)](ikimageview/setoverlay(_:fortype:).md)
  Sets an overlay type for a Core Animation layer.
- [func overlay(forType: String!) -> CALayer!](ikimageview/overlay(fortype:).md)
  Returns the Core Animation layer associated with a layer type.
### Scrolling
- [func scroll(to: NSPoint)](ikimageview/scroll(to:)-myqk.md)
  Scrolls the view to the specified point.
- [func scroll(to: NSRect)](ikimageview/scroll(to:)-535q6.md)
  Scrolls the view so that it includes the provided rectangular area.
### Converting Points and Rectangles
- [func convertPoint(toImagePoint: NSPoint) -> NSPoint](ikimageview/convertpoint(toimagepoint:).md)
  Converts an image view coordinate to an image coordinate.
- [func convertRect(toImageRect: NSRect) -> NSRect](ikimageview/convertrect(toimagerect:).md)
  Converts an image view rectangle to an image rectangle.
- [func convertImagePoint(toViewPoint: NSPoint) -> NSPoint](ikimageview/convertimagepoint(toviewpoint:).md)
  Converts an image coordinate to an image view coordinate.
- [func convertImageRect(toViewRect: NSRect) -> NSRect](ikimageview/convertimagerect(toviewrect:).md)
  Converts an image rectangle to an image view rectangle.
### Constants
- [Tool Modes](tool-modes.md)
  Image Kit tools modes referenced by the [`currentToolMode`](ikimageview/currenttoolmode.md) property.
- [Overlay Types](overlay-types.md)
  A layer level.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class IKCameraDeviceView](ikcameradeviceview.md)
  The `IKCameraDeviceView` class displays the contents of the selected camera.
- [class IKDeviceBrowserView](ikdevicebrowserview.md)
  The `IKDeviceBrowserView` allows you to select a camera or scanner from a list of the available devices.
- [class IKFilterBrowserPanel](ikfilterbrowserpanel.md)
  Presents a user interface for browsing filters.
- [class IKFilterBrowserView](ikfilterbrowserview.md)
  The `IKFilterBrowserView` class is used as a container for the elements of an [`IKFilterBrowserPanel`](ikfilterbrowserpanel.md) object.
- [class IKFilterUIView](ikfilteruiview.md)
  Input parameters for filtering core image filters.
- [class IKImageBrowserCell](ikimagebrowsercell.md)
  A class used to display a cell.
- [class IKImageEditPanel](ikimageeditpanel.md)
  The `IKImageEditPanel` class provides a panel, that is, a utility window that floats on top of document windows, optimized for image editing.
- [class IKPictureTaker](ikpicturetaker.md)
  The `IKPictureTaker` class represents a panel that allows users to choose images by browsing the file system. The picture taker panel provides an Open Recent menu, supports image cropping, and supports taking snapshots from an iSight or other digital camera.
- [class IKSaveOptions](iksaveoptions.md)
  The `IKSaveOptions` class initializes, adds, and manages user interface options for saving image data.
- [class IKScannerDeviceView](ikscannerdeviceview.md)
  The `IKScannerDeviceView` class displays a view that allows scanning. It can be customized by specifying the display mode. The delegate receives the scanned data and must implement the [`IKScannerDeviceViewDelegate`](ikscannerdeviceviewdelegate.md) protocol.
- [class IKSlideshow](ikslideshow.md)
  The `IKSlideshow` class encapsulates a data source and options for a slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview)*