# UIImage

**Framework**: UIKit  
**Kind**: class

An object that manages image data in your app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class UIImage
```

## Mentions

- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md)
- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)
- [Understanding a drag item as a promise](understanding-a-drag-item-as-a-promise.md)

#### Overview

You use image objects to represent image data of all kinds, and the [`UIImage`](uiimage.md) class is capable of managing data for all image formats supported by the underlying platform. Image objects are immutable, so you always create them from existing image data, such as an image file on disk or programmatically created image data. An image object may contain a single image or a sequence of images for use in an animation.

You can use image objects in several different ways:

- Assign an image to a [`UIImageView`](uiimageview.md) object to display the image in your interface.
- Use an image to customize system controls such as buttons, sliders, and segmented controls.
- Draw an image directly into a view or other graphics context.
- Pass an image to other APIs that might require image data.

Although image objects support all platform-native image formats, it’s recommended that you use PNG or JPEG files for most images in your app. Image objects are optimized for reading and displaying both formats, and those formats offer better performance than most other image formats. Because the PNG format is lossless, it’s especially recommended for the images you use in your app’s interface.

##### Create Image Objects

When creating image objects using the methods of this class, you must have existing image data located in a file or data structure. You can’t create an empty image and draw content into it. There are many options for creating image objects, each of which is best for specific situations:

- Use the [`init(named:in:compatibleWith:)`](uiimage/init(named:in:compatiblewith:).md) method (or the [`init(named:)`](uiimage/init(named:).md) method) to create an image from an image asset or image file located in your app’s main bundle (or some other known bundle). Because these methods cache the image data automatically, they’re especially recommended for images that you use frequently.
- Use the [`imageWithContentsOfFile:`](uiimage/imagewithcontentsoffile:.md) or [`init(contentsOfFile:)`](uiimage/init(contentsoffile:).md) method to create an image object where the initial data isn’t in a bundle. These methods load the image data from disk each time, so don’t use them to load the same image repeatedly.
- Use the [`animatedImage(with:duration:)`](uiimage/animatedimage(with:duration:).md) and [`animatedImageNamed(_:duration:)`](uiimage/animatedimagenamed(_:duration:).md) methods to create a single [`UIImage`](uiimage.md) object comprised of multiple sequential images. Install the resulting image in a [`UIImageView`](uiimageview.md) object to create animations in your interface.

Other methods of the [`UIImage`](uiimage.md) class let you create animations from specific types of data, such as Core Graphics images or image data you create yourself. UIKit also provides the [`UIGraphicsGetImageFromCurrentImageContext()`](uigraphicsgetimagefromcurrentimagecontext().md) function to create images from content you draw yourself. You use that function in conjunction with a bitmap-based graphics context, which you use to capture your drawing commands.

> **Note**:  Because image objects are immutable, you can’t change their properties after creation. Most image properties are set automatically using metadata in the accompanying image file or image data. The immutable nature of image objects also means they’re safe to create and use from any thread.

Image assets are the easiest way to manage the images that ship with your app. Each new Xcode project contains an assets library, to which you can add multiple image sets. An image set contains the variations of a single image that your app uses. A single image set can provide different versions of an image for different platforms, for different trait environments (compact or regular), and for different scale factors.

In addition to loading images from disk, you can ask the user to supply images from an available camera or photo library using a [`UIImagePickerController`](uiimagepickercontroller.md) object. An image picker displays a custom user interface for selecting images. Accessing user-supplied images requires explicit user permission. For more information about using an image picker, see [`UIImagePickerController`](uiimagepickercontroller.md).

##### Define a Stretchable Image

A stretchable image is one that defines regions where you can duplicate the underlying image data in an aesthetically pleasing way. Stretchable images are commonly used to create backgrounds that can grow or shrink to fill the available space.

Define a stretchable image by adding insets to an existing image using the [`resizableImage(withCapInsets:)`](uiimage/resizableimage(withcapinsets:).md) or [`resizableImage(withCapInsets:resizingMode:)`](uiimage/resizableimage(withcapinsets:resizingmode:).md) method. The insets subdivide the image into two or more parts. Specifying nonzero values for each inset yields an image divided into nine parts, as shown in the following image:

![An image that depicts how to use insets to define stretchable regions. The image on the left is stretched and shows Left, Right, Top, and Bottom insets. The image on the right is condensed and also shows Left, Right, Top, and Bottom insets.](https://docs-assets.developer.apple.com/published/a24122a4b3a9289007f9bcad22d8667d/media-1965929%402x.png)

Each inset defines the portion of the image that doesn’t stretch in the given dimension. The regions inside an image’s top and bottom insets maintain a fixed height, and the areas inside the left and right insets maintain a fixed width. The following image shows how each part of a nine-part image stretches as the image itself is stretched to fill the available space. The corners of the image don’t change size because they’re inside both a horizontal and vertical inset:

![An image that depicts the stretchable portions of a nine-part image. The image on the left is stretched. The image on the right is condensed. The corners of both images remain the same size.](https://docs-assets.developer.apple.com/published/dcf9ad7415ffdb2dd9a753a3be251cce/media-1965930%402x.png)

##### Compare Images

The [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) method is the only reliable way to determine whether two image objects contain the same image data. The following code illustrates the correct and incorrect ways to compare images.

##### Access the Image Data

Image objects don’t provide direct access to their underlying image data. However, you can retrieve the image data in other formats for use in your app. Specifically, you can use the [`cgImage`](uiimage/cgimage.md) and [`ciImage`](uiimage/ciimage.md) properties to retrieve versions of the image that are compatible with Core Graphics and Core Image, respectively. You can also use the [`pngData()`](uiimage/pngdata().md) and [`jpegData(compressionQuality:)`](uiimage/jpegdata(compressionquality:).md) functions to generate an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object containing the image data in either the PNG or JPEG format.

## Topics

### Loading and caching images
- [Providing images for different appearances](providing-images-for-different-appearances.md)
  Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [Creating custom symbol images for your app](creating-custom-symbol-images-for-your-app.md)
  Create, organize, and annotate symbol images using SF Symbols.
- [init?(named: String, in: Bundle?, compatibleWith: UITraitCollection?)](uiimage/init(named:in:compatiblewith:).md)
  Creates an image object using the named image asset that’s compatible with the specified trait collection.
- [init?(named: String, in: Bundle?, with: UIImage.Configuration?)](uiimage/init(named:in:with:).md)
  Creates an image by using the named image asset that’s compatible with the configuration you specify.
- [convenience init?(named: String, in: Bundle?, variableValue: Double, configuration: UIImage.Configuration?)](uiimage/init(named:in:variablevalue:configuration:).md)
  Creates an image by using the name, configuration, and variable value you specify.
- [init?(named: String)](uiimage/init(named:).md)
  Creates an image object from the specified named asset.
- [convenience init(imageLiteralResourceName: String)](uiimage/init(imageliteralresourcename:).md)
  Returns the image object for the specified resource.
- [init?(systemName: String, withConfiguration: UIImage.Configuration?)](uiimage/init(systemname:withconfiguration:).md)
  Creates an image object that contains a system symbol image with the specified configuration.
- [convenience init?(systemName: String, variableValue: Double, configuration: UIImage.Configuration?)](uiimage/init(systemname:variablevalue:configuration:).md)
  Creates an image object that contains a system symbol image with the configuration and variable value you specify.
- [init?(systemName: String, compatibleWith: UITraitCollection?)](uiimage/init(systemname:compatiblewith:).md)
  Creates an image object that contains a system symbol image appropriate for the specified traits.
- [init?(systemName: String)](uiimage/init(systemname:).md)
  Creates an image object that contains a system symbol image.
- [convenience init(resource: ImageResource)](uiimage/init(resource:).md)
- [Building high-performance lists and collection views](building-high-performance-lists-and-collection-views.md)
  Improve the performance of lists and collections in your app with prefetching and image preparation.
### Loading images for display
- [func preparingForDisplay() -> UIImage?](uiimage/preparingfordisplay.md)
  Decodes an image synchronously and provides a new one for display in views and animations.
- [func prepareForDisplay(completionHandler: (UIImage?) -> Void)](uiimage/preparefordisplay(completionhandler:).md)
  Decodes an image asynchronously and provides a new one for display in views and animations.
- [func preparingThumbnail(of: CGSize) -> UIImage?](uiimage/preparingthumbnail(of:).md)
  Returns a new thumbnail image at the specified size.
- [func prepareThumbnail(of: CGSize, completionHandler: (UIImage?) -> Void)](uiimage/preparethumbnail(of:completionhandler:).md)
  Creates a thumbnail image at the specified size asynchronously on a background thread.
### Creating and initializing image objects
- [init?(contentsOfFile: String)](uiimage/init(contentsoffile:).md)
  Initializes and returns the image object with the contents of the specified file.
- [init?(data: Data)](uiimage/init(data:).md)
  Initializes and returns the image object with the specified data.
- [init?(data: Data, scale: CGFloat)](uiimage/init(data:scale:).md)
  Initializes and returns the image object with the specified data and scale factor.
- [init(cgImage: CGImage)](uiimage/init(cgimage:).md)
  Initializes and returns the image object with the specified Quartz image reference.
- [init(cgImage: CGImage, scale: CGFloat, orientation: UIImage.Orientation)](uiimage/init(cgimage:scale:orientation:).md)
  Initializes and returns an image object with the specified scale and orientation factors.
- [init(ciImage: CIImage)](uiimage/init(ciimage:).md)
  Initializes and returns an image object with the specified Core Image object.
- [init(ciImage: CIImage, scale: CGFloat, orientation: UIImage.Orientation)](uiimage/init(ciimage:scale:orientation:).md)
  Initializes and returns an image object with the specified Core Image object and properties.
- [struct UIImageReader](uiimagereader-swift.struct.md)
### Creating animated images
- [class func animatedImageNamed(String, duration: TimeInterval) -> UIImage?](uiimage/animatedimagenamed(_:duration:).md)
  Creates and returns an animated image.
- [class func animatedImage(with: [UIImage], duration: TimeInterval) -> UIImage?](uiimage/animatedimage(with:duration:).md)
  Creates and returns an animated image from an existing set of images.
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, duration: TimeInterval) -> UIImage?](uiimage/animatedresizableimagenamed(_:capinsets:duration:).md)
  Creates and returns an animated image with end caps.
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode, duration: TimeInterval) -> UIImage?](uiimage/animatedresizableimagenamed(_:capinsets:resizingmode:duration:).md)
  Creates and returns an animated image with end caps and a specific resizing mode.
### Changing the image attributes
- [func withConfiguration(UIImage.Configuration) -> UIImage](uiimage/withconfiguration(_:).md)
  Returns a new version of the current image, replacing the current configuration attributes with the specified attributes.
- [func applyingSymbolConfiguration(UIImage.SymbolConfiguration) -> UIImage?](uiimage/applyingsymbolconfiguration(_:).md)
  Returns a new version of the current image, applying the specified configuration attributes on top of the current attributes.
- [func imageFlippedForRightToLeftLayoutDirection() -> UIImage](uiimage/imageflippedforrighttoleftlayoutdirection.md)
  Returns a new version of the current image that flips horizontally when it’s in a right-to-left layout.
- [func withHorizontallyFlippedOrientation() -> UIImage](uiimage/withhorizontallyflippedorientation.md)
  Returns a new version of the image that’s a mirror of the original image.
- [func withRenderingMode(UIImage.RenderingMode) -> UIImage](uiimage/withrenderingmode(_:).md)
  Returns a new version of the image that uses the specified rendering mode.
- [func withAlignmentRectInsets(UIEdgeInsets) -> UIImage](uiimage/withalignmentrectinsets(_:).md)
  Returns a new version of the image that uses the specified alignment insets.
- [func resizableImage(withCapInsets: UIEdgeInsets) -> UIImage](uiimage/resizableimage(withcapinsets:).md)
  Returns a new version of the image with the specified cap insets.
- [func resizableImage(withCapInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode) -> UIImage](uiimage/resizableimage(withcapinsets:resizingmode:).md)
  Returns a new version of the image with the specified cap insets and options.
- [func imageWithoutBaseline() -> UIImage](uiimage/imagewithoutbaseline.md)
  Creates a copy of the current image object without any baseline information.
- [func withBaselineOffset(fromBottom: CGFloat) -> UIImage](uiimage/withbaselineoffset(frombottom:).md)
  Creates a new image with a baseline at the specified offset from the bottom of the image.
- [UIImage.Configuration](uiimage/configuration-swift.class.md)
  A configuration object that contains the traits that the system uses when selecting the current image variant.
- [UIImage.SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md)
  An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.
### Getting standard system images
- [class var add: UIImage](uiimage/add.md)
  The standard image for indicating the addition of content.
- [class var remove: UIImage](uiimage/remove.md)
  The standard image for indicating the removal of content.
- [class var actions: UIImage](uiimage/actions.md)
  The standard image for indicating user-initiated actions.
- [class var checkmark: UIImage](uiimage/checkmark.md)
  The standard image for a checkmark on a filled-circle background.
- [class var strokedCheckmark: UIImage](uiimage/strokedcheckmark.md)
  The standard image for a checkmark on a tinted circle with a white-stroked border.
### Getting the image data
- [var cgImage: CGImage?](uiimage/cgimage.md)
  The underlying Quartz image data.
- [var ciImage: CIImage?](uiimage/ciimage.md)
  The underlying Core Image data.
- [var images: [UIImage]?](uiimage/images.md)
  The complete array of image objects that compose the animation of an animated object.
- [var imageAsset: UIImageAsset?](uiimage/imageasset.md)
  The image asset (if any) for the image.
### Getting the image size and scale
- [var scale: CGFloat](uiimage/scale.md)
  The scale factor of the image.
- [var size: CGSize](uiimage/size.md)
  The logical dimensions, in points, for the image.
### Accessing image attributes
- [var imageOrientation: UIImage.Orientation](uiimage/imageorientation.md)
  The orientation of the receiver’s image.
- [UIImage.Orientation](uiimage/orientation.md)
  Constants that specify the intended display orientation for an image.
- [var flipsForRightToLeftLayoutDirection: Bool](uiimage/flipsforrighttoleftlayoutdirection.md)
  A Boolean value that indicates whether the image flips in a right-to-left layout.
- [var resizingMode: UIImage.ResizingMode](uiimage/resizingmode-swift.property.md)
  The resizing mode of the image.
- [UIImage.ResizingMode](uiimage/resizingmode-swift.enum.md)
  Constants that specify the possible resizing modes for an image.
- [var duration: TimeInterval](uiimage/duration.md)
  The time interval for displaying an animated image.
- [var capInsets: UIEdgeInsets](uiimage/capinsets.md)
  The end-cap insets.
- [var alignmentRectInsets: UIEdgeInsets](uiimage/alignmentrectinsets.md)
  The alignment metadata for positioning the image during layout.
- [var isSymbolImage: Bool](uiimage/issymbolimage.md)
  A Boolean value that indicates whether the image is a symbol.
### Getting the image configuration
- [var configuration: UIImage.Configuration?](uiimage/configuration-swift.property.md)
  The configuration details for the image.
- [var symbolConfiguration: UIImage.SymbolConfiguration?](uiimage/symbolconfiguration-swift.property.md)
  The configuration details for a symbol image.
- [var traitCollection: UITraitCollection](uiimage/traitcollection.md)
  The trait collection that describes the current variant of the image.
### Specifying the dynamic range
- [var isHighDynamicRange: Bool](uiimage/ishighdynamicrange.md)
- [func imageRestrictedToStandardDynamicRange() -> UIImage](uiimage/imagerestrictedtostandarddynamicrange.md)
- [func heicData() -> Data?](uiimage/heicdata.md)
- [UIImage.DynamicRange](uiimage/dynamicrange.md)
### Managing the baseline
- [var baselineOffsetFromBottom: CGFloat?](uiimage/baselineoffsetfrombottom-3emg.md)
  The position of the baseline relative to the bottom of the image.
### Getting rendering information
- [var renderingMode: UIImage.RenderingMode](uiimage/renderingmode-swift.property.md)
  A setting that determines how the app renders an image.
- [UIImage.RenderingMode](uiimage/renderingmode-swift.enum.md)
  Constants that specify the possible rendering modes for an image.
- [var imageRendererFormat: UIGraphicsImageRendererFormat](uiimage/imagerendererformat.md)
  The preferred image renderer format for the image.
### Tinting the image
- [func withTintColor(UIColor) -> UIImage](uiimage/withtintcolor(_:).md)
  Returns a new version of the current image with the specified tint color.
- [func withTintColor(UIColor, renderingMode: UIImage.RenderingMode) -> UIImage](uiimage/withtintcolor(_:renderingmode:).md)
  Returns a new version of the image with a tint color that uses the specified rendering mode.
### Drawing images
- [func draw(at: CGPoint)](uiimage/draw(at:).md)
  Draws the image at the specified point in the current context.
- [func draw(at: CGPoint, blendMode: CGBlendMode, alpha: CGFloat)](uiimage/draw(at:blendmode:alpha:).md)
  Draws the entire image at the specified point using the custom compositing options.
- [func draw(in: CGRect)](uiimage/draw(in:).md)
  Draws the entire image in the specified rectangle, scaling it as necessary to fit.
- [func draw(in: CGRect, blendMode: CGBlendMode, alpha: CGFloat)](uiimage/draw(in:blendmode:alpha:).md)
  Draws the entire image in the specified rectangle using the specified compositing options.
- [func drawAsPattern(in: CGRect)](uiimage/drawaspattern(in:).md)
  Draws a tiled Quartz pattern using the receiver’s contents as the tile pattern.
### Exporting standard bitmap formats
- [func jpegData(compressionQuality: CGFloat) -> Data?](uiimage/jpegdata(compressionquality:).md)
  Returns a data object that contains the image in JPEG format.
- [func pngData() -> Data?](uiimage/pngdata.md)
  Returns a data object that contains the specified image in PNG format.
### Deprecated
- [func stretchableImage(withLeftCapWidth: Int, topCapHeight: Int) -> UIImage](uiimage/stretchableimage(withleftcapwidth:topcapheight:).md)
  Creates and returns a new image object with the specified cap values.
- [var leftCapWidth: Int](uiimage/leftcapwidth.md)
  The horizontal end-cap size.
- [var topCapHeight: Int](uiimage/topcapheight.md)
  The vertical end-cap size.

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
- [JournalingSuggestionAsset](../JournalingSuggestions/JournalingSuggestionAsset.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSItemProviderReading](../Foundation/NSItemProviderReading.md)
- [NSItemProviderWriting](../Foundation/NSItemProviderWriting.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIItemProviderPresentationSizeProviding](uiitemproviderpresentationsizeproviding.md)

## See Also

- [UIImage.SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md)
  An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.
- [UIImage.Configuration](uiimage/configuration-swift.class.md)
  A configuration object that contains the traits that the system uses when selecting the current image variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage)*