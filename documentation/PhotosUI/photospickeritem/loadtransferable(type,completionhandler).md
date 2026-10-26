# loadTransferable(type:completionHandler:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Attempts to load an instance of the type you specify from the item provider, with a completion handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
@discardableResult
@preconcurrency func loadTransferable<T>(type: T.Type, completionHandler: @escaping @Sendable (Result<T?, any Error>) -> Void) -> Progress where T : Transferable
```

## Parameters

- `type`: A conforming type to load from an item provider.
- `completionHandler`: The completion callback handler with a result object that contains an instance if the system finds a supported content type; otherwise, `nil`.

## See Also

### Loading the provider’s contents
- [func loadTransferable<T>(type: T.Type) async throws -> sending T?](./loadtransferable%28type%29.md)
  Attempts to load an instance of the type you specify from the item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/photospickeritem/loadtransferable(type:completionhandler:))*