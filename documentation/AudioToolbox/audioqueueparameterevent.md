# AudioQueueParameterEvent

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

Specifies an audio queue parameter and associated value.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct AudioQueueParameterEvent
```

```c
struct AudioQueueParameterEvent;
```

## Overview

You use this structure with the [`AudioQueueEnqueueBufferWithParameters(_:_:_:_:_:_:_:_:_:_:)`](./audioqueueenqueuebufferwithparameters%28_,_,_,_,_,_,_,_,_,_%29.md) function. See that function, and [Audio Queue Parameters](./api-1552626-audio-queue-parameters.md), for more information.

## Topics

### Initializers
- [init()](./audioqueueparameterevent/init%28%29.md)
- [init(mID: AudioQueueParameterID, mValue: AudioQueueParameterValue)](./audioqueueparameterevent/init%28mid,mvalue%29.md)
### Instance Properties
- [var mID: AudioQueueParameterID](./audioqueueparameterevent/mid.md)
  The parameter.
- [var mValue: AudioQueueParameterValue](./audioqueueparameterevent/mvalue.md)
  The value of the specified parameter.

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
- [struct AudioQueueLevelMeterState](./audioqueuelevelmeterstate.md)
  Specifies the current level metering information for one channel of an audio queue.
- [typealias AudioQueueParameterID](./audioqueueparameterid.md)
  A `UInt32` value that uniquely identifies an audio queue parameter.
- [typealias AudioQueueParameterValue](./audioqueueparametervalue.md)
  A `Float32` value for an audio queue parameter.
- [typealias AudioQueueProcessingTapCallback](./audioqueueprocessingtapcallback.md)
- [typealias AudioQueueProcessingTapRef](./audioqueueprocessingtapref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueparameterevent)*