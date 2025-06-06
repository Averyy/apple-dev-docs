# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the transformation on selected columns of the data frame.

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
func applied(to input: DataFrame, eventHandler: EventHandler? = nil) async throws -> DataFrame
```

#### Return Value

A data frame produced by applying the transformer to selected columns.

## Parameters

- `input`: A data frame.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselectortransformer/applied(to:eventhandler:))*