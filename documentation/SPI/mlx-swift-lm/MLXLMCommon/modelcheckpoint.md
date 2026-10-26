---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcheckpoint"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelCheckpoint

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Checkpoint tensors and the metadata and quantization settings that describe them.

## Declaration

```swift
struct ModelCheckpoint
```

## Mentions

- [Model Compatibility](./model-compatibility.md)

#### Overview

Models can normalize a checkpoint in [`prepareCheckpoint(_:)`](./baselanguagemodel/preparecheckpoint%28_%29.md) before quantization and strict parameter validation. Name mappings apply to tensors and layer settings together, so a renamed layer keeps its declared precision.

## Topics

### Initializers
- [init(weights: [String : MLXArray], metadata: [String : String], weightMetadata: [String : [String : String]], perLayerQuantization: BaseConfiguration.PerLayerQuantization?)](./modelcheckpoint/init%28weights,metadata,weightmetadata,perlayerquantization%29.md)
### Instance Properties
- [let metadata: [String : String]](./modelcheckpoint/metadata.md)
  The first nonempty file metadata, for compatibility with existing sanitizers.
- [var perLayerQuantization: BaseConfiguration.PerLayerQuantization?](./modelcheckpoint/perlayerquantization.md)
- [var weights: [String : MLXArray]](./modelcheckpoint/weights.md)
### Instance Methods
- [func mapNames((String) -> String?) throws -> ModelCheckpoint](./modelcheckpoint/mapnames%28_%29.md)
  Rename or exclude complete module paths, including their quantization settings. A `nil` name excludes the tensor or layer. Aliases must not overwrite each other.
- [func mapNames(using: CheckpointNameMapping) throws -> ModelCheckpoint](./modelcheckpoint/mapnames%28using%29.md)
  Apply the same declarative mapping to tensors, provenance, and layer settings.
- [func metadata(forWeight: String) -> [String : String]](./modelcheckpoint/metadata%28forweight%29.md)
  Metadata from the file that supplied this tensor, including an empty metadata block.
### Enumerations
- [ModelCheckpoint.MappingError](./modelcheckpoint/mappingerror.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcheckpoint)*