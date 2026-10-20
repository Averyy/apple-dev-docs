# destinationBuffers(colorSpace:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Returns a list of vImage destination buffer types, specifying the order of planes.

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
func destinationBuffers(colorSpace: CGColorSpace) -> [vImage.BufferType?]
```

## See Also

### Related Documentation
- [func vImageConverter_GetDestinationBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](../vimageconverter_getdestinationbufferorder%28_%29.md)
  Returns a list of vImage destination buffer channel names, specifying the order of planes.
### Instance Methods
- [func convert(source: vImage_Buffer, destination: inout vImage_Buffer, flags: vImage.Options) throws](./convert%28source,destination,flags%29.md)
  Converts the pixels in a vImage buffer to another format.
- [func mustOperateOutOfPlace(source: vImage_Buffer, destination: vImage_Buffer, flags: vImage.Options) throws -> Bool](./mustoperateoutofplace%28source,destination,flags%29.md)
  Determines whether a converter is capable of operating in place.
- [func sourceBuffers(colorSpace: CGColorSpace) -> [vImage.BufferType?]](./sourcebuffers%28colorspace%29.md)
  Returns a list of vImage source buffer types, specifying the order of planes.
- [func convert<Src, Dest>(from: vImage.PixelBuffer<Src>, to: vImage.PixelBuffer<Dest>) throws](./convert%28from,to%29-9s7p7.md)
- [func convert<F1, F2>(from: [vImage.PixelBuffer<F1>], to: [vImage.PixelBuffer<F2>]) throws](./convert%28from,to%29-587gc.md)
- [func makeCGToCVPixelBuffers(referencing: CVPixelBuffer) throws -> [vImage.PixelBuffer<vImage.DynamicPixelFormat>]](./makecgtocvpixelbuffers%28referencing%29.md)
- [func makeCVToCGPixelBuffers(referencing: CVPixelBuffer) throws -> [vImage.PixelBuffer<vImage.DynamicPixelFormat>]](./makecvtocgpixelbuffers%28referencing%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter/destinationbuffers(colorspace:))*