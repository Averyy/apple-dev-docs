# AudioQueueLevelMeterState

**Framework**: Audio Toolbox  
**Kind**: struct

Specifies the current level metering information for one channel of an audio queue.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioQueueLevelMeterState
```

## Topics

### Initializers
- [init()](audioqueuelevelmeterstate/init.md)
- [init(mAveragePower: Float32, mPeakPower: Float32)](audioqueuelevelmeterstate/init(maveragepower:mpeakpower:).md)
### Instance Properties
- [var mAveragePower: Float32](audioqueuelevelmeterstate/maveragepower.md)
  The audio channel’s average RMS power.
- [var mPeakPower: Float32](audioqueuelevelmeterstate/mpeakpower.md)
  The audio channel’s peak RMS power.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AudioQueueChannelAssignment](audioqueuechannelassignment.md)
- [struct AudioQueueProcessingTapFlags](audioqueueprocessingtapflags.md)
- [struct AudioQueueBuffer](audioqueuebuffer.md)
  Defines an audio queue buffer.
- [typealias AudioQueueBufferRef](audioqueuebufferref.md)
  A pointer to an audio queue buffer.
- [struct AudioQueueParameterEvent](audioqueueparameterevent.md)
  Specifies an audio queue parameter and associated value.
- [typealias AudioQueueParameterID](audioqueueparameterid.md)
  A `UInt32` value that uniquely identifies an audio queue parameter.
- [typealias AudioQueueParameterValue](audioqueueparametervalue.md)
  A `Float32` value for an audio queue parameter.
- [typealias AudioQueueProcessingTapCallback](audioqueueprocessingtapcallback.md)
- [typealias AudioQueueProcessingTapRef](audioqueueprocessingtapref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuelevelmeterstate)*