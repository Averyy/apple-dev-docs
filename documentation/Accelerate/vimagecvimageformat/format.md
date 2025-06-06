# vImageCVImageFormat.Format

**Framework**: Accelerate  
**Kind**: enum

Constants that specify the format of a Core Video image format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
enum Format
```

## Topics

### RGB format constants
- [vImageCVImageFormat.Format.format16LE555](vimagecvimageformat/format/format16le555.md)
  A little-endian 16-bit, RGB pixel format with 5 bits per channel.
- [vImageCVImageFormat.Format.format16LE565](vimagecvimageformat/format/format16le565.md)
  A little-endian 16-bit, RGB pixel format with 5 bits for red and blue, and 6 bits for green.
- [vImageCVImageFormat.Format.format16BE555](vimagecvimageformat/format/format16be555.md)
  A big-endian 16-bit, RGB pixel format with 5 bits per channel.
- [vImageCVImageFormat.Format.format16BE565](vimagecvimageformat/format/format16be565.md)
  A big-endian 16-bit, RGB pixel format with 5 bits for red and blue, and 6 bits for green.
- [vImageCVImageFormat.Format.format24RGB](vimagecvimageformat/format/format24rgb.md)
  A 24-bit, RGB pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format24BGR](vimagecvimageformat/format/format24bgr.md)
  A 24-bit, BGR pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format30RGB](vimagecvimageformat/format/format30rgb.md)
  A big-endian 30-bit, RGB pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format30RGBLEPackedWideGamut](vimagecvimageformat/format/format30rgblepackedwidegamut.md)
  A little-endian 30-bit, wide-gamut RGB pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format48RGB](vimagecvimageformat/format/format48rgb.md)
  A big-endian 48-bit, RGB pixel format with 16 bits per channel.
### RGBA and ARGB format constants
- [vImageCVImageFormat.Format.format16LE5551](vimagecvimageformat/format/format16le5551.md)
  A little-endian 16-bit, RGBA pixel format with 5 bits per color channel and 1-bit alpha.
- [vImageCVImageFormat.Format.format32ABGR](vimagecvimageformat/format/format32abgr.md)
  A 32-bit, ABGR pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format32ARGB](vimagecvimageformat/format/format32argb.md)
  A 32-bit, ARGB pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format32BGRA](vimagecvimageformat/format/format32bgra.md)
  A 32-bit, BGRA pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format32RGBA](vimagecvimageformat/format/format32rgba.md)
  A 32-bit, RGBA pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format64ARGB](vimagecvimageformat/format/format64argb.md)
  A 64-bit, ARGB pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format64RGBAHalf](vimagecvimageformat/format/format64rgbahalf.md)
  A little-endian 64-bit, RGBA pixel format with 16 bits per channel.
- [vImageCVImageFormat.Format.format128RGBAFloat](vimagecvimageformat/format/format128rgbafloat.md)
  A little-endian 128-bit, RGBA pixel format with 32 bits per channel.
- [vImageCVImageFormat.Format.formatARGB2101010LEPacked](vimagecvimageformat/format/formatargb2101010lepacked.md)
  A little-endian ARGB2101010 full-range ARGB pixel format.
### Monochrome format constants
- [vImageCVImageFormat.Format.format16Gray](vimagecvimageformat/format/format16gray.md)
  A big-endian 16-bit grayscale pixel format with black equal to zero.
- [vImageCVImageFormat.Format.format32AlphaGray](vimagecvimageformat/format/format32alphagray.md)
  A big-endian 16-bit grayscale with alpha pixel format with black equal to zero.
### 4:2:0 YpCbCr format constants
- [vImageCVImageFormat.Format.format420YpCbCr8Planar](vimagecvimageformat/format/format420ypcbcr8planar.md)
  A planar YpCbCr 4:2:0 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format420YpCbCr8BiPlanarFullRange](vimagecvimageformat/format/format420ypcbcr8biplanarfullrange.md)
  A full-range, two-plane YpCbCr 4:2:0 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format420YpCbCr8BiPlanarVideoRange](vimagecvimageformat/format/format420ypcbcr8biplanarvideorange.md)
  A video-range, two-plane YpCbCr 4:2:0 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format420YpCbCr8PlanarFullRange](vimagecvimageformat/format/format420ypcbcr8planarfullrange.md)
  A full-range, planar YpCbCr 4:2:0 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format420YpCbCr10BiPlanarFullRange](vimagecvimageformat/format/format420ypcbcr10biplanarfullrange.md)
  A full-range, two-plane YpCbCr 4:2:0 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format420YpCbCr10BiPlanarVideoRange](vimagecvimageformat/format/format420ypcbcr10biplanarvideorange.md)
  A video-range, two-plane YpCbCr 4:2:0 pixel format with 10 bits per channel.
### 4:2:2 YpCbCr format constants
- [vImageCVImageFormat.Format.format422YpCbCr8](vimagecvimageformat/format/format422ypcbcr8.md)
  A component YpCbCr 4:2:2 pixel format with 8 bits per channel and ordered CbYp₀CrYp₁.
- [vImageCVImageFormat.Format.format422YpCbCr8_yuvs](vimagecvimageformat/format/format422ypcbcr8_yuvs.md)
  A component YpCbCr 4:2:2 pixel format with 8 bits per channel and ordered Yp₀CbYp₁Cr.
- [vImageCVImageFormat.Format.format422YpCbCr8FullRange](vimagecvimageformat/format/format422ypcbcr8fullrange.md)
  A full-range, component YpCbCr 4:2:2 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr10](vimagecvimageformat/format/format422ypcbcr10.md)
  A component YpCbCr 4:2:2 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr10BiPlanarFullRange](vimagecvimageformat/format/format422ypcbcr10biplanarfullrange.md)
  A full-range, two-plane YpCbCr 4:2:2 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr10BiPlanarVideoRange](vimagecvimageformat/format/format422ypcbcr10biplanarvideorange.md)
  A video-range, two-plane YpCbCr 4:2:2 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr16](vimagecvimageformat/format/format422ypcbcr16.md)
  A video-range, two-plane YpCbCr 4:2:2 pixel format with 16 bits per channel.
### 4:4:4 YpCbCr format constants
- [vImageCVImageFormat.Format.format444YpCbCr8](vimagecvimageformat/format/format444ypcbcr8.md)
  A video-range, component YpCbCr 4:4:4 pixel format with 8 bits per channel and ordered CrYpCb.
- [vImageCVImageFormat.Format.format444YpCbCr10](vimagecvimageformat/format/format444ypcbcr10.md)
  A component YpCbCr 4:4:4 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format444YpCbCr10BiPlanarFullRange](vimagecvimageformat/format/format444ypcbcr10biplanarfullrange.md)
  A full-range, two-plane YpCbCr 4:4:4 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format444YpCbCr10BiPlanarVideoRange](vimagecvimageformat/format/format444ypcbcr10biplanarvideorange.md)
  A video-range, two-plane YpCbCr 4:4:4 pixel format with 10 bits per channel.
### YpCbCr with alpha format constants
- [vImageCVImageFormat.Format.format422YpCbCr_4A_8BiPlanar](vimagecvimageformat/format/format422ypcbcr_4a_8biplanar.md)
  A two-plane pixel format that contains a video-range 8-bit YpCbCr 4:2:2 plane and an 8-bit alpha plane.
- [vImageCVImageFormat.Format.format4444AYpCbCr8](vimagecvimageformat/format/format4444aypcbcr8.md)
  A full-range alpha, video-range luminance and chrominance YpCbCrA 4:4:4:4 pixel format with 8 bits per channel and ordered AYpCbCr.
- [vImageCVImageFormat.Format.format4444YpCbCrA8](vimagecvimageformat/format/format4444ypcbcra8.md)
  A component YpCbCrA 4:4:4:4 pixel format with 8 bits per channel and ordered CbYpCrA.
- [vImageCVImageFormat.Format.format4444YpCbCrA8R](vimagecvimageformat/format/format4444ypcbcra8r.md)
  A component YpCbCrA 4:4:4:4 rendering format with 8 bits per channel, full-range alpha, zero-biased YUV, and ordered AYpCbCr.
- [vImageCVImageFormat.Format.format4444AYpCbCr16](vimagecvimageformat/format/format4444aypcbcr16.md)
  A full-range alpha, video-range luminance and chrominance YpCbCrA 4:4:4:4 pixel format with 16 bits per channel and ordered AYpCbCr.
### Bayer format constants
- [vImageCVImageFormat.Format.format14Bayer_BGGR](vimagecvimageformat/format/format14bayer_bggr.md)
  A little-endian 14-bit Bayer pixel format with even rows ordered blue-green and odd rows ordered green-red.
- [vImageCVImageFormat.Format.format14Bayer_GBRG](vimagecvimageformat/format/format14bayer_gbrg.md)
  A little-endian 14-bit Bayer pixel format with even rows ordered green-blue and odd rows ordered red-green.
- [vImageCVImageFormat.Format.format14Bayer_GRBG](vimagecvimageformat/format/format14bayer_grbg.md)
  A little-endian 14-bit Bayer pixel format with even rows ordered green-red and odd rows ordered blue-green.
- [vImageCVImageFormat.Format.format14Bayer_RGGB](vimagecvimageformat/format/format14bayer_rggb.md)
  A little-endian 14-bit Bayer pixel format with even rows ordered red-green and odd rows ordered green-blue.
### Indexed color format constants
- [vImageCVImageFormat.Format.format1Monochrome](vimagecvimageformat/format/format1monochrome.md)
  A 1-bit indexed pixel format.
- [vImageCVImageFormat.Format.format1IndexedGray_WhiteIsZero](vimagecvimageformat/format/format1indexedgray_whiteiszero.md)
  A 1-bit indexed pixel format with white equal to zero.
- [vImageCVImageFormat.Format.format2Indexed](vimagecvimageformat/format/format2indexed.md)
  A 2-bit indexed pixel format.
- [vImageCVImageFormat.Format.format2IndexedGray_WhiteIsZero](vimagecvimageformat/format/format2indexedgray_whiteiszero.md)
  A 2-bit indexed pixel format with white equal to zero.
- [vImageCVImageFormat.Format.format4Indexed](vimagecvimageformat/format/format4indexed.md)
  A 4-bit indexed pixel format.
- [vImageCVImageFormat.Format.format4IndexedGray_WhiteIsZero](vimagecvimageformat/format/format4indexedgray_whiteiszero.md)
  A 4-bit indexed pixel format with white equal to zero.
- [vImageCVImageFormat.Format.format8Indexed](vimagecvimageformat/format/format8indexed.md)
  An 8-bit indexed pixel format.
- [vImageCVImageFormat.Format.format8IndexedGray_WhiteIsZero](vimagecvimageformat/format/format8indexedgray_whiteiszero.md)
  An 8-bit indexed pixel format with white equal to zero.
### Depth format constants
- [vImageCVImageFormat.Format.formatDepthFloat16](vimagecvimageformat/format/formatdepthfloat16.md)
  A 16-bit depth pixel format that describes the distance to an object in meters.
- [vImageCVImageFormat.Format.formatDepthFloat32](vimagecvimageformat/format/formatdepthfloat32.md)
  A 32-bit depth pixel format that describes the distance to an object in meters.
### Disparity format constants
- [vImageCVImageFormat.Format.formatDisparityFloat16](vimagecvimageformat/format/formatdisparityfloat16.md)
  A 16-bit disparity pixel format that describes the normalized shift when comparing two images.
- [vImageCVImageFormat.Format.formatDisparityFloat32](vimagecvimageformat/format/formatdisparityfloat32.md)
  A 32-bit disparity pixel format that describes the normalized shift when comparing two images.
### Single-component format constants
- [vImageCVImageFormat.Format.formatOneComponent8](vimagecvimageformat/format/formatonecomponent8.md)
  An 8-bit, single-component pixel format with black equal to zero.
- [vImageCVImageFormat.Format.formatOneComponent16Half](vimagecvimageformat/format/formatonecomponent16half.md)
  A little-endian 16-bit, single-componennt pixel format.
- [vImageCVImageFormat.Format.formatOneComponent32Float](vimagecvimageformat/format/formatonecomponent32float.md)
  A little-endian 32-bit, single-component pixel format.
### Two-component format constants
- [vImageCVImageFormat.Format.formatTwoComponent8](vimagecvimageformat/format/formattwocomponent8.md)
  An 8-bit, two-component pixel format with black equal to zero.
- [vImageCVImageFormat.Format.formatTwoComponent16Half](vimagecvimageformat/format/formattwocomponent16half.md)
  A little-endian 16-bit, two-component pixel format.
- [vImageCVImageFormat.Format.formatTwoComponent32Float](vimagecvimageformat/format/formattwocomponent32float.md)
  A little-endian 32-bit, two-component pixel format.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [vImageCVImageFormat.ChromaSiting](vimagecvimageformat/chromasiting-swift.enum.md)
  Constants that specify the chrominance siting of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/format)*