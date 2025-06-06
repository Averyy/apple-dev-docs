# load(_:configuration:completionHandler:)

**Framework**: Core ML  
**Kind**: method

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
class func load(asset: MLModelAsset, configuration: MLModelConfiguration) async throws -> MLModel
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func load(asset: MLModelAsset, configuration: MLModelConfiguration) async throws -> MLModel
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func load(asset: MLModelAsset, configuration: MLModelConfiguration) async throws -> MLModel
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `asset`: The compiled model asset derived from in-memory or on-disk Core ML model.
- `configuration`: The model configuration that holds options for loading the model.
- `handler`: The completion handler invoked when the load completes. A valid   returns on success, or an error if failure.

## See Also

- [class func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLModel](mlmodel/load(contentsof:configuration:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/load(_:configuration:completionhandler:))*