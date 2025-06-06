# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs a prediction from a single input.

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
func applied(to input: MLShapedArray<Scalar>, eventHandler: EventHandler? = nil) async throws -> Double
```

#### Return Value

A regression result.

## Parameters

- `input`: The input feature.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelregressoradaptor/applied(to:eventhandler:))*