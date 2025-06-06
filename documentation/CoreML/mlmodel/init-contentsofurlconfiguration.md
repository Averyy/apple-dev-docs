# init(contentsOfURL:configuration:)

**Framework**: Core ML  
**Kind**: init

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
convenience init(contentsOfURL url: URL, configuration: MLModelConfiguration) throws
```

## See Also

- [class func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLModel](mlmodel/load(contentsof:configuration:).md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(MLModelAsset, configuration: MLModelConfiguration, completionHandler: (MLModel?, (any Error)?) -> Void)](mlmodel/load(_:configuration:completionhandler:).md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(contentsOf: URL, configuration: MLModelConfiguration, completionHandler: (Result<MLModel, any Error>) -> Void)](mlmodel/load(contentsof:configuration:completionhandler:).md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.
- [convenience init(contentsOf: URL) throws](mlmodel/init(contentsof:).md)
  Creates a Core ML model instance from a compiled model file.
- [convenience init(contentsOf: URL, configuration: MLModelConfiguration) throws](mlmodel/init(contentsof:configuration:).md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.
- [convenience init(contentsOfURL: URL) throws](mlmodel/init(contentsofurl:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/init(contentsofurl:configuration:))*