# filePromiseProvider(_:fileNameForType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the drag destination file’s name.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
func filePromiseProvider(_ filePromiseProvider: NSFilePromiseProvider, fileNameForType fileType: String) -> String
```

```objc
- (NSString *) filePromiseProvider:(NSFilePromiseProvider *) filePromiseProvider fileNameForType:(NSString *) fileType;
```

## Discussion

This method is called when the drag destination fulfills the file promise. Determine and return the final filename (a base filename, not a full path).

> **Note**:  Don’t start writing the file to the destination directory until the drag process is complete.  The drag process stops to wait for the method to return, and if it has to wait too long, the drag could be canceled.

## Parameters

- `filePromiseProvider`: The file promise provider.
- `fileType`: A string describing the type of file being provided.

## See Also

### Handling File Promises
- [func filePromiseProvider(NSFilePromiseProvider, writePromiseTo: URL, completionHandler: ((any Error)?) -> Void)](./filepromiseprovider%28_,writepromiseto,completionhandler%29.md)
  Writes the contents of a promise to the specified URL.
- [func operationQueue(for: NSFilePromiseProvider) -> OperationQueue](./operationqueue%28for%29.md)
  Returns the operation queue from which to issue the write request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate/filepromiseprovider(_:filenamefortype:))*