# MTL4MachineLearningPipelineState

**Framework**: Metal  
**Kind**: protocol

A pipeline state that you can use with machine-learning encoder instances.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4MachineLearningPipelineState : MTLAllocation, Sendable
```

#### Overview

See [`MTL4MachineLearningCommandEncoder`](mtl4machinelearningcommandencoder.md) for more information.

## Topics

### Instance Properties
- [var device: any MTLDevice](mtl4machinelearningpipelinestate/device.md)
  Returns the device the pipeline state belongs to.
- [var intermediatesHeapSize: Int](mtl4machinelearningpipelinestate/intermediatesheapsize.md)
  Obtain the size of the heap, in bytes, this pipeline requires during the execution.
- [var label: String?](mtl4machinelearningpipelinestate/label.md)
  Queries the string that helps identify this object.
- [var reflection: MTL4MachineLearningPipelineReflection?](mtl4machinelearningpipelinestate/reflection.md)
  Returns reflection information for this machine learning pipeline state.

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Running a machine learning model on the GPU timeline](running-a-machine-learning-model-on-the-gpu-timeline.md)
  Dispatch model inference commands with a machine learning pass in a Metal 4 command buffer.
- [protocol MTL4MachineLearningCommandEncoder](mtl4machinelearningcommandencoder.md)
  Encodes machine learning model inference commands for a single pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinestate)*