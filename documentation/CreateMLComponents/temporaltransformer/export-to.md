# export(to:)

**Framework**: Create ML Components  
**Kind**: method

Exports this temporal transformer as a CoreML model.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func export(to url: URL) throws
```

#### Discussion

> **Note**: By default this method exports .mlpackage files. You can export a .mlmodel file by specifying that as the URL file extension. But if you specify .mlmodel and the transformer doesn’t support it, this method will throw an error.

## Parameters

- `url`: The location to write the model into.

## See Also

- [func export(to: URL, metadata: ModelMetadata) throws](temporaltransformer/export(to:metadata:).md)
  Exports this temporal transformer as a CoreML model with user-supplied metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/export(to:))*