# PHASEPushStreamBufferOptions

**Framework**: PHASE  
**Kind**: struct

Options that inform PHASE of an audio-stream buffer’s playback priority.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct PHASEPushStreamBufferOptions
```

#### Overview

When your app provides audio buffers that PHASE plays through a [`PHASEPushStreamNode`](phasepushstreamnode.md), use this structure to inform PHASE of a particular buffer’s priority.

Associate an option to a particular buffer by passing it in to the [`scheduleBuffer(buffer:time:options:)`](phasepushstreamnode/schedulebuffer(buffer:time:options:).md) function of a [`PHASEPushStreamNode`](phasepushstreamnode.md).

## Topics

### Creating an Option
- [init(rawValue: UInt)](phasepushstreambufferoptions/init(rawvalue:).md)
  Creates a push stream buffer option with the given raw value.
### Options
- [static var `default`: PHASEPushStreamBufferOptions](phasepushstreambufferoptions/default.md)
  Indicates a buffer processes after existing buffers in the queue.
- [static var interrupts: PHASEPushStreamBufferOptions](phasepushstreambufferoptions/interrupts.md)
  Indicates a buffer begins processing immediately.
- [static var interruptsAtLoop: PHASEPushStreamBufferOptions](phasepushstreambufferoptions/interruptsatloop.md)
  Indicates a buffer begins processing when an existing buffer loops.
- [static var loops: PHASEPushStreamBufferOptions](phasepushstreambufferoptions/loops.md)
  Indicates a buffer restarts after it finishes processing.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class PHASESamplerNodeDefinition](phasesamplernodedefinition.md)
  A node that plays complete audio data.
- [enum PHASEPlaybackMode](phaseplaybackmode.md)
  Loop options for audio playback.
- [class PHASEPushStreamNodeDefinition](phasepushstreamnodedefinition.md)
  A node that plays a sequence of audio buffers.
- [class PHASEPushStreamNode](phasepushstreamnode.md)
  An audio stream you manage to provide a sound buffer data.
- [enum PHASECalibrationMode](phasecalibrationmode.md)
  Calibration options for sound pressure level.
- [class PHASEGeneratorNodeDefinition](phasegeneratornodedefinition.md)
  A base class for nodes that provide audio data to generate sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreambufferoptions)*