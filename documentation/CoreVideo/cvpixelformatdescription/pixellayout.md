# CVPixelFormatDescription.PixelLayout

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

Defines pixel layout of a buffer plane or the entire buffer if the format is non-planar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct PixelLayout
```

#### Overview

Note: The value of [`fillExtendedPixels`](./pixellayout/fillextendedpixels.md) property is ignored when comparing two pixel layouts for equality.

## Topics

### Initializers
- [init(blockSize: CVImageSize, bitsPerBlock: Int, bitsPerComponent: Int?, blockAlignment: CVPixelFormatDescription.Dimensions, subsampling: CVPixelFormatDescription.Dimensions, blackBlock: Data?, fillExtendedPixels: ((inout CVMutablePixelBuffer) -> Void)?, cgBitmapInfo: CGBitmapInfo?)](./pixellayout/init%28blocksize,bitsperblock,bitspercomponent,blockalignment,subsampling,blackblock,fillextendedpixels,cgbitmapinfo%29.md)
### Instance Properties
- [var bitsPerBlock: Int](./pixellayout/bitsperblock.md)
  Number of bits per pixel. If [`blockSize`](./pixellayout/blocksize.md) is greater than (1, 1) then this represents bits per block.
- [var bitsPerComponent: Int?](./pixellayout/bitspercomponent.md)
  The logical bit depth of each component of the plane.
- [var blackBlock: Data?](./pixellayout/blackblock.md)
  The bit pattern for a block of black pixels.  If absent, black is assumed to be all zeros. Otherwise, this should be [`bitsPerBlock`](./pixellayout/bitsperblock.md) bits long. If bitsPerBlock is less than a byte, repeat the bit pattern for the full byte.
- [var blockAlignment: CVPixelFormatDescription.Dimensions](./pixellayout/blockalignment.md)
  Alignment requirements on block multiples. v210 would be (8, 1) here for the horizontal case, to match the standard v210 row alignment value of 48.
- [var blockSize: CVImageSize](./pixellayout/blocksize.md)
  Used to assist with allocating memory for pixel formats that don’t have an integer value for bytes per pixel. Block width/height is essentially the width/height in pixels of the smallest “byte addressable” group of pixels. This works in close conjunction with [`bitsPerBlock`](./pixellayout/bitsperblock.md). Examples: 8-bit luminance only, blockSize.width would be 1, bitsPerBlock would be 8 16-bit 1555 RGB, blockSize.width would be 1, bitsPerBlock would be 16 32-bit 8888 ARGB, blockSize.width would be 1, bitsPerBlock would be 32 2vuy (CbYCrY), blockSize.width would be 2, bitsPerBlock would be 32 1-bit bitmap, blockSize.width would be 8, bitsPerBlock would be 8 v210, blockSize.width would be 6, bitsPerBlock would be 128
- [var cgBitmapInfo: CGBitmapInfo?](./pixellayout/cgbitmapinfo.md)
  CoreGraphics bitmap info used for CG compatibility.
- [var fillExtendedPixels: ((inout CVMutablePixelBuffer) -> Void)?](./pixellayout/fillextendedpixels.md)
  Callback which can replicate edge pixels to the extended pixels.
- [var subsampling: CVPixelFormatDescription.Dimensions](./pixellayout/subsampling.md)
  Pixel subsampling for this plane.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/pixellayout)*