# PHASEPushStreamBufferOptions

**Framework**: PHASE  
**Kind**: struct  
**Role**: Structure

Options that inform PHASE of an audio-stream buffer’s playback priority.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct PHASEPushStreamBufferOptions
```

```c
enum PHASEPushStreamBufferOptions : NSUInteger;
```

#### Overview

When your app provides audio buffers that PHASE plays through a [`PHASEPushStreamNode`](./phasepushstreamnode.md), use this structure to inform PHASE of a particular buffer’s priority.

Associate an option to a particular buffer by passing it in to the [`scheduleBuffer(buffer:time:options:)`](./phasepushstreamnode/schedulebuffer%28buffer,time,options%29.md) function of a [`PHASEPushStreamNode`](./phasepushstreamnode.md).

## Topics

### Creating an Option
- [init(rawValue: UInt)](./phasepushstreambufferoptions/init%28rawvalue%29.md)
  Creates a push stream buffer option with the given raw value.
### Options
- [static var `default`: PHASEPushStreamBufferOptions](./phasepushstreambufferoptions/default.md)
  Indicates a buffer processes after existing buffers in the queue.
- [static var interrupts: PHASEPushStreamBufferOptions](./phasepushstreambufferoptions/interrupts.md)
  Indicates a buffer begins processing immediately.
- [static var interruptsAtLoop: PHASEPushStreamBufferOptions](./phasepushstreambufferoptions/interruptsatloop.md)
  Indicates a buffer begins processing when an existing buffer loops.
- [static var loops: PHASEPushStreamBufferOptions](./phasepushstreambufferoptions/loops.md)
  Indicates a buffer restarts after it finishes processing.

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

### Audio-Providing Nodes
- [class PHASESamplerNodeDefinition](./phasesamplernodedefinition.md)
  A node that plays complete audio data.
- [enum PHASEPlaybackMode](./phaseplaybackmode.md)
  Loop options for audio playback.
- [class PHASEPushStreamNodeDefinition](./phasepushstreamnodedefinition.md)
  A node that plays a sequence of audio buffers.
- [class PHASEPushStreamNode](./phasepushstreamnode.md)
  An audio stream you manage to provide a sound buffer data.
- [enum PHASECalibrationMode](./phasecalibrationmode.md)
  Calibration options for sound pressure level.
- [class PHASEGeneratorNodeDefinition](./phasegeneratornodedefinition.md)
  A base class for nodes that provide audio data to generate sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreambufferoptions)*