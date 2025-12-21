# init(specification:)

**Framework**: Core ML  
**Kind**: init

Creates a model asset from an in-memory model specification.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(specification specificationData: Data) throws
```

## Parameters

- `specificationData`: The contents of a   as a data blob.

## See Also

- [convenience init(specification: Data, blobMapping: [URL : Data]) throws](mlmodelasset/init(specification:blobmapping:).md)
  Construct a model asset from an ML Program specification by replacing blob file references with corresponding in-memory blobs.
- [convenience init(url: URL) throws](mlmodelasset/init(url:).md)
  Constructs a ModelAsset from a compiled model URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelasset/init(specification:))*