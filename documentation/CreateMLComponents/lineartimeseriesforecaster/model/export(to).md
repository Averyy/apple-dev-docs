# export(to:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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

Available when `Scalar` conforms to `MLShapedArrayScalar` and `BinaryFloatingPoint`.

## Parameters

- `url`: The location to write the model into.

## See Also

### Exporting the model
- [func export(to: URL, metadata: ModelMetadata) throws](./export%28to,metadata%29.md)
  Exports this transformer as a CoreML model package with user-supplied metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model/export(to:))*