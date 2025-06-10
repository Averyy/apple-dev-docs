# convert(lumaSource:chromaSource:conversionInfo:)

**Framework**: Accelerate  
**Kind**: method

Populates the pixel buffer with ARGB data from the given luminance and chrominance pixel buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func convert(lumaSource: vImage.PixelBuffer<vImage.Planar8>, chromaSource: vImage.PixelBuffer<vImage.Interleaved8x2>, conversionInfo: vImage_YpCbCrToARGB)
```

## Parameters

- `lumaSource`: The source luminance buffer.
- `chromaSource`: The source CbCr chrominance buffer.
- `conversionInfo`: An opaque representation of a 3 x 3 converson matrix for converting Y’CbCr signals to RGB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/convert(lumasource:chromasource:conversioninfo:))*