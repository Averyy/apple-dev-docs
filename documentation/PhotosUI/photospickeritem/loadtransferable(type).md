# loadTransferable(type:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Attempts to load an instance of the type you specify from the item provider.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func loadTransferable<T>(type: T.Type) async throws -> sending T? where T : Transferable
```

#### Return Value

A `Progress` object that reports the loading progress; otherwise, `nil` if the system doesn’t find a supported content type.

## Parameters

- `type`: A conforming type to load from an item provider.

## See Also

### Loading the provider’s contents
- [func loadTransferable<T>(type: T.Type, completionHandler: (Result<T?, any Error>) -> Void) -> Progress](./loadtransferable%28type,completionhandler%29.md)
  Attempts to load an instance of the type you specify from the item provider, with a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/photospickeritem/loadtransferable(type:))*