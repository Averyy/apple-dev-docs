# coordinate(writingItemAt:options:writingItemAt:options:error:byAccessor:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initiates a write operation that involves a secondary write operation.

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
func coordinate(writingItemAt url1: URL, options options1: NSFileCoordinator.WritingOptions = [], writingItemAt url2: URL, options options2: NSFileCoordinator.WritingOptions = [], error outError: NSErrorPointer, byAccessor writer: (URL, URL) -> Void)
```

```objc
- (void) coordinateWritingItemAtURL:(NSURL *) url1 options:(NSFileCoordinatorWritingOptions) options1 writingItemAtURL:(NSURL *) url2 options:(NSFileCoordinatorWritingOptions) options2 error:(NSError **) outError byAccessor:(void (^)(NSURL *newURL1, NSURL *newURL2)) writer;
```

## Discussion

When invoking these methods, declare a `__block` variable before the accessor block and initialize it to a value that signals failure, and then inside the accessor block set it to a value that indicates success. If the coordinated operation fails, then the accessor block never runs. The sentinel variable still holds a value that indicates failure, and the [`NSError`](../nserror.md) out parameter contains a reference that describes the error.

You use this method to perform two write operations without the risk of those operations creating a deadlock. This method executes synchronously, blocking the current thread until the `writer` block finishes executing. You may call the [`coordinate(writingItemAt:options:error:byAccessor:)`](./coordinate%28writingitemat,options,error,byaccessor%29.md) method from your `writer` block. This method does the canonical lock ordering that is required to prevent a potential deadlock of the file operations.

This method makes the same calls to file presenters, and has the same general wait behavior, as the [`coordinate(writingItemAt:options:error:byAccessor:)`](./coordinate%28writingitemat,options,error,byaccessor%29.md) method.

## Parameters

- `url1`: A URL identifying the first file or directory to write. If other objects or processes are acting on the item at the URL, the actual URL passed to the block in the `writer` parameter may be different from the one in this parameter.
- `options1`: One of the writing options described in [`NSFileCoordinator.WritingOptions`](./writingoptions.md).
- `url2`: A URL identifying the other file or directory to write. If other objects or processes are acting on the item at the URL, the actual URL passed to the block in the `writer` parameter may be different from the one in this parameter.
- `options2`: One of the writing options described in [`NSFileCoordinator.WritingOptions`](./writingoptions.md). The options you specify partially determine how file presenters are notified and how this file coordinator object waits to execute your block.
- `outError`: On input, a pointer to a pointer for an error object. If a file presenter encounters an error while preparing for this operation, that error is returned in this parameter and the block in the `writer` parameter is not executed. If you cancel this operation before the `writer` block is executed, this parameter contains an error object on output.
- `writer`: A [Block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) containing the write operations you want to perform in a coordinated manner. This block receives [`NSURL`](../nsurl.md) objects containing the URLs of the items to write and returns no value. Always use the URLs passed into the block instead of the values in the `url1` and `url2` parameters.

## See Also

### Coordinating File Operations Synchronously
- [func coordinate(readingItemAt: URL, options: NSFileCoordinator.ReadingOptions, error: NSErrorPointer, byAccessor: (URL) -> Void)](./coordinate%28readingitemat,options,error,byaccessor%29.md)
  Initiates a read operation on a single file or directory using the specified options.
- [func coordinate(writingItemAt: URL, options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (URL) -> Void)](./coordinate%28writingitemat,options,error,byaccessor%29.md)
  Initiates a write operation on a single file or directory using the specified options.
- [func coordinate(readingItemAt: URL, options: NSFileCoordinator.ReadingOptions, writingItemAt: URL, options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (URL, URL) -> Void)](./coordinate%28readingitemat,options,writingitemat,options,error,byaccessor%29.md)
  Initiates a read operation that contains a follow-up write operation.
- [func prepare(forReadingItemsAt: [URL], options: NSFileCoordinator.ReadingOptions, writingItemsAt: [URL], options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (() -> Void) -> Void)](./prepare%28forreadingitemsat,options,writingitemsat,options,error,byaccessor%29.md)
  Prepare to read or write from multiple files in a single batch operation.
- [func item(at: URL, willMoveTo: URL)](./item%28at,willmoveto%29.md)
  Announces that your app is moving a file to a new URL.
- [func item(at: URL, didMoveTo: URL)](./item%28at,didmoveto%29.md)
  Notifies relevant file presenters that the location of a file or directory changed.
- [func cancel()](./cancel%28%29.md)
  Cancels any active file coordination calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/coordinate(writingitemat:options:writingitemat:options:error:byaccessor:))*