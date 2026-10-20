# load(_:configuration:completionHandler:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Type Method

Construct a model asynchronously from a compiled model asset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func load(_ asset: MLModelAsset, configuration: MLModelConfiguration, completionHandler handler: @escaping @Sendable (MLModel?, (any Error)?) -> Void)
```

```swift
class func load(asset: MLModelAsset, configuration: MLModelConfiguration) async throws -> MLModel
```

```objc
+ (void) loadModelAsset:(MLModelAsset *) asset configuration:(MLModelConfiguration *) configuration completionHandler:(void (^)(MLModel *model, NSError *error)) handler;
```

## Parameters

- `asset`: The compiled model asset derived from in-memory or on-disk Core ML model.
- `configuration`: The model configuration that holds options for loading the model.
- `handler`: The completion handler invoked when the load completes. A valid [`MLModel`](../mlmodel.md) returns on success, or an error if failure.

## See Also

### Loading a model
- [class func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLModel](./load%28contentsof,configuration%29.md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(contentsOf: URL, configuration: MLModelConfiguration, completionHandler: (Result<MLModel, any Error>) -> Void)](./load%28contentsof,configuration,completionhandler%29.md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.
- [convenience init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a Core ML model instance from a compiled model file.
- [convenience init(contentsOf: URL, configuration: MLModelConfiguration) throws](./init%28contentsof,configuration%29.md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.
- [convenience init(contentsOfURL: URL) throws](./init%28contentsofurl%29.md)
- [convenience init(contentsOfURL: URL, configuration: MLModelConfiguration) throws](./init%28contentsofurl,configuration%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/load(_:configuration:completionhandler:))*