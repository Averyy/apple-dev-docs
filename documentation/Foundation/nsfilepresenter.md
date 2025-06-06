# NSFilePresenter

**Framework**: Foundation  
**Kind**: protocol

The interface a file coordinator uses to inform an object presenting a file about changes to that file made elsewhere in the system.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSFilePresenter : NSObjectProtocol
```

## Mentions

- [Improving performance and stability when accessing the file system](improving-performance-and-stability-when-accessing-the-file-system.md)

#### Overview

Objects that allow the user to view or edit the content of files or directories should adopt the [`NSFilePresenter`](nsfilepresenter.md) protocol. You use file presenters in conjunction with an [`NSFileCoordinator`](nsfilecoordinator.md) object to coordinate access to a file or directory among the objects of your application and between your application and other processes. When changes to an item occur, the system notifies objects that adopt this protocol and gives them a chance to respond appropriately.

Use the methods of this protocol to respond to actions about to be taken on the presented file or directory. When another object or process uses a file coordinator to begin reading or writing a file or directory, the file coordinator notifies all presented objects interested in the item first. It notifies the presenter objects by invoking one of the methods defined by this protocol on that object. The actual invocation of that method occurs on the operation queue in the [`presentedItemOperationQueue`](nsfilepresenter/presenteditemoperationqueue.md) property. Your file presenter must provide this queue. If your queue supports the concurrent execution of operations, the methods of your presenter object must be thread-safe and able to run in multiple queues simultaneously.

You can use file presenters to coordinate access to a file or directory among your application’s objects. If another process uses a file coordinator for the same file or directory, your presenter objects are similarly notified whenever the other process makes its changes. Your presenter objects are not notified about changes made directly using low-level read and write calls to the file. Only changes that go through a file coordinator result in notifications.

For information about how to use file presenters with a file coordinator object, see [`NSFileCoordinator`](nsfilecoordinator.md).

##### File Presenters and Ios

If your app enters the background with an active file presenter, any other processes that perform a coordinated read or write on the presented file can deadlock. To prevent this situation, call the coordinator’s [`removeFilePresenter(_:)`](nsfilecoordinator/removefilepresenter(_:).md) type method to remove the file presenter in the [`applicationDidEnterBackground(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationDidEnterBackground(_:)) method or in response to a [`didEnterBackgroundNotification`](https://developer.apple.com/documentation/UIKit/UIApplication/didEnterBackgroundNotification) notification. Call [`addFilePresenter(_:)`](nsfilecoordinator/addfilepresenter(_:).md) to add the file presenter again in the [`applicationWillEnterForeground(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationWillEnterForeground(_:)) method or in response to a [`willEnterForegroundNotification`](https://developer.apple.com/documentation/UIKit/UIApplication/willEnterForegroundNotification) notification.

> **Note**:  The [`UIDocument`](https://developer.apple.com/documentation/UIKit/UIDocument) class automatically removes itself when your app goes to the background. It automatically adds itself again when your app returns to the foreground.

## Topics

### Accessing File Presenter Attributes
- [var presentedItemURL: URL?](nsfilepresenter/presenteditemurl.md)
  The URL of the presented file or directory.
- [var presentedItemOperationQueue: OperationQueue](nsfilepresenter/presenteditemoperationqueue.md)
  The operation queue in which to execute presenter-related messages.
- [var primaryPresentedItemURL: URL?](nsfilepresenter/primarypresenteditemurl.md)
  The URL of a secondary item’s primary presented file or directory.
### Relinquishing Managed Files
- [func relinquishPresentedItem(toReader: ((() -> Void)?) -> Void)](nsfilepresenter/relinquishpresenteditem(toreader:).md)
  Notifies your object that another object or process wants to read the presented file or directory.
- [func relinquishPresentedItem(toWriter: ((() -> Void)?) -> Void)](nsfilepresenter/relinquishpresenteditem(towriter:).md)
  Notifies your object that another object or process wants to write to the presented file or directory.
### Handling Changes to Files
- [func savePresentedItemChanges(completionHandler: ((any Error)?) -> Void)](nsfilepresenter/savepresenteditemchanges(completionhandler:).md)
  Tells your object to save any unsaved changes for the presented item.
- [func accommodatePresentedItemDeletion(completionHandler: ((any Error)?) -> Void)](nsfilepresenter/accommodatepresenteditemdeletion(completionhandler:).md)
  Tells your object that its presented item is about to be deleted.
- [func presentedItemDidMove(to: URL)](nsfilepresenter/presenteditemdidmove(to:).md)
  Tells your object that the presented item moved or was renamed.
- [func presentedItemDidChange()](nsfilepresenter/presenteditemdidchange.md)
  Tells your object that the presented item’s contents or attributes changed.
### Responding to Version Changes
- [func presentedItemDidGain(NSFileVersion)](nsfilepresenter/presenteditemdidgain(_:).md)
  Tells the delegate that a new version of the file or file package was added.
- [func presentedItemDidLose(NSFileVersion)](nsfilepresenter/presenteditemdidlose(_:).md)
  Tells the delegate that a version of the file or file package was removed.
- [func presentedItemDidResolveConflict(NSFileVersion)](nsfilepresenter/presenteditemdidresolveconflict(_:).md)
  Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [func presentedSubitem(at: URL, didGain: NSFileVersion)](nsfilepresenter/presentedsubitem(at:didgain:).md)
  Tells the delegate that the item inside the presented directory gained a new version.
- [func presentedSubitem(at: URL, didLose: NSFileVersion)](nsfilepresenter/presentedsubitem(at:didlose:).md)
  Tells the delegate that the item inside the presented directory lost an existing version.
- [func presentedSubitem(at: URL, didResolve: NSFileVersion)](nsfilepresenter/presentedsubitem(at:didresolve:).md)
  Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.
### Handling Changes to a Presented Directory
- [func accommodatePresentedSubitemDeletion(at: URL, completionHandler: ((any Error)?) -> Void)](nsfilepresenter/accommodatepresentedsubitemdeletion(at:completionhandler:).md)
  Tells the delegate that some entity wants to delete an item that is inside of a presented directory.
- [func presentedSubitemDidAppear(at: URL)](nsfilepresenter/presentedsubitemdidappear(at:).md)
  Tells the delegate that an item was added to the presented directory.
- [func presentedSubitem(at: URL, didMoveTo: URL)](nsfilepresenter/presentedsubitem(at:didmoveto:).md)
  Tells the delegate that an item in the presented directory moved to a new location.
- [func presentedSubitemDidChange(at: URL)](nsfilepresenter/presentedsubitemdidchange(at:).md)
  Tells the delegate that the contents or attributes of the specified item changed.
### Ubiquity Change Notifications
- [var observedPresentedItemUbiquityAttributes: Set<URLResourceKey>](nsfilepresenter/observedpresenteditemubiquityattributes.md)
  A list of ubiquity attributes used to generate and send notifications whenever an attribute in the list changes.
- [func presentedItemDidChangeUbiquityAttributes(Set<URLResourceKey>)](nsfilepresenter/presenteditemdidchangeubiquityattributes(_:).md)
  Tells your object that the file or file package’s ubiquity attributes have changed.
### Instance Methods
- [func accommodatePresentedItemEviction(completionHandler: ((any Error)?) -> Void)](nsfilepresenter/accommodatepresenteditemeviction(completionhandler:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSFileAccessIntent](nsfileaccessintent.md)
  The details of a coordinated-read or coordinated-write operation.
- [class NSFileCoordinator](nsfilecoordinator.md)
  An object that coordinates the reading and writing of files and directories among file presenters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/nsfilepresenter)*