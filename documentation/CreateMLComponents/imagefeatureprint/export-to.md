# export(to:)

**Framework**: Create ML Components  
**Kind**: method

Exports this transformer as a CoreML model.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagefeatureprint/export(to:))*