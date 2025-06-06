# metalDeviceRegistryID

**Framework**: MediaExtension  
**Kind**: property

Requests the processor use the provided Metal device for processing.

**Availability**:
- macOS 15.0+

## Declaration

```swift
optional var metalDeviceRegistryID: UInt64 { get set }
```

#### Discussion

This optional property requests that [`MERAWProcessor`](merawprocessor.md) use `MTLDevice` corresponding to this ID for any Metal-based processing. This is optional and doesn’t need to be implemented if the processor does not use Metal.

## See Also

- [var outputColorAttachments: [String : Any]](merawprocessor/outputcolorattachments.md)
  Returns the color-related Core Video image buffer keys and values that become attachments to the output pixel buffers.
- [var processingParameters: [MERAWProcessingParameter]](merawprocessor/processingparameters.md)
  Provides a list of processing parameters that can be changed by the client of Video Toolbox session to influence processing behavior.
- [var isReadyForMoreMediaData: Bool](merawprocessor/isreadyformoremediadata.md)
  Indicates the readiness of the processor to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessor/metaldeviceregistryid)*