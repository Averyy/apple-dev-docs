# compileModel(at:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Type Method

Compiles a model on the device to update the model in your app.

**Availability**:
- iOS 11.0+ - Deprecated in 27.2
- iPadOS 11.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.13+ - Deprecated in 27.2
- tvOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use the asynchronous interface compileModelAtURL:completionHandler:error: instead.

## Declaration

```swift
class func compileModel(at modelURL: URL) throws -> URL
```

```objc
+ (NSURL *) compileModelAtURL:(NSURL *) modelURL error:(NSError **) error;
```

**Other overloads**:

```swift
class func compileModel(at modelURL: URL) async throws -> URL
```

```swift
class func compileModel(at url: URL) async throws -> URL
```

## Mentions

- [Downloading and Compiling a Model on the User’s Device](../downloading-and-compiling-a-model-on-the-user-s-device.md)

## Return Value

The local file path to the compiled model (the `.mlmodelc` file).

## Discussion

The source `.mlmodel` file must be on the device. Pass the compiled model to [`init(contentsOf:)`](./init%28contentsof%29.md) to initialize an [`MLModel`](../mlmodel.md) instance.

Listing 1. Compiling a model file and creating an `MLModel` instance from the compiled version

```swift
let compiledUrl = try MLModel.compileModel(at: modelUrl)
let model = try MLModel(contentsOf: compiledUrl)
```

Compiling can be time consuming and shouldn’t be done on the main thread.

See [Downloading and Compiling a Model on the User’s Device](../downloading-and-compiling-a-model-on-the-user-s-device.md) for more details.

## Parameters

- `modelURL`: The local file path to your downloaded `.mlmodel` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/compilemodel(at:)-6442s)*