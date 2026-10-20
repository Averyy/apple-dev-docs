# vImageCVImageFormat.Format

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the format of a Core Video image format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
enum Format
```

## Topics

### RGB format constants
- [vImageCVImageFormat.Format.format16LE555](./format/format16le555.md)
  A little-endian 16-bit, RGB pixel format with 5 bits per channel.
- [vImageCVImageFormat.Format.format16LE565](./format/format16le565.md)
  A little-endian 16-bit, RGB pixel format with 5 bits for red and blue, and 6 bits for green.
- [vImageCVImageFormat.Format.format16BE555](./format/format16be555.md)
  A big-endian 16-bit, RGB pixel format with 5 bits per channel.
- [vImageCVImageFormat.Format.format16BE565](./format/format16be565.md)
  A big-endian 16-bit, RGB pixel format with 5 bits for red and blue, and 6 bits for green.
- [vImageCVImageFormat.Format.format24RGB](./format/format24rgb.md)
  A 24-bit, RGB pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format24BGR](./format/format24bgr.md)
  A 24-bit, BGR pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format30RGB](./format/format30rgb.md)
  A big-endian 30-bit, RGB pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format30RGBLEPackedWideGamut](./format/format30rgblepackedwidegamut.md)
  A little-endian 30-bit, wide-gamut RGB pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format48RGB](./format/format48rgb.md)
  A big-endian 48-bit, RGB pixel format with 16 bits per channel.
### RGBA and ARGB format constants
- [vImageCVImageFormat.Format.format16LE5551](./format/format16le5551.md)
  A little-endian 16-bit, RGBA pixel format with 5 bits per color channel and 1-bit alpha.
- [vImageCVImageFormat.Format.format32ABGR](./format/format32abgr.md)
  A 32-bit, ABGR pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format32ARGB](./format/format32argb.md)
  A 32-bit, ARGB pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format32BGRA](./format/format32bgra.md)
  A 32-bit, BGRA pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format32RGBA](./format/format32rgba.md)
  A 32-bit, RGBA pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format64ARGB](./format/format64argb.md)
  A 64-bit, ARGB pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format64RGBAHalf](./format/format64rgbahalf.md)
  A little-endian 64-bit, RGBA pixel format with 16 bits per channel.
- [vImageCVImageFormat.Format.format128RGBAFloat](./format/format128rgbafloat.md)
  A little-endian 128-bit, RGBA pixel format with 32 bits per channel.
- [vImageCVImageFormat.Format.formatARGB2101010LEPacked](./format/formatargb2101010lepacked.md)
  A little-endian ARGB2101010 full-range ARGB pixel format.
### Monochrome format constants
- [vImageCVImageFormat.Format.format16Gray](./format/format16gray.md)
  A big-endian 16-bit grayscale pixel format with black equal to zero.
- [vImageCVImageFormat.Format.format32AlphaGray](./format/format32alphagray.md)
  A big-endian 16-bit grayscale with alpha pixel format with black equal to zero.
### 4:2:0 YpCbCr format constants
- [vImageCVImageFormat.Format.format420YpCbCr8Planar](./format/format420ypcbcr8planar.md)
  A planar YpCbCr 4:2:0 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format420YpCbCr8BiPlanarFullRange](./format/format420ypcbcr8biplanarfullrange.md)
  A full-range, two-plane YpCbCr 4:2:0 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format420YpCbCr8BiPlanarVideoRange](./format/format420ypcbcr8biplanarvideorange.md)
  A video-range, two-plane YpCbCr 4:2:0 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format420YpCbCr8PlanarFullRange](./format/format420ypcbcr8planarfullrange.md)
  A full-range, planar YpCbCr 4:2:0 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format420YpCbCr10BiPlanarFullRange](./format/format420ypcbcr10biplanarfullrange.md)
  A full-range, two-plane YpCbCr 4:2:0 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format420YpCbCr10BiPlanarVideoRange](./format/format420ypcbcr10biplanarvideorange.md)
  A video-range, two-plane YpCbCr 4:2:0 pixel format with 10 bits per channel.
### 4:2:2 YpCbCr format constants
- [vImageCVImageFormat.Format.format422YpCbCr8](./format/format422ypcbcr8.md)
  A component YpCbCr 4:2:2 pixel format with 8 bits per channel and ordered CbYp₀CrYp₁.
- [vImageCVImageFormat.Format.format422YpCbCr8_yuvs](./format/format422ypcbcr8_yuvs.md)
  A component YpCbCr 4:2:2 pixel format with 8 bits per channel and ordered Yp₀CbYp₁Cr.
- [vImageCVImageFormat.Format.format422YpCbCr8FullRange](./format/format422ypcbcr8fullrange.md)
  A full-range, component YpCbCr 4:2:2 pixel format with 8 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr10](./format/format422ypcbcr10.md)
  A component YpCbCr 4:2:2 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr10BiPlanarFullRange](./format/format422ypcbcr10biplanarfullrange.md)
  A full-range, two-plane YpCbCr 4:2:2 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr10BiPlanarVideoRange](./format/format422ypcbcr10biplanarvideorange.md)
  A video-range, two-plane YpCbCr 4:2:2 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format422YpCbCr16](./format/format422ypcbcr16.md)
  A video-range, two-plane YpCbCr 4:2:2 pixel format with 16 bits per channel.
### 4:4:4 YpCbCr format constants
- [vImageCVImageFormat.Format.format444YpCbCr8](./format/format444ypcbcr8.md)
  A video-range, component YpCbCr 4:4:4 pixel format with 8 bits per channel and ordered CrYpCb.
- [vImageCVImageFormat.Format.format444YpCbCr10](./format/format444ypcbcr10.md)
  A component YpCbCr 4:4:4 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format444YpCbCr10BiPlanarFullRange](./format/format444ypcbcr10biplanarfullrange.md)
  A full-range, two-plane YpCbCr 4:4:4 pixel format with 10 bits per channel.
- [vImageCVImageFormat.Format.format444YpCbCr10BiPlanarVideoRange](./format/format444ypcbcr10biplanarvideorange.md)
  A video-range, two-plane YpCbCr 4:4:4 pixel format with 10 bits per channel.
### YpCbCr with alpha format constants
- [vImageCVImageFormat.Format.format422YpCbCr_4A_8BiPlanar](./format/format422ypcbcr_4a_8biplanar.md)
  A two-plane pixel format that contains a video-range 8-bit YpCbCr 4:2:2 plane and an 8-bit alpha plane.
- [vImageCVImageFormat.Format.format4444AYpCbCr8](./format/format4444aypcbcr8.md)
  A full-range alpha, video-range luminance and chrominance YpCbCrA 4:4:4:4 pixel format with 8 bits per channel and ordered AYpCbCr.
- [vImageCVImageFormat.Format.format4444YpCbCrA8](./format/format4444ypcbcra8.md)
  A component YpCbCrA 4:4:4:4 pixel format with 8 bits per channel and ordered CbYpCrA.
- [vImageCVImageFormat.Format.format4444YpCbCrA8R](./format/format4444ypcbcra8r.md)
  A component YpCbCrA 4:4:4:4 rendering format with 8 bits per channel, full-range alpha, zero-biased YUV, and ordered AYpCbCr.
- [vImageCVImageFormat.Format.format4444AYpCbCr16](./format/format4444aypcbcr16.md)
  A full-range alpha, video-range luminance and chrominance YpCbCrA 4:4:4:4 pixel format with 16 bits per channel and ordered AYpCbCr.
### Bayer format constants
- [vImageCVImageFormat.Format.format14Bayer_BGGR](./format/format14bayer_bggr.md)
  A little-endian 14-bit Bayer pixel format with even rows ordered blue-green and odd rows ordered green-red.
- [vImageCVImageFormat.Format.format14Bayer_GBRG](./format/format14bayer_gbrg.md)
  A little-endian 14-bit Bayer pixel format with even rows ordered green-blue and odd rows ordered red-green.
- [vImageCVImageFormat.Format.format14Bayer_GRBG](./format/format14bayer_grbg.md)
  A little-endian 14-bit Bayer pixel format with even rows ordered green-red and odd rows ordered blue-green.
- [vImageCVImageFormat.Format.format14Bayer_RGGB](./format/format14bayer_rggb.md)
  A little-endian 14-bit Bayer pixel format with even rows ordered red-green and odd rows ordered green-blue.
### Indexed color format constants
- [vImageCVImageFormat.Format.format1Monochrome](./format/format1monochrome.md)
  A 1-bit indexed pixel format.
- [vImageCVImageFormat.Format.format1IndexedGray_WhiteIsZero](./format/format1indexedgray_whiteiszero.md)
  A 1-bit indexed pixel format with white equal to zero.
- [vImageCVImageFormat.Format.format2Indexed](./format/format2indexed.md)
  A 2-bit indexed pixel format.
- [vImageCVImageFormat.Format.format2IndexedGray_WhiteIsZero](./format/format2indexedgray_whiteiszero.md)
  A 2-bit indexed pixel format with white equal to zero.
- [vImageCVImageFormat.Format.format4Indexed](./format/format4indexed.md)
  A 4-bit indexed pixel format.
- [vImageCVImageFormat.Format.format4IndexedGray_WhiteIsZero](./format/format4indexedgray_whiteiszero.md)
  A 4-bit indexed pixel format with white equal to zero.
- [vImageCVImageFormat.Format.format8Indexed](./format/format8indexed.md)
  An 8-bit indexed pixel format.
- [vImageCVImageFormat.Format.format8IndexedGray_WhiteIsZero](./format/format8indexedgray_whiteiszero.md)
  An 8-bit indexed pixel format with white equal to zero.
### Depth format constants
- [vImageCVImageFormat.Format.formatDepthFloat16](./format/formatdepthfloat16.md)
  A 16-bit depth pixel format that describes the distance to an object in meters.
- [vImageCVImageFormat.Format.formatDepthFloat32](./format/formatdepthfloat32.md)
  A 32-bit depth pixel format that describes the distance to an object in meters.
### Disparity format constants
- [vImageCVImageFormat.Format.formatDisparityFloat16](./format/formatdisparityfloat16.md)
  A 16-bit disparity pixel format that describes the normalized shift when comparing two images.
- [vImageCVImageFormat.Format.formatDisparityFloat32](./format/formatdisparityfloat32.md)
  A 32-bit disparity pixel format that describes the normalized shift when comparing two images.
### Single-component format constants
- [vImageCVImageFormat.Format.formatOneComponent8](./format/formatonecomponent8.md)
  An 8-bit, single-component pixel format with black equal to zero.
- [vImageCVImageFormat.Format.formatOneComponent16Half](./format/formatonecomponent16half.md)
  A little-endian 16-bit, single-componennt pixel format.
- [vImageCVImageFormat.Format.formatOneComponent32Float](./format/formatonecomponent32float.md)
  A little-endian 32-bit, single-component pixel format.
### Two-component format constants
- [vImageCVImageFormat.Format.formatTwoComponent8](./format/formattwocomponent8.md)
  An 8-bit, two-component pixel format with black equal to zero.
- [vImageCVImageFormat.Format.formatTwoComponent16Half](./format/formattwocomponent16half.md)
  A little-endian 16-bit, two-component pixel format.
- [vImageCVImageFormat.Format.formatTwoComponent32Float](./format/formattwocomponent32float.md)
  A little-endian 32-bit, two-component pixel format.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Supporting types
- [vImageCVImageFormat.ChromaSiting](./chromasiting-swift.enum.md)
  Constants that specify the chrominance siting of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/format)*