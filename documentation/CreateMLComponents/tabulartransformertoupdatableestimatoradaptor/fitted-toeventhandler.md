# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Returns the pre-defined transformer.

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
func fitted(to input: DataFrame, eventHandler: EventHandler? = nil) async throws -> Transformer
```

#### Return Value

The pre-defined transformer.

## Parameters

- `input`: A data frame containing examples.
- `eventHandler`: An event handler.

## See Also

- [func update(inout Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](tabulartransformertoupdatableestimatoradaptor/update(_:with:eventhandler:).md)
  Does nothing since this estimator uses a pre-defined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoupdatableestimatoradaptor/fitted(to:eventhandler:))*