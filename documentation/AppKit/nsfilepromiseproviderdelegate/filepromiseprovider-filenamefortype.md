# filePromiseProvider(_:fileNameForType:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Provides the drag destination file’s name.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
func filePromiseProvider(_ filePromiseProvider: NSFilePromiseProvider, fileNameForType fileType: String) -> String
```

#### Discussion

This method is called when the drag destination fulfills the file promise. Determine and return the final filename (a base filename, not a full path).

> **Note**:  Don’t start writing the file to the destination directory until the drag process is complete.  The drag process stops to wait for the method to return, and if it has to wait too long, the drag could be canceled.

 Don’t start writing the file to the destination directory until the drag process is complete.  The drag process stops to wait for the method to return, and if it has to wait too long, the drag could be canceled.

## Parameters

- `filePromiseProvider`: The file promise provider.
- `fileType`: A string describing the type of file being provided.

## See Also

- [func filePromiseProvider(NSFilePromiseProvider, writePromiseTo: URL, completionHandler: ((any Error)?) -> Void)](nsfilepromiseproviderdelegate/filepromiseprovider(_:writepromiseto:completionhandler:).md)
  Writes the contents of a promise to the specified URL.
- [func operationQueue(for: NSFilePromiseProvider) -> OperationQueue](nsfilepromiseproviderdelegate/operationqueue(for:).md)
  Returns the operation queue from which to issue the write request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromiseproviderdelegate/filepromiseprovider(_:filenamefortype:))*