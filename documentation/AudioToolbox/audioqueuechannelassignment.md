# AudioQueueChannelAssignment

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioQueueChannelAssignment
```

## Topics

### Initializers
- [init(mDeviceUID: Unmanaged<CFString>, mChannelNumber: UInt32)](audioqueuechannelassignment/init(mdeviceuid:mchannelnumber:).md)
### Instance Properties
- [var mChannelNumber: UInt32](audioqueuechannelassignment/mchannelnumber.md)
- [var mDeviceUID: Unmanaged<CFString>](audioqueuechannelassignment/mdeviceuid.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioQueueProcessingTapFlags](audioqueueprocessingtapflags.md)
- [struct AudioQueueBuffer](audioqueuebuffer.md)
  Defines an audio queue buffer.
- [typealias AudioQueueBufferRef](audioqueuebufferref.md)
  A pointer to an audio queue buffer.
- [struct AudioQueueLevelMeterState](audioqueuelevelmeterstate.md)
  Specifies the current level metering information for one channel of an audio queue.
- [struct AudioQueueParameterEvent](audioqueueparameterevent.md)
  Specifies an audio queue parameter and associated value.
- [typealias AudioQueueParameterID](audioqueueparameterid.md)
  A `UInt32` value that uniquely identifies an audio queue parameter.
- [typealias AudioQueueParameterValue](audioqueueparametervalue.md)
  A `Float32` value for an audio queue parameter.
- [typealias AudioQueueProcessingTapCallback](audioqueueprocessingtapcallback.md)
- [typealias AudioQueueProcessingTapRef](audioqueueprocessingtapref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuechannelassignment)*