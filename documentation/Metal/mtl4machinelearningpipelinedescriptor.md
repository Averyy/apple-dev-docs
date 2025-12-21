# MTL4MachineLearningPipelineDescriptor

**Framework**: Metal  
**Kind**: class

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

## Topics

### Instance Properties
- [var label: String?](mtl4machinelearningpipelinedescriptor/label.md)
  Assigns an optional string that helps identify pipeline states you create from this descriptor.
- [var machineLearningFunctionDescriptor: MTL4FunctionDescriptor?](mtl4machinelearningpipelinedescriptor/machinelearningfunctiondescriptor.md)
  Assigns the function that the machine learning pipeline you create from this descriptor executes.
### Instance Methods
- [func inputDimensions(bufferIndex: Int) -> MTLTensorExtents?](mtl4machinelearningpipelinedescriptor/inputdimensions(bufferindex:).md)
  Obtains the dimensions of the input tensor at `bufferIndex` if set, `nil` otherwise.
- [func reset()](mtl4machinelearningpipelinedescriptor/reset.md)
  Resets the descriptor to its default values.
- [func setInputDimensions(MTLTensorExtents?, bufferIndex: Int)](mtl4machinelearningpipelinedescriptor/setinputdimensions(_:bufferindex:)-34gir.md)
  Sets the dimension of an input tensor at a buffer index.
- [func setInputDimensions([MTLTensorExtents], bufferIndex: Int)](mtl4machinelearningpipelinedescriptor/setinputdimensions(_:bufferindex:)-8fnq7.md)
  Sets the dimensions of multiple input tensors on a range of buffer bindings.

## Relationships

### Inherits From
- [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTL4MachineLearningPipelineReflection](mtl4machinelearningpipelinereflection.md)
  Represents reflection information for a machine learning pipeline state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinedescriptor)*