# MTL4MachineLearningPipelineDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

Description for a machine learning pipeline state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTL4MachineLearningPipelineDescriptor
```

```objc
@interface MTL4MachineLearningPipelineDescriptor : MTL4PipelineDescriptor
```

## Topics

### Instance Properties
- [var label: String?](./mtl4machinelearningpipelinedescriptor/label.md)
  Assigns an optional string that helps identify pipeline states you create from this descriptor.
- [var machineLearningFunctionDescriptor: MTL4FunctionDescriptor?](./mtl4machinelearningpipelinedescriptor/machinelearningfunctiondescriptor.md)
  Assigns the function that the machine learning pipeline you create from this descriptor executes.
### Instance Methods
- [func inputDimensions(bufferIndex: Int) -> MTLTensorExtents?](./mtl4machinelearningpipelinedescriptor/inputdimensions%28bufferindex%29.md)
  Obtains the dimensions of the input tensor at `bufferIndex` if set, `nil` otherwise.
- [func reset()](./mtl4machinelearningpipelinedescriptor/reset%28%29.md)
  Resets the descriptor to its default values.
- [func setInputDimensions(MTLTensorExtents?, bufferIndex: Int)](./mtl4machinelearningpipelinedescriptor/setinputdimensions%28_,bufferindex%29-34gir.md)
  Sets the dimension of an input tensor at a buffer index.
- [func setInputDimensions([MTLTensorExtents], bufferIndex: Int)](./mtl4machinelearningpipelinedescriptor/setinputdimensions%28_,bufferindex%29-8fnq7.md)
  Sets the dimensions of multiple input tensors on a range of buffer bindings.
- [- setInputDimensions:withRange:](./mtl4machinelearningpipelinedescriptor/setinputdimensions_withrange_.md)
  Sets the dimensions of multiple input tensors on a range of buffer bindings.

## Relationships

### Inherits From
- [MTL4PipelineDescriptor](./mtl4pipelinedescriptor.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring a machine learning pipeline
- [class MTL4MachineLearningPipelineReflection](./mtl4machinelearningpipelinereflection.md)
  Represents reflection information for a machine learning pipeline state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinedescriptor)*