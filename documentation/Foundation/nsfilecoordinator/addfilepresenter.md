# addFilePresenter(_:)

**Framework**: Foundation  
**Kind**: method

Registers the specified file presenter object so that it can receive notifications.

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
class func addFilePresenter(_ filePresenter: any NSFilePresenter)
```

#### Discussion

This method registers the file presenter object process wide. Thus, any file coordinator objects you create later automatically know about the file presenter object and know to message it when its file or directory is affected.

Be sure to balance calls to this method with a corresponding call to the [`removeFilePresenter(_:)`](nsfilecoordinator/removefilepresenter(_:).md) method. You must remove file presenters from the process wide registry before the object is deallocated, even in a garbage-collected application.

If you call this method while coordinated file operations are already under way in another process, your file presenter may not receive notifications for that operation. To prevent missing such notifications, create a file coordinator, call its  [`coordinate(readingItemAt:options:error:byAccessor:)`](nsfilecoordinator/coordinate(readingitemat:options:error:byaccessor:).md) method, and register your file presenter object there. If you are going to read a file and then create a file presenter for that file, both actions should occur in the same coordinated read block. Synchronizing on the presented file or directory guarantees that when your block executes, all other objects have completed any tasks and you have sole access to the item.

## Parameters

- `filePresenter`: The file presenter object to register.

## See Also

- [class func removeFilePresenter(any NSFilePresenter)](nsfilecoordinator/removefilepresenter(_:).md)
  Unregisters the specified file presenter object.
- [class var filePresenters: [any NSFilePresenter]](nsfilecoordinator/filepresenters.md)
  Returns an array containing the currently registered file presenter objects.
- [var purposeIdentifier: String](nsfilecoordinator/purposeidentifier.md)
  A string that uniquely identifies the file access that was performed by this file coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/addfilepresenter(_:))*