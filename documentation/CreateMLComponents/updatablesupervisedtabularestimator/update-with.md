# update(_:with:)

**Framework**: Create ML Components  
**Kind**: method

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
func update(_ transformer: inout Self.Transformer, with input: DataFrame) async throws
```

## See Also

- [func makeTransformer() -> Self.Transformer](updatablesupervisedtabularestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout Self.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](updatablesupervisedtabularestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtabularestimator/update(_:with:))*