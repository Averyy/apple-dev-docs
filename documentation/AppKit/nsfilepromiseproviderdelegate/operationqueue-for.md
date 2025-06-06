# operationQueue(for:)

**Framework**: AppKit  
**Kind**: method

Returns the operation queue from which to issue the write request.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
optional func operationQueue(for filePromiseProvider: NSFilePromiseProvider) -> OperationQueue
```

#### Discussion

If this method isn’t implemented, the main operation queue is used. Although this method is optional, to avoid blocking your main thread, provide an operation queue other than the main operation queue.

## Parameters

- `filePromiseProvider`: The file promise provider for the operation queue.

## See Also

- [func filePromiseProvider(NSFilePromiseProvider, fileNameForType: String) -> String](nsfilepromiseproviderdelegate/filepromiseprovider(_:filenamefortype:).md)
  Provides the drag destination file’s name.
- [func filePromiseProvider(NSFilePromiseProvider, writePromiseTo: URL, completionHandler: ((any Error)?) -> Void)](nsfilepromiseproviderdelegate/filepromiseprovider(_:writepromiseto:completionhandler:).md)
  Writes the contents of a promise to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate/operationqueue(for:))*