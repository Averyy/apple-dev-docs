# filePromiseProvider(_:writePromiseTo:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Writes the contents of a promise to the specified URL.

**Availability**:
- macOS 10.12+

## Declaration

```swift
nonisolated
func filePromiseProvider(_ filePromiseProvider: NSFilePromiseProvider, writePromiseTo url: URL) async throws
```

#### Discussion

This method is called after the drag is complete. The request executes on the [`OperationQueue`](https://developer.apple.com/documentation/Foundation/OperationQueue) supplied by [`operationQueue(for:)`](nsfilepromiseproviderdelegate/operationqueue(for:).md).

Call the completion handler with the file contents wrapped in [`NSFileCoordinator`](https://developer.apple.com/documentation/Foundation/NSFileCoordinator).  Be sure to write your file to the input `url` parameter.

## Parameters

- `filePromiseProvider`: The file promise provider.
- `url`: The destination URL to write to.
- `completionHandler`: A completion handler to execute after the file has been written.

## See Also

- [func filePromiseProvider(NSFilePromiseProvider, fileNameForType: String) -> String](nsfilepromiseproviderdelegate/filepromiseprovider(_:filenamefortype:).md)
  Provides the drag destination file’s name.
- [func operationQueue(for: NSFilePromiseProvider) -> OperationQueue](nsfilepromiseproviderdelegate/operationqueue(for:).md)
  Returns the operation queue from which to issue the write request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate/filepromiseprovider(_:writepromiseto:completionhandler:))*