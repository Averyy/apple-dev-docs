# AudioQueueLevelMeterState

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

Specifies the current level metering information for one channel of an audio queue.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct AudioQueueLevelMeterState
```

```c
typedef struct AudioQueueLevelMeterState { ... } AudioQueueLevelMeterState;
```

## Topics

### Initializers
- [init()](./audioqueuelevelmeterstate/init%28%29.md)
- [init(mAveragePower: Float32, mPeakPower: Float32)](./audioqueuelevelmeterstate/init%28maveragepower,mpeakpower%29.md)
### Instance Properties
- [var mAveragePower: Float32](./audioqueuelevelmeterstate/maveragepower.md)
  The audio channel’s average RMS power.
- [var mPeakPower: Float32](./audioqueuelevelmeterstate/mpeakpower.md)
  The audio channel’s peak RMS power.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Data Types
- [struct AudioQueueChannelAssignment](./audioqueuechannelassignment.md)
- [struct AudioQueueProcessingTapFlags](./audioqueueprocessingtapflags.md)
- [struct AudioQueueBuffer](./audioqueuebuffer.md)
  Defines an audio queue buffer.
- [typealias AudioQueueBufferRef](./audioqueuebufferref.md)
  A pointer to an audio queue buffer.
- [struct AudioQueueParameterEvent](./audioqueueparameterevent.md)
  Specifies an audio queue parameter and associated value.
- [typealias AudioQueueParameterID](./audioqueueparameterid.md)
  A `UInt32` value that uniquely identifies an audio queue parameter.
- [typealias AudioQueueParameterValue](./audioqueueparametervalue.md)
  A `Float32` value for an audio queue parameter.
- [typealias AudioQueueProcessingTapCallback](./audioqueueprocessingtapcallback.md)
- [typealias AudioQueueProcessingTapRef](./audioqueueprocessingtapref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuelevelmeterstate)*