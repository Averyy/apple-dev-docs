# moveItem(at:to:)

**Framework**: Foundation  
**Kind**: method

Moves the file or directory at the specified URL to a new location synchronously.

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
func moveItem(at srcURL: URL, to dstURL: URL) throws
```

#### Discussion

When moving items, the current process must have permission to read the item at `srcURL` and write the parent directory of `dstURL`. If the item at `srcURL` is a directory, this method moves the directory and all of its contents, including any hidden files. If an item with the same name already exists at `dstURL`, this method stops the move attempt and returns an appropriate error. If the last component of `srcURL` is a symbolic link, only the link is moved to the new path; the item pointed to by the link remains at its current location.

Prior to moving the item, the file manager asks its delegate if it should actually move it. It does this by calling the [`fileManager(_:shouldMoveItemAt:to:)`](filemanagerdelegate/filemanager(_:shouldmoveitemat:to:).md) method; if that method is not implemented it calls the [`fileManager(_:shouldMoveItemAtPath:toPath:)`](filemanagerdelegate/filemanager(_:shouldmoveitematpath:topath:).md) method instead. If the item being moved is a directory, the file manager notifies the delegate only for the directory itself and not for any of its contents. If the delegate method returns [`true`](https://developer.apple.com/documentation/swift/true), or if the delegate does not implement the appropriate methods, the file manager moves the file. If there is an error moving one out of several items, the file manager may also call the delegate’s [`fileManager(_:shouldProceedAfterError:movingItemAt:to:)`](filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitemat:to:).md) or [`fileManager(_:shouldProceedAfterError:movingItemAtPath:toPath:)`](filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitematpath:topath:).md) method to determine how to proceed.

If the source and destination of the move operation are not on the same volume, this method copies the item first and then removes it from its current location. This behavior may trigger additional delegate notifications related to copying and removing individual items.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `srcURL`: The file URL that identifies the file or directory you want to move. The URL in this parameter must not be a file reference URL. This parameter must not be  .
- `dstURL`: The new location for the item in  . The URL in this parameter must not be a file reference URL and must include the name of the file or directory in its new location. This parameter must not be  .

## See Also

- [func removeItem(at: URL) throws](filemanager/removeitem(at:).md)
  Removes the file or directory at the specified URL.
- [func copyItem(at: URL, to: URL) throws](filemanager/copyitem(at:to:).md)
  Copies the file at the specified URL to a new location synchronously.
- [func copyItem(atPath: String, toPath: String) throws](filemanager/copyitem(atpath:topath:).md)
  Copies the item at the specified path to a new location synchronously.
- [func moveItem(atPath: String, toPath: String) throws](filemanager/moveitem(atpath:topath:).md)
  Moves the file or directory at the specified path to a new location synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/moveitem(at:to:))*