# sourceBuffers(colorSpace:)

**Framework**: Accelerate  
**Kind**: method

Returns a list of vImage source buffer types, specifying the order of planes.

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
func sourceBuffers(colorSpace: CGColorSpace) -> [vImage.BufferType?]
```

## See Also

- [func vImageConverter_GetSourceBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](vimageconverter_getsourcebufferorder(_:).md)
  Returns a list of vImage source buffer channel names, specifying the order of planes.
- [func convert(source: vImage_Buffer, destination: inout vImage_Buffer, flags: vImage.Options) throws](vimageconverter/convert(source:destination:flags:).md)
  Converts the pixels in a vImage buffer to another format.
- [func mustOperateOutOfPlace(source: vImage_Buffer, destination: vImage_Buffer, flags: vImage.Options) throws -> Bool](vimageconverter/mustoperateoutofplace(source:destination:flags:).md)
  Determines whether a converter is capable of operating in place.
- [func destinationBuffers(colorSpace: CGColorSpace) -> [vImage.BufferType?]](vimageconverter/destinationbuffers(colorspace:).md)
  Returns a list of vImage destination buffer types, specifying the order of planes.
- [func convert<Src, Dest>(from: vImage.PixelBuffer<Src>, to: vImage.PixelBuffer<Dest>) throws](vimageconverter/convert(from:to:)-9s7p7.md)
- [func convert<F1, F2>(from: [vImage.PixelBuffer<F1>], to: [vImage.PixelBuffer<F2>]) throws](vimageconverter/convert(from:to:)-587gc.md)
- [func makeCGToCVPixelBuffers(referencing: CVPixelBuffer) throws -> [vImage.PixelBuffer<vImage.DynamicPixelFormat>]](vimageconverter/makecgtocvpixelbuffers(referencing:).md)
- [func makeCVToCGPixelBuffers(referencing: CVPixelBuffer) throws -> [vImage.PixelBuffer<vImage.DynamicPixelFormat>]](vimageconverter/makecvtocgpixelbuffers(referencing:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter/sourcebuffers(colorspace:))*