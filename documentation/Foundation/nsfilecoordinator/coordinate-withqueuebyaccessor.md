# coordinate(with:queue:byAccessor:)

**Framework**: Foundation  
**Kind**: method

Performs a number of coordinated-read or -write operations asynchronously.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func coordinate(with intents: [NSFileAccessIntent], queue: OperationQueue, byAccessor accessor: @escaping ((any Error)?) -> Void)
```

## Mentions

- [Improving performance and stability when accessing the file system](improving-performance-and-stability-when-accessing-the-file-system.md)

#### Discussion

This method lets you asynchronously perform coordinated read or writes. You can specify any combination of individual read or write operations. The file coordinator waits asynchronously to get access to the files and then invokes the accessor block on the specified queue.

If an error occurs while waiting for access, an error message is passed to the block. You must check the block’s error parameter before accessing any of the files. If the error parameter is set to `nil`, you can freely perform the read and write operations described by your intents. Otherwise, you may not access the files.

Additionally, always use the URL property of your intent objects when accessing the files inside the accessor block. The system updates this property to account for any changes to the underlying files. For example, if the files are moved or renamed, the system updates this URL property to match.

Your file coordinator has access to the files only until the accessor block returns. Do not dispatch tasks that continue to access these files onto other threads or queues. That can cause your app to access the files outside of file coordination, and could result in data corruption or data loss.

In general, coordinated-read operations wait for coordinated-write operations on the same URL. Coordinated-write operations wait for both coordinated-read and coordinated-write operations on the same URL. Multiple coordinated reads can occur simultaneously without blocking each other.

Performing a coordinated read or coordinated write on the contents of a file package is treated as a coordinated read or write to the package as a whole. In general, coordinated access to a directory that is not a file package is not affected by coordinated access to the directory’s contents. Similarly, accessing the contents does not affect the directory. However, if you make a coordinated write operation using the [`forDeleting`](nsfilecoordinator/writingoptions/fordeleting.md), [`forMoving`](nsfilecoordinator/writingoptions/formoving.md), or [`forReplacing`](nsfilecoordinator/writingoptions/forreplacing.md) options, all coordinated access to the directory and its contents interact as if they were accessing the same URL.

Coordinated reads and writes from the same file coordinator instance never block each other. However, if you make multiple, concurrent calls to [`coordinate(with:queue:byAccessor:)`](nsfilecoordinator/coordinate(with:queue:byaccessor:).md), you risk deadlocking with another process that is similarly making multiple concurrent calls to its file coordinator. Wherever possible, invoke [`coordinate(with:queue:byAccessor:)`](nsfilecoordinator/coordinate(with:queue:byaccessor:).md) once, passing in multiple file access intent objects.

Coordinated-read and -write operations also wait on any file presenters methods that are triggered as part of the coordinated access. Coordinated access triggers method calls on all the file presenters for the same URL—even on file presenters in other processes. There is only one exception: file coordinator never sends messages to the file presenter that was passed to its [`init(filePresenter:)`](nsfilecoordinator/init(filepresenter:).md) method.

Coordinated reads trigger the following method calls:

- The [`relinquishPresentedItem(toReader:)`](nsfilepresenter/relinquishpresenteditem(toreader:).md) method is called.
- If the [`withoutChanges`](nsfilecoordinator/readingoptions/withoutchanges.md) option is not used then [`savePresentedItemChanges(completionHandler:)`](nsfilepresenter/savepresenteditemchanges(completionhandler:).md) is called.
- If the file or directory is part of a file package, these methods are also called on the package’s file presenter. If there are nested packages, the methods are called on all the packages’ file presenters.

Coordinated writes trigger the following method calls:

- The [`relinquishPresentedItem(toWriter:)`](nsfilepresenter/relinquishpresenteditem(towriter:).md) method is called. If the target is part of a file package, the method is called on the package’s presenter, just like in coordinated reads.
- If the target is a directory and the [`forDeleting`](nsfilecoordinator/writingoptions/fordeleting.md), [`forMoving`](nsfilecoordinator/writingoptions/formoving.md), or [`forReplacing`](nsfilecoordinator/writingoptions/forreplacing.md) options are used, [`relinquishPresentedItem(toWriter:)`](nsfilepresenter/relinquishpresenteditem(towriter:).md) is also called on all the file presenters for the directory’s contents.
- If the [`forDeleting`](nsfilecoordinator/writingoptions/fordeleting.md) or [`forReplacing`](nsfilecoordinator/writingoptions/forreplacing.md) options are used,  the [`accommodatePresentedItemDeletion(completionHandler:)`](nsfilepresenter/accommodatepresenteditemdeletion(completionhandler:).md) method is called. If the target is a directory, that method is called on the file presenters for the directory’s contents as well. If the target is inside a file package, the [`accommodatePresentedSubitemDeletion(at:completionHandler:)`](nsfilepresenter/accommodatepresentedsubitemdeletion(at:completionhandler:).md) method is called on the package’s presenter.
- If the [`forReplacing`](nsfilecoordinator/writingoptions/forreplacing.md) option is used, the definition of the target file or directory can vary depending on how this write operation interacts with other coordinated write operations. For more details, see [`forReplacing`](nsfilecoordinator/writingoptions/forreplacing.md).
- if the [`forMerging`](nsfilecoordinator/writingoptions/formerging.md) option is used, the [`savePresentedItemChanges(completionHandler:)`](nsfilepresenter/savepresenteditemchanges(completionhandler:).md) method is called. If the target is part of a file package, the method is called on the package’s presenter, just as with coordinated reads.

For both reading and writing, if there are multiple file presenters involved, the order in which the methods are called is undefined. If any of the file presenters signal an error, the coordinated access fails and the error is passed to the accessor block.

## Parameters

- `intents`: An array of file access intent objects, representing the individual read and write operations.
- `queue`: The operation queue on which the accessor block is executed. The queue must not be  .
- `accessor`: Do not attempt to access the files if the error parameter contains a non-  value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/coordinate(with:queue:byaccessor:))*