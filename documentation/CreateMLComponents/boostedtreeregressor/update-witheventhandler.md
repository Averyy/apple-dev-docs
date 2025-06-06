# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Updates a transformer with a new sequence of examples.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func update(_ transformer: inout TreeRegressorModel, with input: DataFrame, eventHandler: EventHandler?) async throws
```

## Parameters

- `transformer`: A transformer to update.
- `input`: A data frame containing examples.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeregressor/update(_:with:eventhandler:))*