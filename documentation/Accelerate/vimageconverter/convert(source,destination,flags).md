# convert(source:destination:flags:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Converts the pixels in a vImage buffer to another format.

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
func convert(source: vImage_Buffer, destination: inout vImage_Buffer, flags options: vImage.Options = .noFlags) throws
```

## Mentions

- [Building a basic image conversion workflow](../building-a-basic-image-conversion-workflow.md)

## See Also

### Related Documentation
- [func vImageConvert_AnyToAny(vImageConverter, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](../vimageconvert_anytoany%28_,_,_,_,_%29.md)
  Converts the pixels in a vImage buffer to another format, using the specified converter.
### Instance Methods
- [func mustOperateOutOfPlace(source: vImage_Buffer, destination: vImage_Buffer, flags: vImage.Options) throws -> Bool](./mustoperateoutofplace%28source,destination,flags%29.md)
  Determines whether a converter is capable of operating in place.
- [func destinationBuffers(colorSpace: CGColorSpace) -> [vImage.BufferType?]](./destinationbuffers%28colorspace%29.md)
  Returns a list of vImage destination buffer types, specifying the order of planes.
- [func sourceBuffers(colorSpace: CGColorSpace) -> [vImage.BufferType?]](./sourcebuffers%28colorspace%29.md)
  Returns a list of vImage source buffer types, specifying the order of planes.
- [func convert<Src, Dest>(from: vImage.PixelBuffer<Src>, to: vImage.PixelBuffer<Dest>) throws](./convert%28from,to%29-9s7p7.md)
- [func convert<F1, F2>(from: [vImage.PixelBuffer<F1>], to: [vImage.PixelBuffer<F2>]) throws](./convert%28from,to%29-587gc.md)
- [func makeCGToCVPixelBuffers(referencing: CVPixelBuffer) throws -> [vImage.PixelBuffer<vImage.DynamicPixelFormat>]](./makecgtocvpixelbuffers%28referencing%29.md)
- [func makeCVToCGPixelBuffers(referencing: CVPixelBuffer) throws -> [vImage.PixelBuffer<vImage.DynamicPixelFormat>]](./makecvtocgpixelbuffers%28referencing%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter/convert(source:destination:flags:))*