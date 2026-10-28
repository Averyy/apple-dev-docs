# author

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

The name of the model’s author.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var author: String { get set }
```

## Discussion

Returns an empty string if the model has no author.

## See Also

### Reading model information
- [var description: String](./description.md)
  A human-readable description of the model.
- [var license: String](./license.md)
  The license text for the model.
- [var creationDate: Date?](./creationdate.md)
  The model’s creation date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/metadata-swift.struct/author)*