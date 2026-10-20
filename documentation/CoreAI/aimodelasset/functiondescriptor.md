# AIModelAsset.FunctionDescriptor

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A description of a function in the model’s program.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct FunctionDescriptor
```

## Topics

### Inspecting function details
- [var name: String](./functiondescriptor/name.md)
  The function’s symbol name.
- [var inputs: [AIModelAsset.ValueDescriptor]](./functiondescriptor/inputs.md)
  The descriptions of the function’s inputs.
- [var outputs: [AIModelAsset.ValueDescriptor]](./functiondescriptor/outputs.md)
  The descriptions of the function’s outputs.
### Instance Properties
- [var states: [AIModelAsset.ValueDescriptor]](./functiondescriptor/states.md)
  The descriptions of the function’s states.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [AIModelAsset.Metadata](./metadata-swift.struct.md)
  The metadata for a model asset, including author, license, and custom key-value pairs.
- [AIModelAsset.Summary](./summary.md)
  A summary of a model’s structure and statistics.
- [AIModelAsset.ValueDescriptor](./valuedescriptor.md)
  A description of a function’s input or output value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/functiondescriptor)*