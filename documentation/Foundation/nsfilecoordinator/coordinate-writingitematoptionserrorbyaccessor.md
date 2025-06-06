# coordinate(writingItemAt:options:error:byAccessor:)

**Framework**: Foundation  
**Kind**: method

Initiates a write operation on a single file or directory using the specified options.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func coordinate(writingItemAt url: URL, options: NSFileCoordinator.WritingOptions = [], error outError: NSErrorPointer, byAccessor writer: (URL) -> Void)
```

#### Discussion

When invoking these methods, declare a `__block` variable before the accessor block and initialize it to a value that signals failure, and then inside the accessor block set it to a value that indicates success. If the coordinated operation fails, then the accessor block never runs. The sentinel variable still holds a value that indicates failure, and the [`NSError`](nserror.md) out parameter contains a reference that describes the error.

You use this method to perform write-related operations on a file or directory in a coordinated manner. This method executes synchronously, blocking the current thread until the `writer` block finishes executing. Before executing the block, though, the file coordinator waits until other relevant file presenter objects finish in-progress actions. Similarly, your write operation may cause pending actions for other file presenters to wait until your operations are complete. Whether or not the file coordinator waits depends on whether the item being written is a file or directory and also depends on other related operations.

- If the `url` parameter specifies a file:
- This method waits for other readers and writers of the exact same file to finish in-progress actions.
- This method waits if the file is a file package or any item inside a file package and other writers are reading or writing to other items inside the package directory.
- This method does not wait for readers or writers that are manipulating the parent directory of the file, unless one of those writers specified the [`forDeleting`](nsfilecoordinator/writingoptions/fordeleting.md) or [`forMoving`](nsfilecoordinator/writingoptions/formoving.md) option.
- If the `url` parameter specifies a directory:
- This method waits if other read or write operations are occurring on the exact same directory.
- This method does not wait if read or write operations are occurring on items inside the directory (but not on the directory itself).
- This method does not wait for readers or writers that are manipulating the parent directory of the directory, unless one of those writers specified the [`forDeleting`](nsfilecoordinator/writingoptions/fordeleting.md) or [`forMoving`](nsfilecoordinator/writingoptions/formoving.md) option.

This method calls the [`relinquishPresentedItem(toWriter:)`](nsfilepresenter/relinquishpresenteditem(towriter:).md) method of any relevant file presenters. This method is called for file presenters in the current process and in other processes. Depending on the options you specify, other methods of the file presenters may also be called. When writing a file package directory, file presenter objects that are currently reading or writing the contents of that file package also receive these notifications. All of the called methods must return successfully before the file coordinator executes your block. If multiple file presenters are operating on the item, the order in which those presenters are notified is undefined.

> **Note**:  When deleting an item inside a file package using the [`forDeleting`](nsfilecoordinator/writingoptions/fordeleting.md) option, the file coordinator does not call the [`accommodatePresentedItemDeletion(completionHandler:)`](nsfilepresenter/accommodatepresenteditemdeletion(completionhandler:).md) method of any file presenters monitoring the file package directory itself. Instead, the delete operation is treated as a write operation on the file package.

With one exception, do not nest calls to file coordinator methods inside the block you pass to this method. You may call the [`coordinate(readingItemAt:options:error:byAccessor:)`](nsfilecoordinator/coordinate(readingitemat:options:error:byaccessor:).md) method to read the file if you discover through modification-date checking that the contents of the file have changed. However, if you call this method from inside your block, the file coordinator object throws an exception.

## Parameters

- `url`: A URL identifying the file or directory to write to. If other objects or processes are acting on the item at the URL, the actual URL passed to   parameter may be different from the one in this parameter.
- `options`: One of the writing options described in  . The options you specify partially determine how file presenters are notified and how this file coordinator object waits to execute your block.
- `outError`: On input, a pointer to a pointer for an error object. If a file presenter encounters an error while preparing for this write operation, that error is returned in this parameter and the block in the   parameter is not executed. If you cancel this operation before the   block is executed, this parameter contains an error object on output.
- `writer`: A   containing the file operations you want to perform in a coordinated manner. This block receives an   object containing the URL of the item and returns no value. Always use the URL passed into the block instead of the value in the   parameter.

## See Also

- [func coordinate(readingItemAt: URL, options: NSFileCoordinator.ReadingOptions, error: NSErrorPointer, byAccessor: (URL) -> Void)](nsfilecoordinator/coordinate(readingitemat:options:error:byaccessor:).md)
  Initiates a read operation on a single file or directory using the specified options.
- [func coordinate(readingItemAt: URL, options: NSFileCoordinator.ReadingOptions, writingItemAt: URL, options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (URL, URL) -> Void)](nsfilecoordinator/coordinate(readingitemat:options:writingitemat:options:error:byaccessor:).md)
  Initiates a read operation that contains a follow-up write operation.
- [func coordinate(writingItemAt: URL, options: NSFileCoordinator.WritingOptions, writingItemAt: URL, options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (URL, URL) -> Void)](nsfilecoordinator/coordinate(writingitemat:options:writingitemat:options:error:byaccessor:).md)
  Initiates a write operation that involves a secondary write operation.
- [func prepare(forReadingItemsAt: [URL], options: NSFileCoordinator.ReadingOptions, writingItemsAt: [URL], options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (() -> Void) -> Void)](nsfilecoordinator/prepare(forreadingitemsat:options:writingitemsat:options:error:byaccessor:).md)
  Prepare to read or write from multiple files in a single batch operation.
- [func item(at: URL, willMoveTo: URL)](nsfilecoordinator/item(at:willmoveto:).md)
  Announces that your app is moving a file to a new URL.
- [func item(at: URL, didMoveTo: URL)](nsfilecoordinator/item(at:didmoveto:).md)
  Notifies relevant file presenters that the location of a file or directory changed.
- [func cancel()](nsfilecoordinator/cancel.md)
  Cancels any active file coordination calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/coordinate(writingitemat:options:error:byaccessor:))*