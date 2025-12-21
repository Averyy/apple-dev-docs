# export(to:metadata:)

**Framework**: Create ML Components  
**Kind**: method

Exports this transformer as a CoreML model package with user-supplied metadata.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func export(to url: URL, metadata: ModelMetadata) throws
```

## Parameters

- `url`: The location to write the model into.
- `metadata`: Contextual user-provided information.

## See Also

- [func applied(to:eventHandler:)](timeseriesclassifier/model/applied(to:eventhandler:).md)
  Performs a classification on a shaped array of input features.
- [func export(to: URL) throws](timeseriesclassifier/model/export(to:).md)
  Exports this transformer as a CoreML model package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/model/export(to:metadata:))*