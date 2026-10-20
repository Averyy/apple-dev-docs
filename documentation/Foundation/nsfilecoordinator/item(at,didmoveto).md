# item(at:didMoveTo:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Notifies relevant file presenters that the location of a file or directory changed.

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
func item(at oldURL: URL, didMoveTo newURL: URL)
```

```objc
- (void) itemAtURL:(NSURL *) oldURL didMoveToURL:(NSURL *) newURL;
```

#### Discussion

If you move or rename a file or directory as part of a write operation, call this method to notify relevant file presenters that the change occurred. This method calls the [`presentedItemDidMove(to:)`](../nsfilepresenter/presenteditemdidmove%28to%29.md) method for any of the item’s file presenters.  If the item is a directory, this method calls [`presentedItemDidMove(to:)`](../nsfilepresenter/presenteditemdidmove%28to%29.md) on the file presenters for the item’s contents. Finally, it calls [`presentedSubitem(at:didMoveTo:)`](../nsfilepresenter/presentedsubitem%28at,didmoveto%29.md) on the file presenter of any directory containing the item.

You must call this method from a coordinated write block. Calling this method with the same URL in the `oldURL` and `newURL` parameters is harmless. This call must balance a call to [`item(at:willMoveTo:)`](./item%28at,willmoveto%29.md).

## Parameters

- `oldURL`: The old location of the file or directory.
- `newURL`: The new location of the file or directory.

## See Also

### Coordinating File Operations Synchronously
- [func coordinate(readingItemAt: URL, options: NSFileCoordinator.ReadingOptions, error: NSErrorPointer, byAccessor: (URL) -> Void)](./coordinate%28readingitemat,options,error,byaccessor%29.md)
  Initiates a read operation on a single file or directory using the specified options.
- [func coordinate(writingItemAt: URL, options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (URL) -> Void)](./coordinate%28writingitemat,options,error,byaccessor%29.md)
  Initiates a write operation on a single file or directory using the specified options.
- [func coordinate(readingItemAt: URL, options: NSFileCoordinator.ReadingOptions, writingItemAt: URL, options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (URL, URL) -> Void)](./coordinate%28readingitemat,options,writingitemat,options,error,byaccessor%29.md)
  Initiates a read operation that contains a follow-up write operation.
- [func coordinate(writingItemAt: URL, options: NSFileCoordinator.WritingOptions, writingItemAt: URL, options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (URL, URL) -> Void)](./coordinate%28writingitemat,options,writingitemat,options,error,byaccessor%29.md)
  Initiates a write operation that involves a secondary write operation.
- [func prepare(forReadingItemsAt: [URL], options: NSFileCoordinator.ReadingOptions, writingItemsAt: [URL], options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (() -> Void) -> Void)](./prepare%28forreadingitemsat,options,writingitemsat,options,error,byaccessor%29.md)
  Prepare to read or write from multiple files in a single batch operation.
- [func item(at: URL, willMoveTo: URL)](./item%28at,willmoveto%29.md)
  Announces that your app is moving a file to a new URL.
- [func cancel()](./cancel%28%29.md)
  Cancels any active file coordination calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/item(at:didmoveto:))*