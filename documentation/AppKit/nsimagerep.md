# NSImageRep

**Framework**: AppKit  
**Kind**: class

A semiabstract superclass that provides subclasses that you use to draw an image from a particular type of source data.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSImageRep
```

#### Overview

The [`NSImageRep`](nsimagerep.md) class is called “semiabstract” because it has some instance variables and implementation of its own, in addition to defining subclasses. Although an [`NSImageRep`](nsimagerep.md) subclass can be used directly, it is typically accessed through an [`NSImage`](nsimage.md) object, which manages a group of image representations, choosing the best one for the current output device.

## Topics

### Creating Representations of Images
- [class func imageReps(withContentsOfFile: String) -> [NSImageRep]?](nsimagerep/imagereps(withcontentsoffile:).md)
  Creates and returns an array of image representation objects initialized using the contents of the specified file.
- [class func imageReps(with: NSPasteboard) -> [NSImageRep]?](nsimagerep/imagereps(with:).md)
  Creates and returns an array of image representation objects initialized using the contents of the pasteboard.
- [class func imageReps(withContentsOf: URL) -> [NSImageRep]?](nsimagerep/imagereps(withcontentsof:).md)
  Creates and returns an array of image representation objects initialized using the contents of the specified URL.
- [init?(contentsOfFile: String)](nsimagerep/init(contentsoffile:).md)
  Creates and returns an image representation object using the contents of the specified file.
- [init?(pasteboard: NSPasteboard)](nsimagerep/init(pasteboard:).md)
  Creates and returns an image representation object using the contents of the specified pasteboard.
- [init?(contentsOf: URL)](nsimagerep/init(contentsof:).md)
  Creates and returns an image representation object using the data at the specified URL.
- [init()](nsimagerep/init.md)
  Creates and returns an image representation object.
- [init?(coder: NSCoder)](nsimagerep/init(coder:).md)
  Creates and returns an image representation object from data in an unarchiver.
### Determining Types for Images
- [class func canInit(with: Data) -> Bool](nsimagerep/caninit(with:)-6zv56.md)
  Returns a Boolean value that indicates whether the image representation can initialize itself from the specified data.
- [class func canInit(with: NSPasteboard) -> Bool](nsimagerep/caninit(with:)-56pum.md)
  Returns a Boolean value that indicates whether the receiver can initialize itself from the data on the specified pasteboard.
- [class var imageTypes: [String]](nsimagerep/imagetypes.md)
  Returns an array of UTI strings identifying the image types supported by the image representation, either directly or through a user-installed filter service.
- [class var imageUnfilteredTypes: [String]](nsimagerep/imageunfilteredtypes.md)
  Returns an array of UTI strings identifying the image types supported directly by the ime representation.
- [class func imageFileTypes() -> [String]](nsimagerep/imagefiletypes.md)
  Returns the file types supported by the image representation class or one of its subclasses.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimagerep/imagepasteboardtypes.md)
  Returns the pasteboard types supported by the image representation class or one of its subclasses.
- [class func imageUnfilteredFileTypes() -> [String]](nsimagerep/imageunfilteredfiletypes.md)
  Returns the list of file types supported directly by the image representation.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimagerep/imageunfilteredpasteboardtypes.md)
  Returns the list of pasteboard types supported directly by the image representation.
### Accessing Size of Images
- [var size: NSSize](nsimagerep/size.md)
  The size of the image representation, measured in points in the user coordinate space.
### Specifying Information About the Representation
- [var bitsPerSample: Int](nsimagerep/bitspersample.md)
  The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).
- [var colorSpaceName: NSColorSpaceName](nsimagerep/colorspacename.md)
  The name of the color space used by the image data.
- [var hasAlpha: Bool](nsimagerep/hasalpha.md)
  A Boolean value that indicates whether the image data has an alpha channel.
- [var isOpaque: Bool](nsimagerep/isopaque.md)
  A Boolean value that indicates whether the image is opaque.
- [var pixelsHigh: Int](nsimagerep/pixelshigh.md)
  The height of the image, measured in pixels.
- [var pixelsWide: Int](nsimagerep/pixelswide.md)
  The width of the image, measured in pixels.
- [var layoutDirection: NSImage.LayoutDirection](nsimagerep/layoutdirection.md)
  The layout direction for the image.
- [Device-Specific Value](device-specific-value.md)
  A constant that is used by image representations to denote an attribute whose value changes to match the display device.
### Getting Core Graphics Images
- [func cgImage(forProposedRect: UnsafeMutablePointer<NSRect>?, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> CGImage?](nsimagerep/cgimage(forproposedrect:context:hints:).md)
  Returns a Core Graphics image object that captures the drawing of the image.
### Drawing Images
- [func draw() -> Bool](nsimagerep/draw.md)
  Implemented by subclasses to draw the image in the current coordinate system.
- [func draw(at: NSPoint) -> Bool](nsimagerep/draw(at:).md)
  Draws the image representation’s image data at the specified point in the current coordinate system.
- [func draw(in: NSRect) -> Bool](nsimagerep/draw(in:).md)
  Draws the image, scaling it (as needed) to fit the specified rectangle.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?) -> Bool](nsimagerep/draw(in:from:operation:fraction:respectflipped:hints:).md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [NSImageRep.HintKey](nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.
### Managing Representation Subclasses of Images
- [class func `class`(forType: String) -> AnyClass?](nsimagerep/class(fortype:).md)
  Returns the image representation subclass that handles image data for the specified UTI.
- [class func `class`(for: Data) -> AnyClass?](nsimagerep/class(for:).md)
  Returns the image representation subclass that handles the specified type of data.
- [class var registeredClasses: [AnyClass]](nsimagerep/registeredclasses.md)
  Returns an array containing the registered image representation classes.
- [class func registerClass(AnyClass)](nsimagerep/registerclass(_:).md)
  Adds the specified class to the registry of available image representation subclasses.
- [class func unregisterClass(AnyClass)](nsimagerep/unregisterclass(_:).md)
  Removes the specified image representation subclass from the registry of available image representations.
- [class func `class`(forFileType: String) -> AnyClass?](nsimagerep/class(forfiletype:).md)
  Returns the image representation subclass that handles data with the specified type.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](nsimagerep/class(forpasteboardtype:).md)
  Returns the image representation subclass that handles data with the specified pasteboard type.
### Notifications
- [class let registryDidChangeNotification: NSNotification.Name](nsimagerep/registrydidchangenotification.md)
  Posted whenever the image representation class registry changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSBitmapImageRep](nsbitmapimagerep.md)
- [NSCIImageRep](nsciimagerep.md)
- [NSCustomImageRep](nscustomimagerep.md)
- [NSEPSImageRep](nsepsimagerep.md)
- [NSPDFImageRep](nspdfimagerep.md)
- [NSPICTImageRep](nspictimagerep.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Providing images for different appearances](../UIKit/providing-images-for-different-appearances.md)
  Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [Supporting HDR images in your app](../UIKit/supporting-hdr-images-in-your-app.md)
  ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [Applying Apple HDR effect to your photos](applying-apple-hdr-effect-to-your-photos.md)
  You can decode and apply Apple’s HDR gain map to your own images.
- [class NSImage](nsimage.md)
  A high-level interface for manipulating image data.
- [protocol NSImageDelegate](nsimagedelegate.md)
  A set of optional methods that you can use to respond to drawing failures and manage incremental loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep)*