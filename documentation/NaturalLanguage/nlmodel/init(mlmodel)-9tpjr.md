# init(mlModel:)

**Framework**: Natural Language  
**Kind**: init  
**Role**: Initializer

Creates a new natural language model based on the given Core ML model instance.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
convenience init(mlModel: MLModel) throws
```

```objc
+ (instancetype) modelWithMLModel:(MLModel *) mlModel error:(NSError **) error;
```

## Parameters

- `mlModel`: A Core ML model instance that’s the basis for this natural language model.

## See Also

### Creating a model
- [convenience init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a new natural language model based on a compiled Core ML model at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodel/init(mlmodel:)-9tpjr)*