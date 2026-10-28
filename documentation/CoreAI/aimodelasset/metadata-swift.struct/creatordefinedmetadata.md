# creatorDefinedMetadata

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

The custom key-value pairs defined by the model’s creator.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var creatorDefinedMetadata: [String : AIModelAsset.Metadata.CreatorDefinedValue] { get set }
```

## Discussion

Returns an empty dictionary if the model has no creator-defined metadata.

## See Also

### Accessing creator-defined metadata
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
- [subscript(String, Int.Type) -> Int?](./subscript%28_,_%29-9hpy0.md)
  Accesses a custom metadata integer value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/metadata-swift.struct/creatordefinedmetadata)*