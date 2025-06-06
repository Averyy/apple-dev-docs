# NSImage

**Framework**: AppKit  
**Kind**: class

A high-level interface for manipulating image data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
class NSImage
```

#### Overview

You use instances of [`NSImage`](nsimage.md) to load existing images, create new images, and draw the resulting image data into your views. Although you use this class predominantly for image-related operations, the class itself knows little about the underlying image data. Instead, it works in conjunction with one or more image representation objects (subclasses of [`NSImageRep`](nsimagerep.md)) to manage and render the image data. For the most part, these interactions are transparent.

The  class serves many purposes, providing support for the following tasks:

- Loading images stored on disk or at a specified URL.
- Drawing images into a view or graphics context.
- Providing the contents of a [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) object.
- Creating new images based on a series of captured drawing commands.
- Producing versions of the image in a different format.

The `NSImage` class itself is capable of managing image data in a variety of formats. The specific list of formats is dependent on the version of the operating system but includes many standard formats such as TIFF, JPEG, GIF, PNG, and PDF among others. AppKit manages each format using a specific type of image representation object, whose job is to manage the actual image data. You can get a list of supported formats using the methods described in Determining Supported Types of Images.

For more information about how to use image objects in your app, see [`Cocoa Drawing Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290).

##### Using Images with Core Animation Layers

