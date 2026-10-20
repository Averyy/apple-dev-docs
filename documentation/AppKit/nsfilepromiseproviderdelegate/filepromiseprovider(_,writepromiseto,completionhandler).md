# filePromiseProvider(_:writePromiseTo:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Writes the contents of a promise to the specified URL.

**Availability**:
- macOS 10.12+

## Declaration

```swift
nonisolated
func filePromiseProvider(_ filePromiseProvider: NSFilePromiseProvider, writePromiseTo url: URL, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
nonisolated
func filePromiseProvider(_ filePromiseProvider: NSFilePromiseProvider, writePromiseTo url: URL) async throws
```

```objc
- (void) filePromiseProvider:(NSFilePromiseProvider *) filePromiseProvider writePromiseToURL:(NSURL *) url completionHandler:(void (^)(NSError *errorOrNil)) completionHandler;
```

#### Discussion

This method is called after the drag is complete. The request executes on the [`OperationQueue`](../../Foundation/operationqueue.md) supplied by [`operationQueue(for:)`](./operationqueue%28for%29.md).

Call the completion handler with the file contents wrapped in [`NSFileCoordinator`](../../Foundation/nsfilecoordinator.md).  Be sure to write your file to the input `url` parameter.

## Parameters

- `filePromiseProvider`: The file promise provider.
- `url`: The destination URL to write to.
- `completionHandler`: A completion handler to execute after the file has been written.

## See Also

### Handling File Promises
- [func filePromiseProvider(NSFilePromiseProvider, fileNameForType: String) -> String](./filepromiseprovider%28_,filenamefortype%29.md)
  Provides the drag destination file’s name.
- [func operationQueue(for: NSFilePromiseProvider) -> OperationQueue](./operationqueue%28for%29.md)
  Returns the operation queue from which to issue the write request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate/filepromiseprovider(_:writepromiseto:completionhandler:))*