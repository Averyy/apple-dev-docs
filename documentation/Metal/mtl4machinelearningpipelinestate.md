# MTL4MachineLearningPipelineState

**Framework**: Metal  
**Kind**: protocol

A pipeline state that you can use with machine-learning encoder instances.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MTL4MachineLearningCommandEncoder](mtl4machinelearningcommandencoder.md)
  Encodes dispatch commands that run machine-learning model inference on Apple silicon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinestate)*