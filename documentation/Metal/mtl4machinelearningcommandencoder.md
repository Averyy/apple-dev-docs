# MTL4MachineLearningCommandEncoder

**Framework**: Metal  
**Kind**: protocol

Encodes machine-learning model inference commands for a single pass.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4MachineLearningCommandEncoder : MTL4CommandEncoder
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Overview

Create a machine learning encoder by calling a factory method of an [`MTL4CommandBuffer`](mtl4commandbuffer.md) instance, such as [`makeMachineLearningCommandEncoder()`](mtl4commandbuffer/makemachinelearningcommandencoder().md).

The [`dispatchNetwork(intermediatesHeap:)`](mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap:).md) method applies to the [`machineLearning`](mtlstages/machinelearning.md) stage of a machine learning pass. For more information about stages and synchronization, see [`MTLStages`](mtlstages.md) and [`Resource synchronization`](resource-synchronization.md).

## Topics

### Configuring the pass
- [func setPipelineState(any MTL4MachineLearningPipelineState)](mtl4machinelearningcommandencoder/setpipelinestate(_:).md)
  Configures the encoder with a machine learning pipeline state instance.
- [func setArgumentTable(any MTL4ArgumentTable)](mtl4machinelearningcommandencoder/setargumenttable(_:).md)
  Sets an argument table for the command encoder’s machine learning shader stage.
### Running machine learning networks
- [func dispatchNetwork(intermediatesHeap: any MTLHeap)](mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap:).md)
  Dispatches a machine learning network using the current pipeline state and argument table.

## Relationships

### Inherits From
- [MTL4CommandEncoder](mtl4commandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTL4MachineLearningPipelineState](mtl4machinelearningpipelinestate.md)
  A pipeline state that you can use with machine-learning encoder instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder)*