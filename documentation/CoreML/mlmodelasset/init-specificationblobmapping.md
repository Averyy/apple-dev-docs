# init(specification:blobMapping:)

**Framework**: Core ML  
**Kind**: init

Construct a model asset from an ML Program specification by replacing blob file references with corresponding in-memory blobs.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
convenience init(specification specificationData: Data, blobMapping: [URL : Data]) throws
```

#### Discussion

An ML Program may use `BlobFileValue` syntax, which stores the blob data in external files and refers them by URL. This factory method enables in-memory workflow for such models by using the specified in-memory blob data in place of the external files.

The format of in-memory blobs must be the same as the external files. The dictionary must contain all the reference URLs used in the specification.

## Parameters

- `blobMapping`: A dictionary with blob URL as the key and blob data as the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelasset/init(specification:blobmapping:))*