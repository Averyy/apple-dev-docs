# AIModelAsset.Metadata

**Framework**: Core AI  
**Kind**: struct

The metadata for a model asset, including author, license, and custom key-value pairs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Metadata
```

#### Overview

Access metadata through the [`metadata`](aimodelasset/metadata-swift.property.md) property. To modify metadata, use [`updateMetadata(_:)`](aimodelasset/updatemetadata(_:).md), which writes changes back to disk.

In addition to the standard properties like [`author`](aimodelasset/metadata-swift.struct/author.md) and [`license`](aimodelasset/metadata-swift.struct/license.md), you can store custom key-value pairs using subscript syntax:

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
- [init()](aimodelasset/metadata-swift.struct/init.md)
  Creates metadata with no values set.
### Reading model information
- [var description: String](aimodelasset/metadata-swift.struct/description.md)
  A human-readable description of the model.
- [var author: String](aimodelasset/metadata-swift.struct/author.md)
  The name of the model’s author.
- [var license: String](aimodelasset/metadata-swift.struct/license.md)
  The license text for the model.
- [var creationDate: Date?](aimodelasset/metadata-swift.struct/creationdate.md)
  The model’s creation date.
### Accessing creator-defined metadata
- [var creatorDefinedMetadata: [String : AIModelAsset.Metadata.CreatorDefinedValue]](aimodelasset/metadata-swift.struct/creatordefinedmetadata.md)
  The custom key-value pairs defined by the model’s creator.
- [subscript(String, String.Type) -> String?](aimodelasset/metadata-swift.struct/subscript(_:_:)-44ov4.md)
  Accesses a custom metadata string value for the specified key.
- [subscript(String, Bool.Type) -> Bool?](aimodelasset/metadata-swift.struct/subscript(_:_:)-50v52.md)
  Accesses a custom metadata Boolean value for the specified key.
- [subscript(String, [AIModelAsset.Metadata.CreatorDefinedValue].Type) -> [AIModelAsset.Metadata.CreatorDefinedValue]?](aimodelasset/metadata-swift.struct/subscript(_:_:)-5o1kb.md)
  Accesses a custom metadata array value for the specified key.
- [subscript(String, [String : AIModelAsset.Metadata.CreatorDefinedValue].Type) -> [String : AIModelAsset.Metadata.CreatorDefinedValue]?](aimodelasset/metadata-swift.struct/subscript(_:_:)-5se5j.md)
  Accesses a custom metadata dictionary value for the specified key.
- [subscript(String, Double.Type) -> Double?](aimodelasset/metadata-swift.struct/subscript(_:_:)-6bxrd.md)
  Accesses a custom metadata number value for the specified key.
- [subscript(String, Int.Type) -> Int?](aimodelasset/metadata-swift.struct/subscript(_:_:)-9hpy0.md)
  Accesses a custom metadata integer value for the specified key.
### Defining value types
- [AIModelAsset.Metadata.CreatorDefinedValue](aimodelasset/metadata-swift.struct/creatordefinedvalue.md)
  A custom metadata value.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AIModelAsset.FunctionDescriptor](aimodelasset/functiondescriptor.md)
  A description of a function in the model’s program.
- [AIModelAsset.Summary](aimodelasset/summary.md)
  A summary of a model’s structure and statistics.
- [AIModelAsset.ValueDescriptor](aimodelasset/valuedescriptor.md)
  A description of a function’s input or output value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/metadata-swift.struct)*