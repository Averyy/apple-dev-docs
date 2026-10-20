# init(contentsOfURL:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
convenience init(contentsOfURL url: URL) throws
```

## See Also

### Loading a model
- [class func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLModel](./load%28contentsof,configuration%29.md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(MLModelAsset, configuration: MLModelConfiguration, completionHandler: (MLModel?, (any Error)?) -> Void)](./load%28_,configuration,completionhandler%29.md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(contentsOf: URL, configuration: MLModelConfiguration, completionHandler: (Result<MLModel, any Error>) -> Void)](./load%28contentsof,configuration,completionhandler%29.md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.
- [convenience init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a Core ML model instance from a compiled model file.
- [convenience init(contentsOf: URL, configuration: MLModelConfiguration) throws](./init%28contentsof,configuration%29.md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.
- [convenience init(contentsOfURL: URL, configuration: MLModelConfiguration) throws](./init%28contentsofurl,configuration%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/init(contentsofurl:))*