# load(contentsOf:configuration:)

**Framework**: Core ML  
**Kind**: method

Construct a model asynchronously from a compiled model asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class func load(contentsOf url: URL, configuration: MLModelConfiguration = MLModelConfiguration()) async throws -> MLModel
```

#### Return Value

The loaded model, if successful; otherwise, `nil`.

## Parameters

- `url`: The URL of the compiled model asset derived from in-memory or on-disk Core ML model.
- `configuration`: The model configuration that hold options for loading the model.

## See Also

- [class func load(MLModelAsset, configuration: MLModelConfiguration, completionHandler: (MLModel?, (any Error)?) -> Void)](mlmodel/load(_:configuration:completionhandler:).md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(contentsOf: URL, configuration: MLModelConfiguration, completionHandler: (Result<MLModel, any Error>) -> Void)](mlmodel/load(contentsof:configuration:completionhandler:).md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.
- [convenience init(contentsOf: URL) throws](mlmodel/init(contentsof:).md)
  Creates a Core ML model instance from a compiled model file.
- [convenience init(contentsOf: URL, configuration: MLModelConfiguration) throws](mlmodel/init(contentsof:configuration:).md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.
- [convenience init(contentsOfURL: URL) throws](mlmodel/init(contentsofurl:).md)
- [convenience init(contentsOfURL: URL, configuration: MLModelConfiguration) throws](mlmodel/init(contentsofurl:configuration:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/load(contentsof:configuration:))*