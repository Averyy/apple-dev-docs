# init(url:)

**Framework**: Core ML  
**Kind**: init

Constructs a ModelAsset from a compiled model URL.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(url compiledModelURL: URL) throws
```

#### Return Value

A model asset or nil if there is an error.

## Parameters

- `compiledModelURL`: Location on the disk where the model asset is present.

## See Also

- [convenience init(specification: Data) throws](mlmodelasset/init(specification:).md)
  Creates a model asset from an in-memory model specification.
- [convenience init(specification: Data, blobMapping: [URL : Data]) throws](mlmodelasset/init(specification:blobmapping:).md)
  Construct a model asset from an ML Program specification by replacing blob file references with corresponding in-memory blobs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelasset/init(url:))*