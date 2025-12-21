# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs a classification on a single input.

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
func applied(to input: MLShapedArray<Scalar>, eventHandler: EventHandler? = nil) async throws -> ClassificationDistribution<Label>
```

#### Return Value

A classification distribution.

## Parameters

- `input`: The classifier input.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifiermodel/applied(to:eventhandler:))*