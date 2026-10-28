# export(to:as:isolation:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Exports the asset to the output location in the specified file type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@backDeployed(before: macOS 26.0, iOS 26.0, tvOS 26.0, visionOS 26.0)
final func export(to url: URL, as fileType: AVFileType, isolation: isolated (any Actor)? = #isolation) async throws
```

## Discussion

This method throws an error if you cancel the export or you specify a file type value that isn’t contained in the session’s [`supportedFileTypes`](./supportedfiletypes.md).

You can monitor the status of an export by calling the [`states(updateInterval:)`](./states%28updateinterval%29.md) method.

> **Note**:  You can cancel an in-progress export by calling [`cancel()`](../../Swift/task/cancel%28%29.md) on the [`Task`](../../Swift/task.md) or parent task that initiated the operation.

## Parameters

- `url`: An output location to write the exported media. You can use the [`preferredFilenameExtension`](../../UniformTypeIdentifiers/uttype-swift.struct/preferredfilenameextension.md) property of [`UTType`](../../UniformTypeIdentifiers/uttype-swift.struct.md) to determine an appropriate file extension for the specified file type.
- `fileType`: The type of file for the session to write.
- `isolation`: The isolation context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/export(to:as:isolation:))*