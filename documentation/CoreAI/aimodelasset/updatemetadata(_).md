# updateMetadata(_:)

**Framework**: Core AI  
**Kind**: method  
**Role**: Instance Method

Updates the asset metadata.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
mutating func updateMetadata(_ updates: (inout AIModelAsset.Metadata) throws -> Void) throws
```

#### Discussion

Pass a closure that takes the existing metadata and updates it. After the closure executes, this method writes the new metadata to the model asset on disk.

#### Example

```swift
var asset = try AIModelAsset(contentsOf: input)
try asset.updateMetadata { metadata in
  metadata.author = "Alice"
  metadata.description = "An example model"
  metadata["iterations"] = 1000 // Custom metadata
}
```

## See Also

### Modifying an asset
- [func removeDerivedArtifacts() throws](./removederivedartifacts%28%29.md)
  Removes all derived artifacts for the model’s program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/updatemetadata(_:))*