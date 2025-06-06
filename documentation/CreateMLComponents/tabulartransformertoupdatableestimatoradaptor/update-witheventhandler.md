# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Does nothing since this estimator uses a pre-defined transformer.

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
func update(_ transformer: inout Transformer, with input: DataFrame, eventHandler: EventHandler? = nil) async throws
```

## See Also

- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> Transformer](tabulartransformertoupdatableestimatoradaptor/fitted(to:eventhandler:).md)
  Returns the pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoupdatableestimatoradaptor/update(_:with:eventhandler:))*