# registerCustomPixelFormat(_:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func registerCustomPixelFormat(_ customPixelFormat: [String : Any])
```

```objc
- (void) registerCustomPixelFormat:(NSDictionary<NSString *,id> *) customPixelFormat;
```

## Discussion

This property is appropriate for decoders which produce output in a custom pixel format. This will generally only be used by decoders which produce RAW output, where the decoder’s output buffers will only be consumed by an [`MERAWProcessor`](../merawprocessor.md) extension which registers the same pixel format. The [`MERAWProcessor`](../merawprocessor.md) needs to manually register the custom pixel format using [`CVPixelFormatDescriptionCreateWithPixelFormatType(_:_:)`](../../CoreVideo/cvpixelformatdescriptioncreatewithpixelformattype%28_,_%29.md).

## Parameters

- `customPixelFormat`: A dictionary containing a set of keys and values as described in [`CVPixelFormatDescription`](../../CoreVideo/cvpixelformatdescription.md) suitable for providing as the ‘description’ parameter to [`CVPixelFormatDescriptionCreateWithPixelFormatType(_:_:)`](../../CoreVideo/cvpixelformatdescriptioncreatewithpixelformattype%28_,_%29.md).  This must contain the custom pixel format fourCC as the value for the `kCVPixelFormatCodecType` key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoderpixelbuffermanager/registercustompixelformat(_:))*