# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Updates a transformer with a new sequence of examples.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func update(_ transformer: inout Self.Transformer, with input: DataFrame, eventHandler: EventHandler?) async throws
```

## Parameters

- `transformer`: A transformer to update.
- `input`: A data frame containing examples.
- `eventHandler`: An event handler.

## See Also

### Transforming
- [func makeTransformer() -> Self.Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout Self.Transformer, with: DataFrame) async throws](./update%28_,with%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtabularestimator/update(_:with:eventhandler:))*