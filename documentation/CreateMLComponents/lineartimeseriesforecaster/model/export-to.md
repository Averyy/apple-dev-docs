# export(to:)

**Framework**: Create ML Components  
**Kind**: method

Exports this transformer as a CoreML model package.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func export(to url: URL) throws
```

## Parameters

- `url`: The location to write the model into.

## See Also

- [func export(to: URL, metadata: ModelMetadata) throws](lineartimeseriesforecaster/model/export(to:metadata:).md)
  Exports this transformer as a CoreML model package with user-supplied metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model/export(to:))*