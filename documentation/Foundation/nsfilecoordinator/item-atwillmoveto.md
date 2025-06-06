# item(at:willMoveTo:)

**Framework**: Foundation  
**Kind**: method

Announces that your app is moving a file to a new URL.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func item(at oldURL: URL, willMoveTo newURL: URL)
```

#### Discussion

This method is intended for apps that adopt App Sandbox.

Some apps need to rename files while saving them. For example, when a user adds an attachment to a rich text document, TextEdit changes the document’s filename extension from `.rtf` to `.rtfd`. In such a case, in a sandboxed app, you must call this method to declare your intent to rename a file without user approval.

After the renaming process succeeds, call the [`item(at:didMoveTo:)`](nsfilecoordinator/item(at:didmoveto:).md) method, with the same arguments, to provide your app with continued access to the file under its new name, while also giving up access to any file that appears with the old name.

If your macOS app is not sandboxed, this method serves no purpose. This method is nonfunctional in iOS.

## Parameters

- `oldURL`: The old location of the file or directory.
- `newURL`: The new location of the file or directory.

## See Also

- [func coordinate(readingItemAt: URL, options: NSFileCoordinator.ReadingOptions, error: NSErrorPointer, byAccessor: (URL) -> Void)](nsfilecoordinator/coordinate(readingitemat:options:error:byaccessor:).md)
  Initiates a read operation on a single file or directory using the specified options.
- [func coordinate(writingItemAt: URL, options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (URL) -> Void)](nsfilecoordinator/coordinate(writingitemat:options:error:byaccessor:).md)
  Initiates a write operation on a single file or directory using the specified options.
- [func coordinate(readingItemAt: URL, options: NSFileCoordinator.ReadingOptions, writingItemAt: URL, options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (URL, URL) -> Void)](nsfilecoordinator/coordinate(readingitemat:options:writingitemat:options:error:byaccessor:).md)
  Initiates a read operation that contains a follow-up write operation.
- [func coordinate(writingItemAt: URL, options: NSFileCoordinator.WritingOptions, writingItemAt: URL, options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (URL, URL) -> Void)](nsfilecoordinator/coordinate(writingitemat:options:writingitemat:options:error:byaccessor:).md)
  Initiates a write operation that involves a secondary write operation.
- [func prepare(forReadingItemsAt: [URL], options: NSFileCoordinator.ReadingOptions, writingItemsAt: [URL], options: NSFileCoordinator.WritingOptions, error: NSErrorPointer, byAccessor: (() -> Void) -> Void)](nsfilecoordinator/prepare(forreadingitemsat:options:writingitemsat:options:error:byaccessor:).md)
  Prepare to read or write from multiple files in a single batch operation.
- [func item(at: URL, didMoveTo: URL)](nsfilecoordinator/item(at:didmoveto:).md)
  Notifies relevant file presenters that the location of a file or directory changed.
- [func cancel()](nsfilecoordinator/cancel.md)
  Cancels any active file coordination calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/item(at:willmoveto:))*