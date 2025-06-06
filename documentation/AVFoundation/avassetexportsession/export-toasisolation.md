# export(to:as:isolation:)

**Framework**: Avfoundation  
**Kind**: method

Exports the asset to the output location in the specified file type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func export(to url: URL, as fileType: AVFileType, isolation: isolated (any Actor)? = #isolation) async throws
```

#### Discussion

This method throws an error if you cancel the export or you specify a file type value that isn’t contained in the session’s [`supportedFileTypes`](avassetexportsession/supportedfiletypes.md).

You can monitor the status of an export by calling the [`states(updateInterval:)`](avassetexportsession/states(updateinterval:).md) method.

> **Note**:  You can cancel an in-progress export by calling [`cancel()`](https://developer.apple.com/documentation/Swift/Task/cancel()) on the [`Task`](https://developer.apple.com/documentation/Swift/Task) or parent task that initiated the operation.

## Parameters

- `url`: An output location to write the exported media. You can use the   property of   to determine an appropriate file extension for the specified file type.
- `fileType`: The type of file for the session to write.
- `isolation`: The isolation context.

## See Also

- [func cancelExport()](avassetexportsession/cancelexport.md)
  Cancels the execution of an export session.
- [func exportAsynchronously(completionHandler: () -> Void)](avassetexportsession/exportasynchronously(completionhandler:).md)
  Starts the asynchronous execution of an export session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/export(to:as:isolation:))*