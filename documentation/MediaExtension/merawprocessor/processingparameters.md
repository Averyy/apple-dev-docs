# processingParameters

**Framework**: MediaExtension  
**Kind**: property  
**Required**: Yes

Provides a list of processing parameters that can be changed by the client of Video Toolbox session to influence processing behavior.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var processingParameters: [MERAWProcessingParameter] { get }
```

#### Discussion

This property value is an array of [`MERAWProcessingParameter`](merawprocessingparameter.md) objects, each describing the parameter and providing an interface where the processing parameter value may be modified.

## See Also

- [var metalDeviceRegistryID: UInt64](merawprocessor/metaldeviceregistryid.md)
  Requests the processor use the provided Metal device for processing.
- [var outputColorAttachments: [String : Any]](merawprocessor/outputcolorattachments.md)
  Returns the color-related Core Video image buffer keys and values that become attachments to the output pixel buffers.
- [var isReadyForMoreMediaData: Bool](merawprocessor/isreadyformoremediadata.md)
  Indicates the readiness of the processor to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessor/processingparameters)*