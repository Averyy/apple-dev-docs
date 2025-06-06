# AudioQueueProcessingTapCallback

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioQueueProcessingTapCallback = (UnsafeMutableRawPointer, AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioQueueProcessingTapFlags>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> Void
```

## See Also

- [struct AudioQueueChannelAssignment](audioqueuechannelassignment.md)
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
- [typealias AudioQueueProcessingTapRef](audioqueueprocessingtapref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapcallback)*