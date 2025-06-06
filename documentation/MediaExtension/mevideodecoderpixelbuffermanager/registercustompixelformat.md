# registerCustomPixelFormat(_:)

**Framework**: MediaExtension  
**Kind**: method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func registerCustomPixelFormat(_ customPixelFormat: [String : Any])
```

#### Discussion

This property is appropriate for decoders which produce output in a custom pixel format. This will generally only be used by decoders which produce RAW output, where the decoder’s output buffers will only be consumed by an [`MERAWProcessor`](merawprocessor.md) extension which registers the same pixel format. The [`MERAWProcessor`](merawprocessor.md) needs to manually register the custom pixel format using [`CVPixelFormatDescriptionCreateWithPixelFormatType(_:_:)`](https://developer.apple.com/documentation/CoreVideo/CVPixelFormatDescriptionCreateWithPixelFormatType(_:_:)).

## Parameters

- `customPixelFormat`: A dictionary containing a set of keys and values as described in   suitable for providing as the ‘description’ parameter to  .  This must contain the custom pixel format fourCC as the value for the   key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoderpixelbuffermanager/registercustompixelformat(_:))*