# write(_:to:overwrite:)

**Framework**: Create ML Components  
**Kind**: method

Writes the encoded transformer to a file.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func write(_ transformer: Self.Transformer, to url: URL, overwrite: Bool = true) throws
```

## Parameters

- `transformer`: A transformer created by this estimator.
- `url`: A file URL.
- `overwrite`: A Boolean value indicating whether to overwrite existing files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletemporalestimator/write(_:to:overwrite:))*