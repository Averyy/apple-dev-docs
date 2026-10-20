# init(contentsOf:)

**Framework**: Natural Language  
**Kind**: init  
**Role**: Initializer

Creates a new natural language model based on a compiled Core ML model at the given URL.

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
convenience init(contentsOf url: URL) throws
```

```objc
+ (instancetype) modelWithContentsOfURL:(NSURL *) url error:(NSError **) error;
```

## Parameters

- `url`: The location of the *compiled* Core ML model file in the file system (ending with `.mlmodelc`) that’s the basis for this natural language model.

## See Also

### Creating a model
- [convenience init(mlModel: MLModel) throws](./init%28mlmodel%29-9tpjr.md)
  Creates a new natural language model based on the given Core ML model instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodel/init(contentsof:))*