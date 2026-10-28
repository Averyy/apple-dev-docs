# outputColorAttachments

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

Returns the color-related Core Video image buffer keys and values that become attachments to the output pixel buffers.

**Availability**:
- macOS 15.0+

## Declaration

```swift
optional var outputColorAttachments: [String : Any] { get }
```

```objc
@property (readonly) NSDictionary<NSString *,id> * outputColorAttachments;
```

## Discussion

This is an optional property. Only color-related keys from [Image Buffer Attachment Keys](../../CoreVideo/image-buffer-attachment-keys.md) are permitted in the returned dictionary.

## See Also

### Inspecting a RAW processor
- [var metalDeviceRegistryID: UInt64](./metaldeviceregistryid.md)
  Requests the processor use the provided Metal device for processing.
- [var processingParameters: [MERAWProcessingParameter]](./processingparameters.md)
  Provides a list of processing parameters that can be changed by the client of Video Toolbox session to influence processing behavior.
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  Indicates the readiness of the processor to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessor/outputcolorattachments)*