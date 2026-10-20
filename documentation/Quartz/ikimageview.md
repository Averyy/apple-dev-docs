# IKImageView

**Framework**: Quartz  
**Kind**: class  
**Role**: Class

A view that allows displaying and minor editing of an image.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IKImageView
```

```objc
@interface IKImageView : NSView
```

#### Overview

The `IKImageView` class provides an efficient way to display images in a view while at the same time supporting a number of image editing operations such as rotating, zooming, and cropping. If possible, image rendering uses hardware acceleration to achieve optimal performance. The `IKImageView` class is implemented as a subclass of [`NSView`](../AppKit/nsview.md). Similar to [`NSImageView`](../AppKit/nsimageview.md), the `IKImageView` class is used to display a single image.

You can provide an images for the view in any of these formats:

- File reference ([`NSURL`](../Foundation/nsurl.md), [`CFURL`](../CoreFoundation/cfurl.md), or a path)
- [`CGImageSource`](../ImageIO/cgimagesource.md)
- Data ([`NSData`](../Foundation/nsdata.md) or [`CFData`](../CoreFoundation/cfdata.md))
- Image ([`CGImage`](../CoreGraphics/cgimage.md) or [`CIImage`](../CoreImage/ciimage.md))

Providing a file reference is the preferred way to set the the image for a view because in addition to the actual image data, `IKImageView` also handles the image metadata embedded in the file. The image view automatically fetches the metadata from a file reference, whereas for the other sources (except for a [`CGImageSource`](../ImageIO/cgimagesource.md) source), it cannot. For images set from other sources, you need to set the metadata separately.

`IKImageView` supports multi-frame images (TIFF, GIF, and so forth) and animated images.

## Topics

### Getting and Setting Image View Characteristics
- [var delegate: AnyObject!](./ikimageview/delegate.md)
  Specifies the delegate object of the receiver.
- [var zoomFactor: CGFloat](./ikimageview/zoomfactor.md)
  Specifies the zoom factor for the image view.
- [var rotationAngle: CGFloat](./ikimageview/rotationangle.md)
  Specifies the rotation angle for the image view.
- [var currentToolMode: String!](./ikimageview/currenttoolmode.md)
  Specifies the current tool mode for the image view.
- [var autoresizes: Bool](./ikimageview/autoresizes.md)
  Specifies the automatic resizing state for the image view.
- [var hasHorizontalScroller: Bool](./ikimageview/hashorizontalscroller.md)
  Specifies the horizontal scroll bar state for the image view.
- [var hasVerticalScroller: Bool](./ikimageview/hasverticalscroller.md)
  Specifies the vertical scroll bar state for the image view.
- [var autohidesScrollers: Bool](./ikimageview/autohidesscrollers.md)
  Specifies the automatic-hiding scroll bar state for the image view.
- [var supportsDragAndDrop: Bool](./ikimageview/supportsdraganddrop.md)
  Specifies the drag-and-drop support state for the image view.
- [var editable: Bool](./ikimageview/editable.md)
  Specifies the editable state for the image view.
- [var doubleClickOpensImageEditPanel: Bool](./ikimageview/doubleclickopensimageeditpanel.md)
  Specifies the image-opening state of the editing pane in the image view.
- [var imageCorrection: CIFilter!](./ikimageview/imagecorrection.md)
  Specifies a Core Image filter for image correction.
- [var backgroundColor: NSColor!](./ikimageview/backgroundcolor.md)
  Specifies the background color for the image view.
- [func imageSize() -> NSSize](./ikimageview/imagesize%28%29.md)
  Returns the size of the image in the image view.
- [func imageProperties() -> [AnyHashable : Any]!](./ikimageview/imageproperties%28%29.md)
  Returns the metadata for the image in the view.
### Getting and Setting Images
- [func image() -> Unmanaged<CGImage>!](./ikimageview/image%28%29.md)
  Returns the image associated with the view, after any image corrections.
- [func setImage(CGImage!, imageProperties: [AnyHashable : Any]!)](./ikimageview/setimage%28_,imageproperties%29.md)
  Sets the image to display in an image view.
- [func setImageWith(URL!)](./ikimageview/setimagewith%28_%29.md)
  Initializes an image view with the image specified by a URL.
### Manipulating the Image in a View
- [func setRotationAngle(CGFloat, center: NSPoint)](./ikimageview/setrotationangle%28_,center%29.md)
  Sets the rotation angle at the provided origin.
- [func setImageZoomFactor(CGFloat, center: NSPoint)](./ikimageview/setimagezoomfactor%28_,center%29.md)
  Sets the zoom factor at the provided origin.
- [func zoomImageToFit(Any!)](./ikimageview/zoomimagetofit%28_%29.md)
  Zooms the image so that it fits in the image view.
- [func zoomImageToActualSize(Any!)](./ikimageview/zoomimagetoactualsize%28_%29.md)
  Zooms the image so that it is displayed using its true size.
- [func zoomImage(to: NSRect)](./ikimageview/zoomimage%28to%29.md)
  Zooms the image so that it fits in the specified rectangle.
- [func zoomIn(Any!)](./ikimageview/zoomin%28_%29.md)
  Zooms the image in.
- [func zoomOut(Any!)](./ikimageview/zoomout%28_%29.md)
  Zooms the image out.
- [func crop(Any!)](./ikimageview/crop%28_%29.md)
  Crops the image using the current selection.
- [func flipImageHorizontal(Any!)](./ikimageview/flipimagehorizontal%28_%29.md)
  Flips an image along the horizontal axis.
- [func flipImageVertical(Any!)](./ikimageview/flipimagevertical%28_%29.md)
  Flips an image along the vertical axis.
- [func rotateImageLeft(Any!)](./ikimageview/rotateimageleft%28_%29.md)
  Rotates the image left (counter-clockwise).
- [func rotateImageRight(Any!)](./ikimageview/rotateimageright%28_%29.md)
  Rotates the image right (clockwise).
### Working With Core Animation
- [func setOverlay(CALayer!, forType: String!)](./ikimageview/setoverlay%28_,fortype%29.md)
  Sets an overlay type for a Core Animation layer.
- [func overlay(forType: String!) -> CALayer!](./ikimageview/overlay%28fortype%29.md)
  Returns the Core Animation layer associated with a layer type.
### Scrolling
- [func scroll(to: NSPoint)](./ikimageview/scroll%28to%29-myqk.md)
  Scrolls the view to the specified point.
- [func scroll(to: NSRect)](./ikimageview/scroll%28to%29-535q6.md)
  Scrolls the view so that it includes the provided rectangular area.
### Converting Points and Rectangles
- [func convertPoint(toImagePoint: NSPoint) -> NSPoint](./ikimageview/convertpoint%28toimagepoint%29.md)
  Converts an image view coordinate to an image coordinate.
- [func convertRect(toImageRect: NSRect) -> NSRect](./ikimageview/convertrect%28toimagerect%29.md)
  Converts an image view rectangle to an image rectangle.
- [func convertImagePoint(toViewPoint: NSPoint) -> NSPoint](./ikimageview/convertimagepoint%28toviewpoint%29.md)
  Converts an image coordinate to an image view coordinate.
- [func convertImageRect(toViewRect: NSRect) -> NSRect](./ikimageview/convertimagerect%28toviewrect%29.md)
  Converts an image rectangle to an image view rectangle.
### Constants
- [Tool Modes](./tool-modes.md)
  Image Kit tools modes referenced by the [`currentToolMode`](./ikimageview/currenttoolmode.md) property.
- [Overlay Types](./overlay-types.md)
  A layer level.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class IKCameraDeviceView](./ikcameradeviceview.md)
  The `IKCameraDeviceView` class displays the contents of the selected camera.
- [class IKDeviceBrowserView](./ikdevicebrowserview.md)
  The `IKDeviceBrowserView` allows you to select a camera or scanner from a list of the available devices.
- [class IKFilterBrowserPanel](./ikfilterbrowserpanel.md)
  Presents a user interface for browsing filters.
- [class IKFilterBrowserView](./ikfilterbrowserview.md)
  The `IKFilterBrowserView` class is used as a container for the elements of an [`IKFilterBrowserPanel`](./ikfilterbrowserpanel.md) object.
- [class IKFilterUIView](./ikfilteruiview.md)
  Input parameters for filtering core image filters.
- [class IKImageBrowserCell](./ikimagebrowsercell.md)
  A class used to display a cell.
- [class IKImageEditPanel](./ikimageeditpanel.md)
  The `IKImageEditPanel` class provides a panel, that is, a utility window that floats on top of document windows, optimized for image editing.
- [class IKPictureTaker](./ikpicturetaker.md)
  The `IKPictureTaker` class represents a panel that allows users to choose images by browsing the file system. The picture taker panel provides an Open Recent menu, supports image cropping, and supports taking snapshots from an iSight or other digital camera.
- [class IKSaveOptions](./iksaveoptions.md)
  The `IKSaveOptions` class initializes, adds, and manages user interface options for saving image data.
- [class IKScannerDeviceView](./ikscannerdeviceview.md)
  The `IKScannerDeviceView` class displays a view that allows scanning. It can be customized by specifying the display mode. The delegate receives the scanned data and must implement the [`IKScannerDeviceViewDelegate`](./ikscannerdeviceviewdelegate.md) protocol.
- [class IKSlideshow](./ikslideshow.md)
  The `IKSlideshow` class encapsulates a data source and options for a slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview)*