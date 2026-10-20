# operationQueue(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the operation queue from which to issue the write request.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
optional func operationQueue(for filePromiseProvider: NSFilePromiseProvider) -> OperationQueue
```

```objc
- (NSOperationQueue *) operationQueueForFilePromiseProvider:(NSFilePromiseProvider *) filePromiseProvider;
```

#### Discussion

If this method isn’t implemented, the main operation queue is used. Although this method is optional, to avoid blocking your main thread, provide an operation queue other than the main operation queue.

## Parameters

- `filePromiseProvider`: The file promise provider for the operation queue.

## See Also

### Handling File Promises
- [func filePromiseProvider(NSFilePromiseProvider, fileNameForType: String) -> String](./filepromiseprovider%28_,filenamefortype%29.md)
  Provides the drag destination file’s name.
- [func filePromiseProvider(NSFilePromiseProvider, writePromiseTo: URL, completionHandler: ((any Error)?) -> Void)](./filepromiseprovider%28_,writepromiseto,completionhandler%29.md)
  Writes the contents of a promise to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate/operationqueue(for:))*