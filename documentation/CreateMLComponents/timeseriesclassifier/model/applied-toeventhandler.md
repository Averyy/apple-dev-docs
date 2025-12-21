# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs a classification on a shaped array of input features.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func applied(to input: MLShapedArray<Scalar>, eventHandler: EventHandler? = nil) async throws -> ClassificationDistribution<Label>
```

#### Return Value

A classification distribution.

## Parameters

- `input`: A shaped array of input features. The shape must  .
- `eventHandler`: An event handler.

## See Also

- [func export(to: URL) throws](timeseriesclassifier/model/export(to:).md)
  Exports this transformer as a CoreML model package.
- [func export(to: URL, metadata: ModelMetadata) throws](timeseriesclassifier/model/export(to:metadata:).md)
  Exports this transformer as a CoreML model package with user-supplied metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/model/applied(to:eventhandler:))*