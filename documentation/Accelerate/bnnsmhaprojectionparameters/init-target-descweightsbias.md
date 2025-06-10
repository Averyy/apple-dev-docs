# init(target_desc:weights:bias:)

**Framework**: Accelerate  
**Kind**: init

Returns a new multihead attention projection parameters structure from the specified parameters.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(target_desc: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor)
```

## Parameters

- `target_desc`: The descriptor—which is either an input query, key, or value, or an output—of the main target of the operation.
- `weights`: The descriptor of the initial projection’s weights.
- `bias`: The descriptor of the initial projection’s bias.

## See Also

- [init()](bnnsmhaprojectionparameters/init.md)
  Returns a new multihead attention projection parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsmhaprojectionparameters/init(target_desc:weights:bias:))*