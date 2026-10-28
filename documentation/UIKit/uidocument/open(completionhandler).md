# open(completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Opens a document asynchronously.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func open(completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func open() async -> Bool
```

```objc
- (void) openWithCompletionHandler:(void (^)(BOOL success)) completionHandler;
```

## Discussion

Call this method to begin the sequence of method calls that opens and reads a document asynchronously. The method obtains the file-system location of the document from the [`fileURL`](./fileurl.md) property. After the open operation concludes, the code in `completionHandler` is executed.

You can override this method if you want custom document-opening behavior, but if you do it’s recommended that you call the superclass implementation first (`super`). If you don’t call `super`, you should use the [`NSFileCoordinator`](../../Foundation/nsfilecoordinator.md) class to implement coordinated reading. The default implementation calls [`performAsynchronousFileAccess(_:)`](./performasynchronousfileaccess%28_%29.md) to schedule the document-reading work for execution on a background queue and then, from the dispatched block, performs file coordination. The queued task then calls [`read(from:)`](./read%28from%29.md).

## Parameters

- `completionHandler`: A block with code to execute after the open operation concludes. The block returns no value and has one parameter:

  - **`success`**: [`true`](../../Swift/true.md) if the open operation succeeds, otherwise [`false`](../../Swift/false.md).

  The block is invoked on the main queue.

## See Also

### Reading document data
- [func load(fromContents: Any, ofType: String?) throws](./load%28fromcontents,oftype%29.md)
  Loads the document data into the app’s data model.
- [func read(from: URL) throws](./read%28from%29.md)
  Reads the document data in a file at a specified location in the application sandbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/open(completionhandler:))*