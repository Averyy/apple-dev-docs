# init(url:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) modelAssetWithURL:(NSURL *) compiledModelURL error:(NSError **) error;
```

#### Return Value

A model asset or nil if there is an error.

## Parameters

- `compiledModelURL`: Location on the disk where the model asset is present.

## See Also

### Creating a model asset
- [convenience init(specification: Data) throws](./init%28specification%29.md)
  Creates a model asset from an in-memory model specification.
- [convenience init(specification: Data, blobMapping: [URL : Data]) throws](./init%28specification,blobmapping%29.md)
  Construct a model asset from an ML Program specification by replacing blob file references with corresponding in-memory blobs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelasset/init(url:)-43988)*