# fileMover(isPresented:file:onCompletion:)

**Framework**: MusicKit  
**Kind**: method

Presents a system interface for allowing the user to move an existing file to a new location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: @escaping (Result<URL, any Error>) -> Void) -> some View
```

#### Discussion

> **Note**: This interface provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

This interface provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

In order for the interface to appear, both `isPresented` must be `true` and `file` must not be `nil`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

## Parameters

- `isPresented`: A binding to whether the interface should be shown.
- `file`: The   of the file to be moved.
- `onCompletion`: A callback that will be invoked when the operation has   has succeeded or failed. To access the received URLs, call  .   When the access is no longer required, call  .
- `result`: A   indicating whether the operation succeeded or   failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/filemover(ispresented:file:oncompletion:))*