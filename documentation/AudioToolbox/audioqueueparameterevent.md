# AudioQueueParameterEvent

**Framework**: Audio Toolbox  
**Kind**: struct

Specifies an audio queue parameter and associated value.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioQueueParameterEvent
```

#### Overview

You use this structure with the [`AudioQueueEnqueueBufferWithParameters(_:_:_:_:_:_:_:_:_:_:)`](audioqueueenqueuebufferwithparameters(_:_:_:_:_:_:_:_:_:_:).md) function. See that function, and [`Audio Queue Parameters`](1552626-audio-queue-parameters.md), for more information.

## Topics

### Initializers
- [init()](audioqueueparameterevent/init.md)
- [init(mID: AudioQueueParameterID, mValue: AudioQueueParameterValue)](audioqueueparameterevent/init(mid:mvalue:).md)
### Instance Properties
- [var mID: AudioQueueParameterID](audioqueueparameterevent/mid.md)
  The parameter.
- [var mValue: AudioQueueParameterValue](audioqueueparameterevent/mvalue.md)
  The value of the specified parameter.

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
- [struct AudioQueueLevelMeterState](audioqueuelevelmeterstate.md)
  Specifies the current level metering information for one channel of an audio queue.
- [typealias AudioQueueParameterID](audioqueueparameterid.md)
  A `UInt32` value that uniquely identifies an audio queue parameter.
- [typealias AudioQueueParameterValue](audioqueueparametervalue.md)
  A `Float32` value for an audio queue parameter.
- [typealias AudioQueueProcessingTapCallback](audioqueueprocessingtapcallback.md)
- [typealias AudioQueueProcessingTapRef](audioqueueprocessingtapref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueparameterevent)*