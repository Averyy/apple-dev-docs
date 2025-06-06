# load(contentsOf:configuration:completionHandler:)

**Framework**: Core ML  
**Kind**: method

Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func load(contentsOf url: URL, configuration: MLModelConfiguration = MLModelConfiguration(), completionHandler handler: @escaping (Result<MLModel, any Error>) -> Void)
```

#### Discussion

Use this method to load a model asynchronously. Core ML calls your completion handler after it successfully loads the model, or encounters an error attempting to load it.

In Swift, if the model loaded successfully, you can use the instance from the [`Result.success(_:)`](https://developer.apple.com/documentation/Swift/Result/success(_:)) associated value; otherwise, use the [`Result.failure(_:)`](https://developer.apple.com/documentation/Swift/Result/failure(_:)) associated value to address the error. In Objective-C, you can use the [`MLModel`](mlmodel.md) instance in your completion hander; otherwise, use the [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) instance to address the error.  See [`MLModelError.Code`](mlmodelerror-swift.struct/code.md) for the list of error codes.

## Parameters

- `url`: The path to a compiled model file ( ), typically with the   that   returns.
- `configuration`: The runtime settings for the new model instance.
- `handler`: A closure the method calls when it finishes loading the model.

## See Also

- [class func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLModel](mlmodel/load(contentsof:configuration:).md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(MLModelAsset, configuration: MLModelConfiguration, completionHandler: (MLModel?, (any Error)?) -> Void)](mlmodel/load(_:configuration:completionhandler:).md)
  Construct a model asynchronously from a compiled model asset.
- [convenience init(contentsOf: URL) throws](mlmodel/init(contentsof:).md)
  Creates a Core ML model instance from a compiled model file.
- [convenience init(contentsOf: URL, configuration: MLModelConfiguration) throws](mlmodel/init(contentsof:configuration:).md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.
- [convenience init(contentsOfURL: URL) throws](mlmodel/init(contentsofurl:).md)
- [convenience init(contentsOfURL: URL, configuration: MLModelConfiguration) throws](mlmodel/init(contentsofurl:configuration:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/load(contentsof:configuration:completionhandler:))*