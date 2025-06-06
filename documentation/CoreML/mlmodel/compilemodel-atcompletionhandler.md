# compileModel(at:completionHandler:)

**Framework**: Core ML  
**Kind**: method

Compile a model for a device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class func compileModel(at url: URL, completionHandler handler: @escaping (Result<URL, any Error>) -> Void)
```

## Parameters

- `url`: The URL to the model file.
- `handler`: The completion handler the framework calls when the compilation completes.

## See Also

- [class func compileModel(at: URL) async throws -> URL](mlmodel/compilemodel(at:)-45ao6.md)
  Compile a model for a device.
- [class func compileModel(at: URL) async throws -> URL](mlmodel/compilemodel(at:)-3nea.md)
  Compile a model for a device.
- [class func compileModel(at: URL) throws -> URL](mlmodel/compilemodel(at:)-6442s.md)
  Compiles a model on the device to update the model in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/compilemodel(at:completionhandler:))*