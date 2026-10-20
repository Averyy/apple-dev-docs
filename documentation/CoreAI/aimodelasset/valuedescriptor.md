# AIModelAsset.ValueDescriptor

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A description of a function’s input or output value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ValueDescriptor
```

## Topics

### Inspecting value details
- [var name: String](./valuedescriptor/name.md)
  The value’s name.
- [var typeName: String](./valuedescriptor/typename.md)
  The value’s type name.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [AIModelAsset.FunctionDescriptor](./functiondescriptor.md)
  A description of a function in the model’s program.
- [AIModelAsset.Metadata](./metadata-swift.struct.md)
  The metadata for a model asset, including author, license, and custom key-value pairs.
- [AIModelAsset.Summary](./summary.md)
  A summary of a model’s structure and statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/valuedescriptor)*