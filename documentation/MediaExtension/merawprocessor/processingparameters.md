# processingParameters

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Provides a list of processing parameters that can be changed by the client of Video Toolbox session to influence processing behavior.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var processingParameters: [MERAWProcessingParameter] { get }
```

```objc
@property (readonly) NSArray<MERAWProcessingParameter *> * processingParameters;
```

#### Discussion

This property value is an array of [`MERAWProcessingParameter`](../merawprocessingparameter.md) objects, each describing the parameter and providing an interface where the processing parameter value may be modified.

## See Also

### Inspecting a RAW processor
- [var metalDeviceRegistryID: UInt64](./metaldeviceregistryid.md)
  Requests the processor use the provided Metal device for processing.
- [var outputColorAttachments: [String : Any]](./outputcolorattachments.md)
  Returns the color-related Core Video image buffer keys and values that become attachments to the output pixel buffers.
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  Indicates the readiness of the processor to accept more sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessor/processingparameters)*