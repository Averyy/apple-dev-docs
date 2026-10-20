# copyItem(at:to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies the file at the specified URL to a new location synchronously.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func copyItem(at srcURL: URL, to dstURL: URL) throws
```

```objc
- (BOOL) copyItemAtURL:(NSURL *) srcURL toURL:(NSURL *) dstURL error:(NSError **) error;
```

## Mentions

- [About Apple File System](../about-apple-file-system.md)

#### Discussion

When copying items, the current process must have permission to read the file or directory at `srcURL` and write the parent directory of `dstURL`. If the item at `srcURL` is a directory, this method copies the directory and all of its contents, including any hidden files. If a file with the same name already exists at `dstURL`, this method stops the copy attempt and returns an appropriate error. If the last component of `srcURL` is a symbolic link, only the link is copied to the new path.

Prior to copying each item, the file manager asks its delegate if it should actually do so. It does this by calling the [`fileManager(_:shouldCopyItemAt:to:)`](../filemanagerdelegate/filemanager%28_,shouldcopyitemat,to%29.md) method; if that method is not implemented (or the process is running in OS X 10.5 or earlier) it calls the [`fileManager(_:shouldCopyItemAtPath:toPath:)`](../filemanagerdelegate/filemanager%28_,shouldcopyitematpath,topath%29.md) method instead. If the delegate method returns [`true`](../../Swift/true.md), or if the delegate does not implement the appropriate methods, the file manager proceeds to copy the file or directory. If there is an error copying an item, the file manager may also call the delegate’s [`fileManager(_:shouldProceedAfterError:copyingItemAt:to:)`](../filemanagerdelegate/filemanager%28_,shouldproceedaftererror,copyingitemat,to%29.md) or [`fileManager(_:shouldProceedAfterError:copyingItemAtPath:toPath:)`](../filemanagerdelegate/filemanager%28_,shouldproceedaftererror,copyingitematpath,topath%29.md) method to determine how to proceed.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `srcURL`: The file URL that identifies the file you want to copy. The URL in this parameter must not be a file reference URL. This parameter must not be `nil`.
- `dstURL`: The URL at which to place the copy of `srcURL`. The URL in this parameter must not be a file reference URL and must include the name of the file in its new location. This parameter must not be `nil`.

## See Also

### Moving and copying items
- [func copyItem(atPath: String, toPath: String) throws](./copyitem%28atpath,topath%29.md)
  Copies the item at the specified path to a new location synchronously.
- [func moveItem(at: URL, to: URL) throws](./moveitem%28at,to%29.md)
  Moves the file or directory at the specified URL to a new location synchronously.
- [func moveItem(atPath: String, toPath: String) throws](./moveitem%28atpath,topath%29.md)
  Moves the file or directory at the specified path to a new location synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/copyitem(at:to:))*