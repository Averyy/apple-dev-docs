# export(to:metadata:)

**Framework**: Create ML Components  
**Kind**: method

Exports this transformer as a CoreML model with userInfo.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func export(to url: URL, metadata: ModelMetadata) throws
```

#### Discussion

> **Note**: By default this method exports .mlpackage files. You can export a .mlmodel file by specifying that as the URL file extension. But if you specify .mlmodel and the transformer doesn’t support it, this method will throw an error.

By default this method exports .mlpackage files. You can export a .mlmodel file by specifying that as the URL file extension. But if you specify .mlmodel and the transformer doesn’t support it, this method will throw an error.

## Parameters

- `url`: The location to write the model into.
- `metadata`: Contextual user-provided information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtabulartransformer/export(to:metadata:)-85vf4)*