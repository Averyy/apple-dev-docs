# Building a basic image conversion workflow

**Framework**: Accelerate  
**Role**: Article

Learn the fundamentals of the convert-any-to-any function by converting a CMYK image to an RGB image.

#### Overview

The functions in the vImage library that perform image-processing operations are specific to properties such as bit-depth, the number of channels, and channel ordering. For example, the [`vImageAlphaBlend_ARGB8888(_:_:_:_:)`](./vimagealphablend_argb8888%28_,_,_,_%29.md) function works with 8-bit-per-channel, ARGB image data. The convert-any-to-any functionality allows you to convert images with formats you know at runtime to a format you define at compile time.

You can use the vImage convert-any-to-any functionality to convert image data between different bit depths, different channel counts, and different color spaces. In this example, the code converts a 16-bit-per-channel CMYK source image to an 8-bit-per-channel RGB destination image. In some cases, working in a non-RGB color space simplifies image-processing tasks. For an example of using convert-any-to-any to work in L*a*b* color space, see [Adjusting the hue of an image](./adjusting-the-hue-of-an-image.md).

##### Create the source and destination image formats

A [`vImageConverter`](./vimageconverter.md) instance – that contains the information to perform image conversion – requires two [`vImage_CGImageFormat`](./vimage_cgimageformat.md) structures that describe the source and destination formats. The code below defines the CMYK source format and the RGB destination format:

**Swift**:

```swift
let cmykSourceImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 16,
    bitsPerPixel: 16 * 4,
    colorSpace: CGColorSpaceCreateDeviceCMYK(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue))!

let rgbDestinationImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 3,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue))!
```

**Objective-C**:

```objc
vImage_CGImageFormat cmykSourceImageFormat = {
    .bitsPerComponent = 16,
    .bitsPerPixel = 16 * 4,
    .colorSpace = CGColorSpaceCreateDeviceCMYK(),
    .bitmapInfo = kCGImageAlphaNone,
    .version = 0,
    .renderingIntent = kCGRenderingIntentDefault
};

vImage_CGImageFormat rgbDestinationImageFormat = {
    .bitsPerComponent = 8,
    .bitsPerPixel = 8 * 3,
    .colorSpace = CGColorSpaceCreateDeviceRGB(),
    .bitmapInfo = kCGImageAlphaNone,
    .version = 0,
    .renderingIntent = kCGRenderingIntentDefault
};
```

##### Create the converter

The Swift [`make(sourceFormat:destinationFormat:flags:)`](./vimageconverter/make%28sourceformat,destinationformat,flags%29-8tbym.md) method calls the underlying [`vImageConverter_CreateWithCGImageFormat(_:_:_:_:_:)`](./vimageconverter_createwithcgimageformat%28_,_,_,_,_%29.md) function and returns a new any-to-any converter instance.

**Swift**:

```swift
let cmykToRgbConverter = try vImageConverter.make(
    sourceFormat: cmykSourceImageFormat,
    destinationFormat: rgbDestinationImageFormat)
```

**Objective-C**:

```objc
vImage_Error error;
vImageConverterRef cmykToRgbConverter =
    vImageConverter_CreateWithCGImageFormat(&cmykSourceImageFormat,
                                           &rgbDestinationImageFormat,
                                           NULL,
                                           kvImageNoFlags,
                                           &error);
```

##### Perform the conversion using pixel buffers

The code below converts the CMYK image data that `cmykSourceBuffer` contains and writes the RGB result to `rgbDestinationBuffer`. In this example, `cmykSourceBuffer` is a [`vImage.PixelBuffer`](./vimage/pixelbuffer.md) structure with a [`vImage.Interleaved16Ux4`](./vimage/interleaved16ux4.md) format.

The Swift [`convert(from:to:)`](./vimageconverter/convert%28from,to%29-9s7p7.md) method calls the underlying [`vImageConvert_AnyToAny(_:_:_:_:_:)`](./vimageconvert_anytoany%28_,_,_,_,_%29.md) function.

```swift
let rgbDestinationBuffer = vImage.PixelBuffer<vImage.Interleaved8x3>(
    size: cmykSourceBuffer.size)

try cmykToRgbConverter.convert(from: cmykSourceBuffer,
                               to: rgbDestinationBuffer)
```

On return, `rgbDestinationBuffer` contains the RGB representation of the CMYK source image.

##### Perform the conversion using vImage buffers

If you’re creating apps for older operating systems that don’t support the [`vImage.PixelBuffer`](./vimage/pixelbuffer.md) API, the following code performs the same conversion using [`vImage_Buffer`](./vimage_buffer.md) structures.

The Swift [`convert(source:destination:flags:)`](./vimageconverter/convert%28source,destination,flags%29.md) method calls the underlying [`vImageConvert_AnyToAny(_:_:_:_:_:)`](./vimageconvert_anytoany%28_,_,_,_,_%29.md) function

**Swift**:

```swift
var rgbDestinationBuffer = try vImage_Buffer(
    size: cmykSourceBuffer.size,
    bitsPerPixel: rgbDestinationImageFormat.bitsPerPixel)

try cmykToRgbConverter.convert(source: cmykSourceBuffer,
                               destination: &rgbDestinationBuffer)
```

**Objective-C**:

```objc
vImage_Buffer rgbDestinationBuffer;
vImageBuffer_Init(&rgbDestinationBuffer,
                  cmykSourceBuffer.height,
                  cmykSourceBuffer.width,
                  rgbDestinationImageFormat.bitsPerPixel,
                  kvImageNoFlags);

vImageConvert_AnyToAny(cmykToRgbConverter,
                       &cmykSourceBuffer,
                       &rgbDestinationBuffer,
                       NULL,
                       kvImageNoFlags);
```

On return, `rgbDestinationBuffer` contains the RGB representation of the CMYK source image.

## See Also

### Conversion Between Image Formats
- [Converting color images to grayscale](./converting-color-images-to-grayscale.md)
  Convert an RGB image to grayscale using matrix multiplication.
- [Applying color transforms to images with a multidimensional lookup table](./applying-color-transforms-to-images-with-a-multidimensional-lookup-table.md)
  Precompute translation values to optimize color space conversion and other pointwise operations.
- [Converting luminance and chrominance planes to an ARGB image](./converting-luminance-and-chrominance-planes-to-an-argb-image.md)
  Create a displayable ARGB image using the luminance and chrominance information from your device’s camera.
- [Conversion](./conversion.md)
  Convert an image to a different format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/building-a-basic-image-conversion-workflow)*