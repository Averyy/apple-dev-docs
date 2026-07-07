# AIModelAsset

**Framework**: Core AI  
**Kind**: struct

An unspecialized source model asset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AIModelAsset
```

#### Overview

Use a model asset to inspect a model’s structure and metadata without specializing it for a specific device. This lets you query model information without performing specialization, which is an expensive operation. You create a model asset by providing the URL of an `.aimodel` bundle on disk:

```swift
let asset = try AIModelAsset(contentsOf: modelURL)
guard let summary = try asset.summary(includingStatistics: true) else { return }
```

Unlike [`AIModel`](aimodel.md), a model asset can’t perform inference. Instead, use it to query model information such as function signatures, input and output descriptions, compute and storage types, and author-provided metadata.

## Topics

### Loading an asset
- [init(contentsOf: URL) throws](aimodelasset/init(contentsof:).md)
  Creates a model asset from the contents of the specified URL.
- [static func isValid(at: URL) -> Bool](aimodelasset/isvalid(at:).md)
  Returns a Boolean value that indicates whether the URL contains a valid model asset.
### Inspecting an asset
- [var metadata: AIModelAsset.Metadata](aimodelasset/metadata-swift.property.md)
  The author-provided metadata for the model asset.
- [func summary(includingStatistics: Bool) throws -> AIModelAsset.Summary?](aimodelasset/summary(includingstatistics:).md)
  Returns the model summary.
- [let url: URL](aimodelasset/url.md)
  The file URL of the model asset bundle on disk.
### Modifying an asset
- [func updateMetadata((inout AIModelAsset.Metadata) throws -> Void) throws](aimodelasset/updatemetadata(_:).md)
  Updates the asset metadata.
- [func removeDerivedArtifacts() throws](aimodelasset/removederivedartifacts.md)
  Removes all derived artifacts for the model’s program.
### Supporting types
- [AIModelAsset.FunctionDescriptor](aimodelasset/functiondescriptor.md)
  A description of a function in the model’s program.
- [AIModelAsset.Metadata](aimodelasset/metadata-swift.struct.md)
  The metadata for a model asset, including author, license, and custom key-value pairs.
- [AIModelAsset.Summary](aimodelasset/summary.md)
  A summary of a model’s structure and statistics.
- [AIModelAsset.ValueDescriptor](aimodelasset/valuedescriptor.md)
  A description of a function’s input or output value.

## See Also

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)
  Power your app’s intelligent features with an on-device AI model.
- [struct AIModel](aimodel.md)
  A specialized model for running inference on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset)*