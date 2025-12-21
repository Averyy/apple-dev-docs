# open(completionHandler:)

**Framework**: UIKit  
**Kind**: method

Opens a document asynchronously.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func open() async -> Bool
```

#### Discussion

Call this method to begin the sequence of method calls that opens and reads a document asynchronously. The method obtains the file-system location of the document from the [`fileURL`](uidocument/fileurl.md) property. After the open operation concludes, the code in `completionHandler` is executed.

You can override this method if you want custom document-opening behavior, but if you do it’s recommended that you call the superclass implementation first (`super`). If you don’t call `super`, you should use the [`NSFileCoordinator`](https://developer.apple.com/documentation/Foundation/NSFileCoordinator) class to implement coordinated reading. The default implementation calls [`performAsynchronousFileAccess(_:)`](uidocument/performasynchronousfileaccess(_:).md) to schedule the document-reading work for execution on a background queue and then, from the dispatched block, performs file coordination. The queued task then calls [`read(from:)`](uidocument/read(from:).md).

## Parameters

- `completionHandler`: The block is invoked on the main queue.

## See Also

- [func load(fromContents: Any, ofType: String?) throws](uidocument/load(fromcontents:oftype:).md)
  Loads the document data into the app’s data model.
- [func read(from: URL) throws](uidocument/read(from:).md)
  Reads the document data in a file at a specified location in the application sandbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/open(completionhandler:))*