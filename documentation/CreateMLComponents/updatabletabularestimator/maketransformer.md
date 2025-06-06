# makeTransformer()

**Framework**: Create ML Components  
**Kind**: method  
**Required**: Yes

Creates a default-initialized transformer suitable for incremental fitting.

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
func makeTransformer() -> Self.Transformer
```

## See Also

- [func update(inout Self.Transformer, with: DataFrame) async throws](updatabletabularestimator/update(_:with:).md)
- [func update(inout Self.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](updatabletabularestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimator/maketransformer())*