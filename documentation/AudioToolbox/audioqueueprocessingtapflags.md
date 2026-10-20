# AudioQueueProcessingTapFlags

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct AudioQueueProcessingTapFlags
```

```c
enum AudioQueueProcessingTapFlags : UInt32;
```

## Topics

### Constants
- [static var endOfStream: AudioQueueProcessingTapFlags](./audioqueueprocessingtapflags/endofstream.md)
- [static var postEffects: AudioQueueProcessingTapFlags](./audioqueueprocessingtapflags/posteffects.md)
- [static var preEffects: AudioQueueProcessingTapFlags](./audioqueueprocessingtapflags/preeffects.md)
- [static var siphon: AudioQueueProcessingTapFlags](./audioqueueprocessingtapflags/siphon.md)
- [static var startOfStream: AudioQueueProcessingTapFlags](./audioqueueprocessingtapflags/startofstream.md)
### Initializers
- [init(rawValue: UInt32)](./audioqueueprocessingtapflags/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Data Types
- [struct AudioQueueChannelAssignment](./audioqueuechannelassignment.md)
- [struct AudioQueueBuffer](./audioqueuebuffer.md)
  Defines an audio queue buffer.
- [typealias AudioQueueBufferRef](./audioqueuebufferref.md)
  A pointer to an audio queue buffer.
- [struct AudioQueueLevelMeterState](./audioqueuelevelmeterstate.md)
  Specifies the current level metering information for one channel of an audio queue.
- [struct AudioQueueParameterEvent](./audioqueueparameterevent.md)
  Specifies an audio queue parameter and associated value.
- [typealias AudioQueueParameterID](./audioqueueparameterid.md)
  A `UInt32` value that uniquely identifies an audio queue parameter.
- [typealias AudioQueueParameterValue](./audioqueueparametervalue.md)
  A `Float32` value for an audio queue parameter.
- [typealias AudioQueueProcessingTapCallback](./audioqueueprocessingtapcallback.md)
- [typealias AudioQueueProcessingTapRef](./audioqueueprocessingtapref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags)*