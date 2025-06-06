# outputColorAttachments

**Framework**: MediaExtension  
**Kind**: property

Returns the color-related Core Video image buffer keys and values that become attachments to the output pixel buffers.

**Availability**:
- macOS 15.0+

## Declaration

```swift
optional var outputColorAttachments: [String : Any] { get }
```

#### Discussion

This is an optional property. Only color-related keys from [`Image Buffer Attachment Keys`](https://developer.apple.com/documentation/CoreVideo/image-buffer-attachment-keys) are permitted in the returned dictionary.

## See Also

- [var metalDeviceRegistryID: UInt64](merawprocessor/metaldeviceregistryid.md)
  Requests the processor use the provided Metal device for processing.
- [var processingParameters: [MERAWProcessingParameter]](merawprocessor/processingparameters.md)
  Provides a list of processing parameters that can be changed by the client of Video Toolbox session to influence processing behavior.
- [var isReadyForMoreMediaData: Bool](merawprocessor/isreadyformoremediadata.md)
  Indicates the readiness of the processor to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessor/outputcolorattachments)*