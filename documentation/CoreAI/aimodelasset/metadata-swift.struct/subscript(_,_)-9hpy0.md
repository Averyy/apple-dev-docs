# subscript(_:_:)

**Framework**: Core AI  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a custom metadata integer value for the specified key.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
subscript(key: String, type: Int.Type = Int.self) -> Int? { get set }
```

## See Also

### Accessing creator-defined metadata
- [var creatorDefinedMetadata: [String : AIModelAsset.Metadata.CreatorDefinedValue]](./creatordefinedmetadata.md)
  The custom key-value pairs defined by the model’s creator.
- [subscript(String, String.Type) -> String?](./subscript%28_,_%29-44ov4.md)
  Accesses a custom metadata string value for the specified key.
- [subscript(String, Bool.Type) -> Bool?](./subscript%28_,_%29-50v52.md)
  Accesses a custom metadata Boolean value for the specified key.
- [subscript(String, [AIModelAsset.Metadata.CreatorDefinedValue].Type) -> [AIModelAsset.Metadata.CreatorDefinedValue]?](./subscript%28_,_%29-5o1kb.md)
  Accesses a custom metadata array value for the specified key.
- [subscript(String, [String : AIModelAsset.Metadata.CreatorDefinedValue].Type) -> [String : AIModelAsset.Metadata.CreatorDefinedValue]?](./subscript%28_,_%29-5se5j.md)
  Accesses a custom metadata dictionary value for the specified key.
- [subscript(String, Double.Type) -> Double?](./subscript%28_,_%29-6bxrd.md)
  Accesses a custom metadata number value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/metadata-swift.struct/subscript(_:_:)-9hpy0)*