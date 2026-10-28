# AIModelAsset.Metadata

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

The metadata for a model asset, including author, license, and custom key-value pairs.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Metadata
```

## Overview

Access metadata through the [`metadata`](./metadata-swift.property.md) property. To modify metadata, use [`updateMetadata(_:)`](./updatemetadata%28_%29.md), which writes changes back to disk.

In addition to the standard properties like [`author`](./metadata-swift.struct/author.md) and [`license`](./metadata-swift.struct/license.md), you can store custom key-value pairs using subscript syntax:

```swift
var asset = try AIModelAsset(contentsOf: modelURL)
try asset.updateMetadata { metadata in
  metadata.author = "Alice"
  metadata["iterations"] = 1000
  metadata["accuracy"] = 0.95
}
```

## Topics

### Creating metadata
- [init()](./metadata-swift.struct/init%28%29.md)
  Creates metadata with no values set.
### Reading model information
- [var description: String](./metadata-swift.struct/description.md)
  A human-readable description of the model.
- [var author: String](./metadata-swift.struct/author.md)
  The name of the model’s author.
- [var license: String](./metadata-swift.struct/license.md)
  The license text for the model.
- [var creationDate: Date?](./metadata-swift.struct/creationdate.md)
  The model’s creation date.
### Accessing creator-defined metadata
- [var creatorDefinedMetadata: [String : AIModelAsset.Metadata.CreatorDefinedValue]](./metadata-swift.struct/creatordefinedmetadata.md)
  The custom key-value pairs defined by the model’s creator.
- [subscript(String, String.Type) -> String?](./metadata-swift.struct/subscript%28_,_%29-44ov4.md)
  Accesses a custom metadata string value for the specified key.
- [subscript(String, Bool.Type) -> Bool?](./metadata-swift.struct/subscript%28_,_%29-50v52.md)
  Accesses a custom metadata Boolean value for the specified key.
- [subscript(String, [AIModelAsset.Metadata.CreatorDefinedValue].Type) -> [AIModelAsset.Metadata.CreatorDefinedValue]?](./metadata-swift.struct/subscript%28_,_%29-5o1kb.md)
  Accesses a custom metadata array value for the specified key.
- [subscript(String, [String : AIModelAsset.Metadata.CreatorDefinedValue].Type) -> [String : AIModelAsset.Metadata.CreatorDefinedValue]?](./metadata-swift.struct/subscript%28_,_%29-5se5j.md)
  Accesses a custom metadata dictionary value for the specified key.
- [subscript(String, Double.Type) -> Double?](./metadata-swift.struct/subscript%28_,_%29-6bxrd.md)
  Accesses a custom metadata number value for the specified key.
- [subscript(String, Int.Type) -> Int?](./metadata-swift.struct/subscript%28_,_%29-9hpy0.md)
  Accesses a custom metadata integer value for the specified key.
### Defining value types
- [AIModelAsset.Metadata.CreatorDefinedValue](./metadata-swift.struct/creatordefinedvalue.md)
  A custom metadata value.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [AIModelAsset.FunctionDescriptor](./functiondescriptor.md)
  A description of a function in the model’s program.
- [AIModelAsset.Summary](./summary.md)
  A summary of a model’s structure and statistics.
- [AIModelAsset.ValueDescriptor](./valuedescriptor.md)
  A description of a function’s input or output value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/metadata-swift.struct)*