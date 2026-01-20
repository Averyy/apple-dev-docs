# Core Image

**Framework**: Core Image  
**Kind**: module

Use built-in or custom filters to process still and video images.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

#### Overview

Core Image is an image processing and analysis technology that provides high-performance processing for still and video images. Use the many built-in image filters to process images and build complex effects by chaining filters. For a list of all the built-in filters see the [`Filter Catalog`](https://developer.apple.com/documentation/coreimage#Filter-Catalog).

You can also create new effects with custom filters and image processors; see [`Custom Filters`](https://developer.apple.com/documentation/coreimage#Custom-Filters).

## Topics

### Essentials
- [Processing an Image Using Built-in Filters](processing-an-image-using-built-in-filters.md)
  Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [class CIContext](cicontext.md)
  The Core Image context class provides an evaluation context for Core Image processing with Metal, OpenGL, or OpenCL.
- [class CIImage](ciimage.md)
  A representation of an image to be processed or produced by Core Image filters.
### Filters
- [class CIFilter](cifilter-swift.class.md)
  An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [class CIRAWFilter](cirawfilter.md)
  A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [class CIColor](cicolor.md)
  The Core Image class that defines a color object.
- [class CIVector](civector.md)
  The Core Image class that defines a vector object.
### Filter Catalog
- [Blur Filters](blur-filters.md)
  Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color-adjustment-filters.md)
  Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color-effect-filters.md)
  Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite-operations.md)
  Composite images by using a range of blend modes and compositing operators.
- [Convolution Filters](convolution-filters.md)
  Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion-filters.md)
  Apply distortion to images.
- [Generator Filters](generator-filters.md)
  Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](geometry-adjustment-filters.md)
  Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](gradient-filters.md)
  Generate linear and radial gradients.
- [Halftone Effect Filters](halftone-effect-filters.md)
  Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](reduction-filters.md)
  Create statistical information about an image.
- [Sharpening Filters](sharpening-filters.md)
  Apply sharpening to images.
- [Stylizing Filters](stylizing-filters.md)
  Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile-effect-filters.md)
  Produce tiled images from source images.
- [Transition Filters](transition-filters.md)
  Transition between two images by using effects including page curl and swipe.
### Filter Recipes
- [Applying a Chroma Key Effect](applying-a-chroma-key-effect.md)
  Replace a color in one image with the background from another.
- [Selectively Focusing on an Image](selectively-focusing-on-an-image.md)
  Focus on a part of an image by applying Gaussian blur and gradient masks.
- [Customizing Image Transitions](customizing-image-transitions.md)
  Transition between images in creative ways using Core Image filters.
- [Simulating Scratchy Analog Film](simulating-scratchy-analog-film.md)
  Degrade the quality of an image to make it look like dated, analog film.
### Custom Filters
- [Writing Custom Kernels](writing-custom-kernels.md)
  Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [class CIKernel](cikernel.md)
  A GPU-based image-processing routine used to create custom Core Image filters.
- [class CIColorKernel](cicolorkernel.md)
  A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [class CIWarpKernel](ciwarpkernel.md)
  A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [class CIBlendKernel](ciblendkernel.md)
  A GPU-based image-processing routine that is optimized for blending two images.
- [class CISampler](cisampler.md)
  An object that retrieves pixel samples for processing by a filter kernel.
- [class CIFilterShape](cifiltershape.md)
  A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [struct CIFormat](ciformat.md)
  Pixel data formats for image input, output, and processing.
### Custom Image Processors
- [class CIImageProcessorKernel](ciimageprocessorkernel.md)
  The abstract class you extend to create custom image processors that can integrate with Core Image workflows.
- [protocol CIImageProcessorInput](ciimageprocessorinput.md)
  A container of image data and information for use in a custom image processor.
- [protocol CIImageProcessorOutput](ciimageprocessoroutput.md)
  A container for writing image data and information produced by a custom image processor.
### Custom Render Destination
- [Generating an animation with a Core Image Render Destination](generating-an-animation-with-a-core-image-render-destination.md)
  Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [class CIRenderDestination](cirenderdestination.md)
  A specification for configuring all attributes of a render task’s destination and issuing asynchronous render tasks.
- [class CIRenderInfo](cirenderinfo.md)
  An encapsulation of a render task’s timing, passes, and pixels processed.
- [class CIRenderTask](cirendertask.md)
  A single render task.
- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.
### Feedback-Based Processing
- [class CIImageAccumulator](ciimageaccumulator.md)
  An object that manages feedback-based image processing for tasks such as painting or fluid simulation.
### Barcode Descriptions
- [class CIBarcodeDescriptor](cibarcodedescriptor.md)
  An abstract base class that represents a machine-readable code’s attributes.
