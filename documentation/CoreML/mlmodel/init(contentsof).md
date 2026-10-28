# init(contentsOf:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a Core ML model instance from a compiled model file.

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
convenience init(contentsOf url: URL) throws
```

```objc
+ (instancetype) modelWithContentsOfURL:(NSURL *) url error:(NSError **) error;
```

## Discussion

In most cases, your app won’t need to create a model object directly. Consider the programmer-friendly wrapper class that Xcode automatically generates when you add a model to your project (see [Integrating a Core ML Model into Your App](../integrating-a-core-ml-model-into-your-app.md)).

If the wrapper class doesn’t meet your app’s needs or you need to customize the model’s configuration, use this initializer to create a model object from any compiled model file you can access. Typically, you use this initializer after your app has downloaded and compiled a model, which is one technique for saving space in your app (see [Downloading and Compiling a Model on the User’s Device](../downloading-and-compiling-a-model-on-the-user-s-device.md)).

## Parameters

- `url`: The path to a compiled model file (*ModelName*`.mlmodelc`), typically with the `URL` that [`compileModel(at:)`](./compilemodel%28at%29-6442s.md) returns.

## See Also

### Loading a model
- [class func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLModel](./load%28contentsof,configuration%29.md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(MLModelAsset, configuration: MLModelConfiguration, completionHandler: (MLModel?, (any Error)?) -> Void)](./load%28_,configuration,completionhandler%29.md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(contentsOf: URL, configuration: MLModelConfiguration, completionHandler: (Result<MLModel, any Error>) -> Void)](./load%28contentsof,configuration,completionhandler%29.md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.
- [convenience init(contentsOf: URL, configuration: MLModelConfiguration) throws](./init%28contentsof,configuration%29.md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.
- [convenience init(contentsOfURL: URL) throws](./init%28contentsofurl%29.md)
- [convenience init(contentsOfURL: URL, configuration: MLModelConfiguration) throws](./init%28contentsofurl,configuration%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/init(contentsof:))*