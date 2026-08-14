# AudioQueueProcessingTapFlags

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
struct AudioQueueProcessingTapFlags
```

## Topics

### Constants
- [static var endOfStream: AudioQueueProcessingTapFlags](audioqueueprocessingtapflags/endofstream.md)
- [static var postEffects: AudioQueueProcessingTapFlags](audioqueueprocessingtapflags/posteffects.md)
- [static var preEffects: AudioQueueProcessingTapFlags](audioqueueprocessingtapflags/preeffects.md)
- [static var siphon: AudioQueueProcessingTapFlags](audioqueueprocessingtapflags/siphon.md)
- [static var startOfStream: AudioQueueProcessingTapFlags](audioqueueprocessingtapflags/startofstream.md)
### Initializers
- [init(rawValue: UInt32)](audioqueueprocessingtapflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [struct AudioQueueChannelAssignment](audioqueuechannelassignment.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags)*