# AIModelAsset.FunctionDescriptor

**Framework**: Core AI  
**Kind**: struct

A description of a function in the model’s program.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct FunctionDescriptor
```

## Topics

### Inspecting function details
- [var name: String](aimodelasset/functiondescriptor/name.md)
  The function’s symbol name.
- [var inputs: [AIModelAsset.ValueDescriptor]](aimodelasset/functiondescriptor/inputs.md)
  The descriptions of the function’s inputs.
- [var outputs: [AIModelAsset.ValueDescriptor]](aimodelasset/functiondescriptor/outputs.md)
  The descriptions of the function’s outputs.
### Instance Properties
- [var states: [AIModelAsset.ValueDescriptor]](aimodelasset/functiondescriptor/states.md)
  The descriptions of the function’s states.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [AIModelAsset.Metadata](aimodelasset/metadata-swift.struct.md)
  The metadata for a model asset, including author, license, and custom key-value pairs.
- [AIModelAsset.Summary](aimodelasset/summary.md)
  A summary of a model’s structure and statistics.
- [AIModelAsset.ValueDescriptor](aimodelasset/valuedescriptor.md)
  A description of a function’s input or output value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/functiondescriptor)*