- [class CIQRCodeDescriptor](ciqrcodedescriptor.md)
  A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
- [class CIAztecCodeDescriptor](ciazteccodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.
### Image Feature Detection
- [class CIDetector](cidetector.md)
  An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [class CIFeature](cifeature.md)
  The abstract superclass for objects representing notable features detected in an image.
- [class CIFaceFeature](cifacefeature.md)
  Information about a face detected in a still or video image.
- [class CIRectangleFeature](cirectanglefeature.md)
  Information about a rectangular region detected in a still or video image.
- [class CITextFeature](citextfeature.md)
  Information about a text that was detected in a still or video image.
- [class CIQRCodeFeature](ciqrcodefeature.md)
  Information about a Quick Response code detected in a still or video image.
### Image Units
- [class CIPlugIn](ciplugin.md)
  The mechanism for loading image units in macOS.
- [class CIFilterGenerator](cifiltergenerator.md)
  An object that creates and configures chains of individual image filters.
- [protocol CIPlugInRegistration](cipluginregistration.md)
  The interface for loading Core Image image units.
- [protocol CIFilterConstructor](cifilterconstructor.md)
  A general interface for objects that produce filters.
### Protocols
- [protocol CIAreaBoundsRed](ciareaboundsred.md)
- [protocol CIMaximumScaleTransform](cimaximumscaletransform.md)
- [protocol CIToneMapHeadroom](citonemapheadroom.md)
- [protocol CIAreaAverageMaximumRed](ciareaaveragemaximumred.md)
  The protocol for the Area Average and Maximum Red filter.
- [protocol CIBlurredRoundedRectangleGenerator](ciblurredroundedrectanglegenerator.md)
  The protocol for the Blurred Rounded Rectangle Generator filter.
- [protocol CIDistanceGradientFromRedMask](cidistancegradientfromredmask.md)
  The protocol for the Distance Gradient From Red Mask filter.
- [protocol CIRoundedQRCodeGenerator](ciroundedqrcodegenerator.md)
  The protocol for the Rounded QR Code Generator filter.
- [protocol CISignedDistanceGradientFromRedMask](cisigneddistancegradientfromredmask.md)
  The protocol for the Signed Distance Gradient From Red Mask filter.
### Reference
- [Core Image Constants](core-image-constants.md)
### Variables
- [let kCIInputBacksideImageKey: String](kciinputbacksideimagekey.md)
  A key to get or set the backside image for a transition Core Image filter.
- [let kCIInputBiasVectorKey: String](kciinputbiasvectorkey.md)
  A key to get or set the vector bias value of a Core Image filter.
- [let kCIInputColor0Key: String](kciinputcolor0key.md)
  A key to get or set a color value of a Core Image filter.
- [let kCIInputColor1Key: String](kciinputcolor1key.md)
  A key to get or set a color value of a Core Image filter.
- [let kCIInputColorSpaceKey: String](kciinputcolorspacekey.md)
  A key to get or set a color space value of a Core Image filter.
- [let kCIInputCountKey: String](kciinputcountkey.md)
  A key to get or set the scalar count value of a Core Image filter.
- [let kCIInputExtrapolateKey: String](kciinputextrapolatekey.md)
  A key to get or set the boolean behavior of a Core Image filter that specifies if the filter should extrapolate a table beyond the defined range.
- [let kCIInputPaletteImageKey: String](kciinputpaletteimagekey.md)
  A key to get or set the palette image for a  Core Image filter.
- [let kCIInputPerceptualKey: String](kciinputperceptualkey.md)
  A key to get or set the boolean behavior of a Core Image filter that specifies if the filter should operate in linear or perceptual colors.
- [let kCIInputPoint0Key: String](kciinputpoint0key.md)
  A key to get or set the coordinate value of a Core Image filter.
The value for this key needs to be a [`CIVector`](civector.md) instance containing the `x,y` coordinate.
- [let kCIInputPoint1Key: String](kciinputpoint1key.md)
  A key to get or set a coordinate value of a Core Image filter.
The value for this key needs to be a [`CIVector`](civector.md) instance containing the `x,y` coordinate.
- [let kCIInputRadius0Key: String](kciinputradius0key.md)
  A key to get or set the geometric radius value of a Core Image filter.
- [let kCIInputRadius1Key: String](kciinputradius1key.md)
  A key to get or set the geometric radius value of a Core Image filter.
- [let kCIInputThresholdKey: String](kciinputthresholdkey.md)
  A key to get or set the scalar threshold value of a Core Image filter.

## See Also

- [Core Image Filter Reference](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346-Reference)
- [Core Image Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreImage)*