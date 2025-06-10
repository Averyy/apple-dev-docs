# NSFileCoordinator

**Framework**: Foundation  
**Kind**: class

An object that coordinates the reading and writing of files and directories among file presenters.

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
class NSFileCoordinator
```

## Mentions

- [Improving performance and stability when accessing the file system](improving-performance-and-stability-when-accessing-the-file-system.md)

#### Overview

The [`NSFileCoordinator`](nsfilecoordinator.md) class coordinates the reading and writing of files and directories among multiple processes and objects in the same process. You use instances of this class as is to read from, write to, modify the attributes of, change the location of, or delete a file or directory, but before your code to perform those actions executes, the file coordinator lets registered file presenter objects perform any tasks that they might require to ensure their own integrity. For example, if you want to change the location of a file, other objects interested in that file need to know where you intend to move it so that they can update their references.

Objects that adopt the [`NSFilePresenter`](nsfilepresenter.md) protocol must register themselves with the [`NSFileCoordinator`](nsfilecoordinator.md) class to be notified of any pending changes. They do this by calling the [`addFilePresenter(_:)`](nsfilecoordinator/addfilepresenter(_:).md) class method. A file presenter must balance calls to [`addFilePresenter(_:)`](nsfilecoordinator/addfilepresenter(_:).md) with a call to [`removeFilePresenter(_:)`](nsfilecoordinator/removefilepresenter(_:).md) before being released, even in a garbage-collected application. The file presenter class maintains a list of active file presenter objects in the current application and uses that list, plus the file coordinator classes in other processes, to deliver notifications to all of the objects interested in a particular item.

Instances of [`NSFileCoordinator`](nsfilecoordinator.md) are meant to be used on a per-file-operation basis, where a file operation is something like opening and reading the contents of a file or moving a batch of files and directories to a new location. There is no benefit to keeping a file coordinator object past the length of the planned operation. In fact, because file coordinators retain file presenter objects, keeping one around could prevent the file presenter objects from being released in a timely manner.

For information about implementing a file presenter object to receive file-related notifications, see [`NSFilePresenter`](nsfilepresenter.md).

##### File Presenters and Ios

If your app or extension enters the background with an active file presenter, it may be terminated by the system in order to prevent deadlock on that file. To prevent this situation, call [`removeFilePresenter(_:)`](nsfilecoordinator/removefilepresenter(_:).md) to remove the file presenter in the [`applicationDidEnterBackground(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationDidEnterBackground(_:)) method or in response to a [`didEnterBackgroundNotification`](https://developer.apple.com/documentation/UIKit/UIApplication/didEnterBackgroundNotification) notification. Call [`addFilePresenter(_:)`](nsfilecoordinator/addfilepresenter(_:).md) to add the file presenter again in the [`applicationWillEnterForeground(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationWillEnterForeground(_:)) method or in response to a [`willEnterForegroundNotification`](https://developer.apple.com/documentation/UIKit/UIApplication/willEnterForegroundNotification) notification.

> **Note**:  The [`UIDocument`](https://developer.apple.com/documentation/UIKit/UIDocument) class automatically removes itself when your app goes to the background. It automatically adds itself again when your app returns to the foreground.

##### File Coordinators and Ios

A coordinated read or write will automatically begin a background task when granted, similar to one created with the [`beginBackgroundTask(expirationHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/beginBackgroundTask(expirationHandler:)) method. This helps ensure that your app or extension has sufficient time to finish the read or write operation if it’s suspended, without creating a deadlock on access to that file by other processes. If a process is suspended while waiting for a coordinated read or write to be granted, the request is canceled, and an `NSError` object with the code [`NSUserCancelledError`](nsusercancellederror-swift.var.md) is produced. If the background task expires, the process is terminated.

> **Note**:  The [`UIDocument`](https://developer.apple.com/documentation/UIKit/UIDocument) class automatically requests additional background time and safely performs coordinated reads and writes when loading and saving the document.

##### Threading Considerations

Each file coordinator object you create should be used on a single thread only. If you need to coordinate file operations across multiple objects in different threads, each object should create its own file coordinator.

## Topics

### Initializing a File Coordinator
- [init(filePresenter: (any NSFilePresenter)?)](nsfilecoordinator/init(filepresenter:).md)
  Initializes and returns a file coordinator object using the specified file presenter.
### Managing File Presenters
- [class func addFilePresenter(any NSFilePresenter)](nsfilecoordinator/addfilepresenter(_:).md)
  Registers the specified file presenter object so that it can receive notifications.
- [class func removeFilePresenter(any NSFilePresenter)](nsfilecoordinator/removefilepresenter(_:).md)
  Unregisters the specified file presenter object.
- [class var filePresenters: [any NSFilePresenter]](nsfilecoordinator/filepresenters.md)
  Returns an array containing the currently registered file presenter objects.
- [var purposeIdentifier: String](nsfilecoordinator/purposeidentifier.md)
  A string that uniquely identifies the file access that was performed by this file coordinator.
### Coordinating File Operations Asynchronously
- [func coordinate(with: [NSFileAccessIntent], queue: OperationQueue, byAccessor: ((any Error)?) -> Void)](nsfilecoordinator/coordinate(with:queue:byaccessor:).md)
  Performs a number of coordinated-read or -write operations asynchronously.
### Coordinating File Operations Synchronously
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
- [func item(at: URL, willMoveTo: URL)](nsfilecoordinator/item(at:willmoveto:).md)
  Announces that your app is moving a file to a new URL.
- [func item(at: URL, didMoveTo: URL)](nsfilecoordinator/item(at:didmoveto:).md)
  Notifies relevant file presenters that the location of a file or directory changed.
- [func cancel()](nsfilecoordinator/cancel.md)
  Cancels any active file coordination calls.
### Constants
- [NSFileCoordinator.ReadingOptions](nsfilecoordinator/readingoptions.md)
  Options to use when reading the contents or attributes of a file or directory.
- [NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions.md)
  Options to use when changing the contents or attributes of a file or directory.
### Ubiquity Change Notifications
- [func item(at: URL, didChangeUbiquityAttributes: Set<URLResourceKey>)](nsfilecoordinator/item(at:didchangeubiquityattributes:).md)
  Tells observing file providers that the item’s ubiquity attributes have changed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSFilePresenter](nsfilepresenter.md)
  The interface a file coordinator uses to inform an object presenting a file about changes to that file made elsewhere in the system.
- [class NSFileAccessIntent](nsfileaccessintent.md)
  The details of a coordinated-read or coordinated-write operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator)*