# isReadyForMoreMediaData

**Framework**: MediaExtension  
**Kind**: property  
**Required**: Yes

Indicates the readiness of the processor to accept more sample buffers.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var isReadyForMoreMediaData: Bool { get }
```

#### Discussion

An [`MERAWProcessor`](merawprocessor.md) operates asynchronously and often has a fixed capacity for buffers in flight in the processor. This property allows the processor to signal to [`Video Toolbox`](https://developer.apple.com/documentation/VideoToolbox) that its internal buffers are full and cannot accept more samples. The processor must use [`MERAWProcessorReadyForMoreMediaDataDidChangeNotification`](merawprocessorreadyformoremediadatadidchangenotification.md) to notify Video Toolbox when this property changes.

## See Also

- [var metalDeviceRegistryID: UInt64](merawprocessor/metaldeviceregistryid.md)
  Requests the processor use the provided Metal device for processing.
- [var outputColorAttachments: [String : Any]](merawprocessor/outputcolorattachments.md)
  Returns the color-related Core Video image buffer keys and values that become attachments to the output pixel buffers.
- [var processingParameters: [MERAWProcessingParameter]](merawprocessor/processingparameters.md)
  Provides a list of processing parameters that can be changed by the client of Video Toolbox session to influence processing behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessor/isreadyformoremediadata)*