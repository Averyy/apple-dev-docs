# creatorDefinedMetadata

**Framework**: Core AI  
**Kind**: property

The custom key-value pairs defined by the model’s creator.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var creatorDefinedMetadata: [String : AIModelAsset.Metadata.CreatorDefinedValue] { get set }
```

#### Discussion

Returns an empty dictionary if the model has no creator-defined metadata.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/metadata-swift.struct/creatordefinedmetadata)*