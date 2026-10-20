# export(to:metadata:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Exports this transformer as a CoreML model package with user-supplied metadata.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func export(to url: URL, metadata: ModelMetadata) throws
```

Available when `Scalar` conforms to `MLShapedArrayScalar`, `Scalar` conforms to `BinaryFloatingPoint`, `Label` conforms to `Comparable`, `Label` conforms to `Decodable`, `Label` conforms to `Encodable`, and `Label` conforms to `Hashable`.

## Parameters

- `url`: The location to write the model into.
- `metadata`: Contextual user-provided information.

## See Also

### Applying and exporting
- [func applied(to:eventHandler:)](./applied%28to,eventhandler%29.md)
  Performs a classification on a shaped array of input features.
- [func export(to: URL) throws](./export%28to%29.md)
  Exports this transformer as a CoreML model package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/model/export(to:metadata:))*