# compileModel(at:)

**Framework**: Core ML  
**Kind**: method

Compiles a model on the device to update the model in your app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func compileModel(at modelURL: URL) throws -> URL
```

## Mentions

- [Downloading and Compiling a Model on the User’s Device](downloading-and-compiling-a-model-on-the-user-s-device.md)

#### Return Value

The local file path to the compiled model (the `.mlmodelc` file).

#### Discussion

The source `.mlmodel` file must be on the device. Pass the compiled model to [`init(contentsOf:)`](mlmodel/init(contentsof:).md) to initialize an [`MLModel`](mlmodel.md) instance.

Listing 1. Compiling a model file and creating an `MLModel` instance from the compiled version

```swift
let compiledUrl = try MLModel.compileModel(at: modelUrl)
let model = try MLModel(contentsOf: compiledUrl)
```

Compiling can be time consuming and shouldn’t be done on the main thread.

See [`Downloading and Compiling a Model on the User’s Device`](downloading-and-compiling-a-model-on-the-user-s-device.md) for more details.

## Parameters

- `modelURL`: The local file path to your downloaded   file.

## See Also

- [Downloading and Compiling a Model on the User’s Device](downloading-and-compiling-a-model-on-the-user-s-device.md)
  Install Core ML models on the user’s device dynamically at runtime.
- [class func compileModel(at: URL) async throws -> URL](mlmodel/compilemodel(at:)-45ao6.md)
  Compile a model for a device.
- [class func compileModel(at: URL, completionHandler: (Result<URL, any Error>) -> Void)](mlmodel/compilemodel(at:completionhandler:).md)
  Compile a model for a device.
- [class func compileModel(at: URL) async throws -> URL](mlmodel/compilemodel(at:)-3nea.md)
  Compile a model for a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/compilemodel(at:)-6442s)*