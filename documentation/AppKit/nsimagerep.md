# NSImageRep

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A semiabstract superclass that provides subclasses that you use to draw an image from a particular type of source data.

**Availability**:
- macOS

## Declaration

```swift
class NSImageRep
```

```objc
@interface NSImageRep : NSObject
```

#### Overview

The [`NSImageRep`](./nsimagerep.md) class is called “semiabstract” because it has some instance variables and implementation of its own, in addition to defining subclasses. Although an [`NSImageRep`](./nsimagerep.md) subclass can be used directly, it is typically accessed through an [`NSImage`](./nsimage.md) object, which manages a group of image representations, choosing the best one for the current output device.

## Topics

### Creating Representations of Images
- [class func imageReps(withContentsOfFile: String) -> [NSImageRep]?](./nsimagerep/imagereps%28withcontentsoffile%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the specified file.
- [class func imageReps(with: NSPasteboard) -> [NSImageRep]?](./nsimagerep/imagereps%28with%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the pasteboard.
- [class func imageReps(withContentsOf: URL) -> [NSImageRep]?](./nsimagerep/imagereps%28withcontentsof%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the specified URL.
- [init?(contentsOfFile: String)](./nsimagerep/init%28contentsoffile%29.md)
  Creates and returns an image representation object using the contents of the specified file.
- [init?(pasteboard: NSPasteboard)](./nsimagerep/init%28pasteboard%29.md)
  Creates and returns an image representation object using the contents of the specified pasteboard.
- [init?(contentsOf: URL)](./nsimagerep/init%28contentsof%29.md)
  Creates and returns an image representation object using the data at the specified URL.
- [init()](./nsimagerep/init%28%29.md)
  Creates and returns an image representation object.
- [init?(coder: NSCoder)](./nsimagerep/init%28coder%29.md)
  Creates and returns an image representation object from data in an unarchiver.
### Determining Types for Images
- [class func canInit(with: Data) -> Bool](./nsimagerep/caninit%28with%29-6zv56.md)
  Returns a Boolean value that indicates whether the image representation can initialize itself from the specified data.
- [class func canInit(with: NSPasteboard) -> Bool](./nsimagerep/caninit%28with%29-56pum.md)
  Returns a Boolean value that indicates whether the receiver can initialize itself from the data on the specified pasteboard.
- [class var imageTypes: [String]](./nsimagerep/imagetypes.md)
  Returns an array of UTI strings identifying the image types supported by the image representation, either directly or through a user-installed filter service.
- [class var imageUnfilteredTypes: [String]](./nsimagerep/imageunfilteredtypes.md)
  Returns an array of UTI strings identifying the image types supported directly by the ime representation.
### Accessing Size of Images
- [var size: NSSize](./nsimagerep/size.md)
  The size of the image representation, measured in points in the user coordinate space.
### Specifying Information About the Representation
- [var bitsPerSample: Int](./nsimagerep/bitspersample.md)
  The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).
- [var colorSpaceName: NSColorSpaceName](./nsimagerep/colorspacename.md)
  The name of the color space used by the image data.
- [var hasAlpha: Bool](./nsimagerep/hasalpha.md)
  A Boolean value that indicates whether the image data has an alpha channel.
- [var isOpaque: Bool](./nsimagerep/isopaque.md)
  A Boolean value that indicates whether the image is opaque.
- [var pixelsHigh: Int](./nsimagerep/pixelshigh.md)
  The height of the image, measured in pixels.
- [var pixelsWide: Int](./nsimagerep/pixelswide.md)
  The width of the image, measured in pixels.
- [var layoutDirection: NSImage.LayoutDirection](./nsimagerep/layoutdirection.md)
  The layout direction for the image.
- [Device-Specific Value](./device-specific-value.md)
  A constant that is used by image representations to denote an attribute whose value changes to match the display device.
### Getting Core Graphics Images
- [func cgImage(forProposedRect: UnsafeMutablePointer<NSRect>?, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> CGImage?](./nsimagerep/cgimage%28forproposedrect,context,hints%29.md)
  Returns a Core Graphics image object that captures the drawing of the image.
### Drawing Images
- [func draw() -> Bool](./nsimagerep/draw%28%29.md)
  Implemented by subclasses to draw the image in the current coordinate system.
- [func draw(at: NSPoint) -> Bool](./nsimagerep/draw%28at%29.md)
  Draws the image representation’s image data at the specified point in the current coordinate system.
- [func draw(in: NSRect) -> Bool](./nsimagerep/draw%28in%29.md)
  Draws the image, scaling it (as needed) to fit the specified rectangle.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?) -> Bool](./nsimagerep/draw%28in,from,operation,fraction,respectflipped,hints%29.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [NSImageRep.HintKey](./nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.
### Managing Representation Subclasses of Images
- [class func `class`(forType: String) -> AnyClass?](./nsimagerep/class%28fortype%29.md)
  Returns the image representation subclass that handles image data for the specified UTI.
- [class func `class`(for: Data) -> AnyClass?](./nsimagerep/class%28for%29.md)
  Returns the image representation subclass that handles the specified type of data.
- [class var registeredClasses: [AnyClass]](./nsimagerep/registeredclasses.md)
  Returns an array containing the registered image representation classes.
- [class func registerClass(AnyClass)](./nsimagerep/registerclass%28_%29.md)
  Adds the specified class to the registry of available image representation subclasses.
- [class func unregisterClass(AnyClass)](./nsimagerep/unregisterclass%28_%29.md)
  Removes the specified image representation subclass from the registry of available image representations.
### Notifications
- [class let registryDidChangeNotification: NSNotification.Name](./nsimagerep/registrydidchangenotification.md)
  Posted whenever the image representation class registry changes.
- [NSImageRepRegistryChangedNotification](./nsimagerepregistrychangednotification.md)
  Posted whenever the image representation class registry changes.
### Deprecated
- [Deprecated symbols](./nsimagerep-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Structures
- [NSImageRep.RegistryDidChangeMessage](./nsimagerep/registrydidchangemessage.md)
### Initializers
- [init?(contentsOfURL: URL)](./nsimagerep/init%28contentsofurl%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSBitmapImageRep](./nsbitmapimagerep.md)
- [NSCIImageRep](./nsciimagerep.md)
- [NSCustomImageRep](./nscustomimagerep.md)
- [NSEPSImageRep](./nsepsimagerep.md)
- [NSPDFImageRep](./nspdfimagerep.md)
- [NSPICTImageRep](./nspictimagerep.md)
- [NSCachedImageRep](./nscachedimagerep.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Images
- [Providing images for different appearances](../UIKit/providing-images-for-different-appearances.md)
  Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Supporting Continuity Camera in Your Mac App](./supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [Supporting HDR images in your app](../UIKit/supporting-hdr-images-in-your-app.md)
  ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [Applying Apple HDR effect to your photos](./applying-apple-hdr-effect-to-your-photos.md)
  You can decode and apply Apple’s HDR gain map to your own images.
- [class NSImage](./nsimage.md)
  A high-level interface for manipulating image data.
- [protocol NSImageDelegate](./nsimagedelegate.md)
  A set of optional methods that you can use to respond to drawing failures and manage incremental loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep)*