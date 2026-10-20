# load(contentsOf:configuration:completionHandler:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Type Method

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

**Swift**:

```swift
MLModel.load(contentsOf: modelURL) { result in
    switch result {
    case .success(let loadedModel):
        print("Successfully loaded model `\(loadedModel)`.")

        // Use the loaded model for predictions.
        // ...

    case .failure(let error):
        print("Error loading model: \(error).")
    }
}
```

**Objective-C**:

```objc
[MLModel loadContentsOfURL:modelURL
             configuration:[[MLModelConfiguration alloc] init]
         completionHandler:^(MLModel *loadedModel,
                             NSError *error) {
    if (nil == loadedModel) {
        NSLog(@"Error loading model`: %@", (nil != error) ? error : modelURL);
        return;
    }

    NSLog(@"Successfully loaded model at: %@", modelURL);

    // Use the loaded model for predictions.
    // ...
}];
```

In Swift, if the model loaded successfully, you can use the instance from the [`Result.success(_:)`](../../Swift/result/success%28_%29.md) associated value; otherwise, use the [`Result.failure(_:)`](../../Swift/result/failure%28_%29.md) associated value to address the error. In Objective-C, you can use the [`MLModel`](../mlmodel.md) instance in your completion hander; otherwise, use the [`NSError`](../../Foundation/nserror.md) instance to address the error.  See [`MLModelError.Code`](../mlmodelerror-swift.struct/code.md) for the list of error codes.

## Parameters

- `url`: The path to a compiled model file (*ModelName*`.mlmodelc`), typically with the `URL` that [`compileModel(at:)`](./compilemodel%28at%29-6442s.md) returns.
- `configuration`: The runtime settings for the new model instance.
- `handler`: A closure the method calls when it finishes loading the model.

## See Also

### Loading a model
- [class func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLModel](./load%28contentsof,configuration%29.md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(MLModelAsset, configuration: MLModelConfiguration, completionHandler: (MLModel?, (any Error)?) -> Void)](./load%28_,configuration,completionhandler%29.md)
  Construct a model asynchronously from a compiled model asset.
- [convenience init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a Core ML model instance from a compiled model file.
- [convenience init(contentsOf: URL, configuration: MLModelConfiguration) throws](./init%28contentsof,configuration%29.md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.
- [convenience init(contentsOfURL: URL) throws](./init%28contentsofurl%29.md)
- [convenience init(contentsOfURL: URL, configuration: MLModelConfiguration) throws](./init%28contentsofurl,configuration%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/load(contentsof:configuration:completionhandler:))*