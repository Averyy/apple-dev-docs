# MTL4MachineLearningCommandEncoder

**Framework**: Metal  
**Kind**: protocol

Encodes commands for dispatching machine learning networks on the GPU.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol MTL4MachineLearningCommandEncoder : MTL4CommandEncoder
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

## Topics

### Instance Methods
- [func dispatchNetwork(intermediatesHeap: any MTLHeap)](mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap:).md)
  Dispatches a machine learning network using the current pipeline state and argument table.
- [func setArgumentTable(any MTL4ArgumentTable)](mtl4machinelearningcommandencoder/setargumenttable(_:).md)
  Sets an argument table for the command encoder’s machine learning shader stage.
- [func setPipelineState(any MTL4MachineLearningPipelineState)](mtl4machinelearningcommandencoder/setpipelinestate(_:).md)
  Configures the encoder with a machine learning pipeline state instance.

## Relationships

### Inherits From
- [MTL4CommandEncoder](mtl4commandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTL4MachineLearningPipelineState](mtl4machinelearningpipelinestate.md)
  A pipeline state that you can use with machine-learning encoder instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder)*