Although you can assign an `NSImage` object directly to the [`contents`](https://developer.apple.com/documentation/QuartzCore/CALayer/contents) property of a [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) object, doing so may not always yield the best results. Instead of using your image object, you can use the [`layerContents(forContentsScale:)`](nsimage/layercontents(forcontentsscale:).md) method to obtain an object that you can use for your layer’s contents. The image created by that method serves as the contents of a layer, which also supports all of the layer’s gravity modes. By contrast, the `NSImage` class supports only the [`resize`](https://developer.apple.com/documentation/QuartzCore/CALayerContentsGravity/resize), [`resizeAspect`](https://developer.apple.com/documentation/QuartzCore/CALayerContentsGravity/resizeAspect), and [`resizeAspectFill`](https://developer.apple.com/documentation/QuartzCore/CALayerContentsGravity/resizeAspectFill) modes.

Before calling the [`layerContents(forContentsScale:)`](nsimage/layercontents(forcontentsscale:).md) method, use the [`recommendedLayerContentsScale(_:)`](nsimage/recommendedlayercontentsscale(_:).md) method to get the recommended scale factor for the resulting image. The code listing below shows a typical example that uses the scale factor of a window’s backing store as the desired scale factor. From that scale factor, the code gets the scale factor for the specified image object and creates an object that you assign to the layer. You might use this code for images that fit the layer bounds precisely or for which you rely on the [`contentsGravity`](https://developer.apple.com/documentation/QuartzCore/CALayer/contentsGravity) property of the layer to position or scale the image.

Listing 1. Assigning an image to a layer

```objc
static void updateLayerWithImageInWindow1(NSImage *image, CALayer *layer, NSWindow *window) {
   CGFloat desiredScaleFactor = [window backingScaleFactor];
   CGFloat actualScaleFactor = [image recommendedLayerContentsScale:desiredScaleFactor];
 
   id layerContents = [image layerContentsForContentsScale:actualScaleFactor];
 
   [layer setContents:layerContents];
   [layer setContentsScale:actualScaleFactor];
}
```

## Topics

### Creating Images by Name
- [Configuring and displaying symbol images in your UI](../UIKit/configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [init?(named: NSImage.Name)](nsimage/init(named:).md)
  Returns the image object associated with the specified name.
- [convenience init?(systemSymbolName: String, accessibilityDescription: String?)](nsimage/init(systemsymbolname:accessibilitydescription:).md)
  Creates a symbol image with the system symbol name and accessibility description you specify.
- [convenience init?(systemSymbolName: String, variableValue: Double, accessibilityDescription: String?)](nsimage/init(systemsymbolname:variablevalue:accessibilitydescription:).md)
  Creates a symbol image with the system symbol name and variable value you specify.
- [convenience init?(symbolName: String, variableValue: Double)](nsimage/init(symbolname:variablevalue:).md)
  Creates a symbol image with the symbol name and variable value you specify.
- [convenience init?(symbolName: String, bundle: Bundle?, variableValue: Double)](nsimage/init(symbolname:bundle:variablevalue:).md)
- [convenience init(resource: ImageResource)](nsimage/init(resource:).md)
- [func setName(NSImage.Name?) -> Bool](nsimage/setname(_:).md)
  Registers the image object under the specified name.
- [func name() -> NSImage.Name?](nsimage/name.md)
  Returns the name associated with the image, if any.
- [typealias Name](nsimage/name-swift.typealias.md)
  Named images, defined by the system or you, for use in your app.
- [convenience init(imageLiteralResourceName: String)](nsimage/init(imageliteralresourcename:).md)
  Creates an image initialized with the specified resource name.
### Creating Dynamically Drawn Images
- [convenience init(size: NSSize, flipped: Bool, drawingHandler: (NSRect) -> Bool)](nsimage/init(size:flipped:drawinghandler:).md)
  Creates and returns an image object whose contents are drawn using the specified block.
### Creating Images from Resource Files
- [convenience init?(byReferencingFile: String)](nsimage/init(byreferencingfile:).md)
  Initializes and returns an image object using the specified file.
- [convenience init(byReferencing: URL)](nsimage/init(byreferencing:).md)
  Initializes and returns an image object using the specified URL.
- [convenience init?(contentsOfFile: String)](nsimage/init(contentsoffile:).md)
  Initializes and returns an image object with the contents of the specified file.
- [convenience init?(contentsOf: URL)](nsimage/init(contentsof:).md)
  Initializes and returns an image object with the contents of the specified URL.
### Creating Images from Existing Data
- [convenience init?(data: Data)](nsimage/init(data:).md)
  Initializes and returns an image object using the provided image data.
- [convenience init?(dataIgnoringOrientation: Data)](nsimage/init(dataignoringorientation:).md)
  Initializes and returns an image object using the provided image data and ignoring the EXIF orientation tags.
- [convenience init(cgImage: CGImage, size: NSSize)](nsimage/init(cgimage:size:).md)
  Creates a new image using the contents of the provided image.
- [convenience init?(pasteboard: NSPasteboard)](nsimage/init(pasteboard:).md)
  Initializes and returns an image object with data from the specified pasteboard.
- [init(coder: NSCoder)](nsimage/init(coder:).md)
  Initializes and returns an image object from data in an unarchiver.
### Creating Empty Images
- [init(size: NSSize)](nsimage/init(size:).md)
  Initializes and returns an image object with the specified dimensions.
### Creating Symbol Images
- [func withSymbolConfiguration(NSImage.SymbolConfiguration) -> NSImage?](nsimage/withsymbolconfiguration(_:).md)
  Creates a new symbol image with the specified configuration.
- [NSImage.SymbolConfiguration](nsimage/symbolconfiguration-swift.class.md)
  An object that contains the specific font, style, and weight attributes to apply to a symbol image.
### Getting the Symbol Image Configuration
- [var symbolConfiguration: NSImage.SymbolConfiguration](nsimage/symbolconfiguration-swift.property.md)
  The configuration details for a symbol image.
### Managing Loading and Drawing of Images
- [var delegate: (any NSImageDelegate)?](nsimage/delegate.md)
  The image’s delegate object.
- [protocol NSImageDelegate](nsimagedelegate.md)
  A set of optional methods that you can use to respond to drawing failures and manage incremental loads.
### Setting Attributes of Images
- [var size: NSSize](nsimage/size.md)
  The size of the image.
- [var isTemplate: Bool](nsimage/istemplate.md)
  A Boolean value that determines whether the image represents a template image.
- [var isTemplate: Bool](nsimage/istemplate.md)
  A Boolean value that determines whether the image represents a template image.
### Determining Supported Types of Images
- [class func canInit(with: NSPasteboard) -> Bool](nsimage/caninit(with:).md)
  Tests whether the image can create an instance of itself using pasteboard data.
- [class var imageTypes: [String]](nsimage/imagetypes.md)
  Returns an array of UTI strings identifying the image types supported by the registered image representation objects, either directly or through a user-installed filter service.
- [class var imageUnfilteredTypes: [String]](nsimage/imageunfilteredtypes.md)
  Returns an array of UTI strings identifying the image types supported directly by the registered image representation objects.
### Working with Representations of Images
- [func addRepresentation(NSImageRep)](nsimage/addrepresentation(_:).md)
  Adds the specified image representation object to the image.
- [func addRepresentations([NSImageRep])](nsimage/addrepresentations(_:).md)
  Adds an array of image representation objects to the image.
- [var representations: [NSImageRep]](nsimage/representations.md)
  An array containing all of the image object’s image representations.
- [func removeRepresentation(NSImageRep)](nsimage/removerepresentation(_:).md)
  Removes and releases the specified image representation.
- [func bestRepresentation(for: NSRect, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> NSImageRep?](nsimage/bestrepresentation(for:context:hints:).md)
  Returns the best representation of the image for the specified rectangle using the provided hints.
- [NSImageRep.HintKey](nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.
- [NSImage.LayoutDirection](nsimage/layoutdirection.md)
  Constants that describe the layout direction for the image.
### Setting the Representation Selection Criteria for Images
- [var prefersColorMatch: Bool](nsimage/preferscolormatch.md)
  A Boolean value that indicates whether the image prefers to choose image representations using color-matching or resolution-matching.
- [var usesEPSOnResolutionMismatch: Bool](nsimage/usesepsonresolutionmismatch.md)
  A Boolean value that indicates whether EPS representations are preferred when no other representations match the resolution of the device.
- [var matchesOnMultipleResolution: Bool](nsimage/matchesonmultipleresolution.md)
  A Boolean value that indicates whether image representations whose resolution is an integral multiple of the device resolution are a match.
### Drawing Images
- [func draw(in: NSRect)](nsimage/draw(in:).md)
  Draws the image in the specified rectangle.
- [func draw(at: NSPoint, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](nsimage/draw(at:from:operation:fraction:).md)
  Draws all or part of the image at the specified point in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](nsimage/draw(in:from:operation:fraction:).md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?)](nsimage/draw(in:from:operation:fraction:respectflipped:hints:).md)
  Draws all or part of the image in the specified rectangle respecting the hints and the orientation of the current coordinate system.
- [func drawRepresentation(NSImageRep, in: NSRect) -> Bool](nsimage/drawrepresentation(_:in:).md)
  Draws the image using the specified image representation object.
- [enum NSCompositingOperation](nscompositingoperation.md)
  Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.
### Managing Drawing Options
- [var isValid: Bool](nsimage/isvalid.md)
  A Boolean value that indicates whether it is possible to draw an image representation.
- [var backgroundColor: NSColor](nsimage/backgroundcolor.md)
  The background color for the image.
- [var capInsets: NSEdgeInsets](nsimage/capinsets.md)
  The cap insets for the image.
- [var resizingMode: NSImage.ResizingMode](nsimage/resizingmode-swift.property.md)
  The resizing mode for the image.
- [NSImage.ResizingMode](nsimage/resizingmode-swift.enum.md)
  Constants that describe the resizing mode for the image.
### Working with Alignment Metadata
- [var alignmentRect: NSRect](nsimage/alignmentrect.md)
  A rectangle that you can use to position the image during layout.
### Managing Caching Options
- [var cacheMode: NSImage.CacheMode](nsimage/cachemode-swift.property.md)
  The image’s caching mode.
- [func recache()](nsimage/recache.md)
  Invalidates and frees offscreen caches of all image representations.
- [NSImage.CacheMode](nsimage/cachemode-swift.enum.md)
  Constants that specify the caching policy on a per-image basis.
### Producing TIFF Data for Images
- [var tiffRepresentation: Data?](nsimage/tiffrepresentation.md)
  A data object containing TIFF data for all of the image representations in the image.
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsimage/tiffrepresentation(using:factor:).md)
  Returns a data object that contains TIFF data with the specified compression settings for all of the image representations in the image.
### Producing Core Graphics Images
- [func cgImage(forProposedRect: UnsafeMutablePointer<NSRect>?, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> CGImage?](nsimage/cgimage(forproposedrect:context:hints:).md)
  Returns a Core Graphics image based on the contents of the current image object.
### Hit-Testing Images
- [func hitTest(NSRect, withDestinationRect: NSRect, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?, flipped: Bool) -> Bool](nsimage/hittest(_:withdestinationrect:context:hints:flipped:).md)
  Returns whether the destination rectangle would intersect a non-transparent portion of the image.
### Managing Image Accessibility
- [var accessibilityDescription: String?](nsimage/accessibilitydescription.md)
  The image’s accessibility description.
### Using Images with Core Animation
- [func layerContents(forContentsScale: CGFloat) -> Any](nsimage/layercontents(forcontentsscale:).md)
  Returns an object that may be used as the contents of a layer.
- [func recommendedLayerContentsScale(CGFloat) -> CGFloat](nsimage/recommendedlayercontentsscale(_:).md)
  Returns the recommended layer contents scale for this image.
### Managing Axis Matching
- [var matchesOnlyOnBestFittingAxis: Bool](nsimage/matchesonlyonbestfittingaxis.md)
  A Boolean value that indicates whether the image matches only on the best fitting axis.
### Localizing Images
- [func withLocale(Locale?) -> NSImage](nsimage/withlocale(_:).md)
- [var locale: Locale?](nsimage/locale.md)
### Deprecated
- [Deprecated Symbols](nsimage-deprecated-symbols.md)
  Review symbols that are no longer supported, and find the replacements to use instead.
### Enumerations
- [NSImage.DynamicRange](nsimage/dynamicrange.md)
  Describes how High Dynamic Range (HDR) image content displays.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSItemProviderReading](../Foundation/NSItemProviderReading.md)
- [NSItemProviderWriting](../Foundation/NSItemProviderWriting.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSPasteboardReading](nspasteboardreading.md)
- [NSPasteboardWriting](nspasteboardwriting.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Transferable](../CoreTransferable/Transferable.md)

## See Also

- [Providing images for different appearances](../UIKit/providing-images-for-different-appearances.md)
  Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [Supporting HDR images in your app](../UIKit/supporting-hdr-images-in-your-app.md)
  ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [Applying Apple HDR effect to your photos](applying-apple-hdr-effect-to-your-photos.md)
  You can decode and apply Apple’s HDR gain map to your own images.
- [protocol NSImageDelegate](nsimagedelegate.md)
  A set of optional methods that you can use to respond to drawing failures and manage incremental loads.
- [class NSImageRep](nsimagerep.md)
  A semiabstract superclass that provides subclasses that you use to draw an image from a particular type of source data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage)*