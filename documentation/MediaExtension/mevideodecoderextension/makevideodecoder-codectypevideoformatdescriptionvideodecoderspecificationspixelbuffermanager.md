# makeVideoDecoder(codecType:videoFormatDescription:videoDecoderSpecifications:pixelBufferManager:)

**Framework**: MediaExtension  
**Kind**: method  
**Required**: Yes

Creates a new video decoder that matches the codec type, format description, decoder specifications, and pixel buffer manager that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func makeVideoDecoder(codecType: CMVideoCodecType, videoFormatDescription: CMVideoFormatDescription, videoDecoderSpecifications: [String : Any], pixelBufferManager extensionDecoderPixelBufferManager: MEVideoDecoderPixelBufferManager) throws -> any MEVideoDecoder
```

#### Return Value

A new [`MEVideoDecoder`](mevideodecoder.md).

#### Discussion

The `videoDecoderSpecifications` parameter accepts the following keys:

- [`kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder`](https://developer.apple.com/documentation/VideoToolbox/kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder)
- [`kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder`](https://developer.apple.com/documentation/VideoToolbox/kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder)
- [`kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID`](https://developer.apple.com/documentation/VideoToolbox/kVTVideoDecoderSpecification_RequiredDecoderGPURegistryID)
- [`kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID`](https://developer.apple.com/documentation/VideoToolbox/kVTVideoDecoderSpecification_PreferredDecoderGPURegistryID)

If the parameter values aren’t compatible with the video decoder, this method fails with the error [`MEError.Code.unsupportedFeature`](meerror-swift.struct/code/unsupportedfeature.md).

The video decoder needs to retain the pixel buffer manager and use it to allocate and configure output pixel buffers.

## Parameters

- `codecType`: The codec type for the requested decoder.
- `videoFormatDescription`: An object that describes the video data.
- `videoDecoderSpecifications`: A dictionary that contains video decoder specification values, which may be empty. See   for a list of keys to use.
- `extensionDecoderPixelBufferManager`: A pixel buffer manager.

## See Also

- [init()](mevideodecoderextension/init.md)
  Creates a new video decoder factory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoderextension/makevideodecoder(codectype:videoformatdescription:videodecoderspecifications:pixelbuffermanager:))*