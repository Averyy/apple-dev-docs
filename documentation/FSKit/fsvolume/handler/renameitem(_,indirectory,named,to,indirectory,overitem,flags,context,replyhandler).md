# renameItem(_:inDirectory:named:to:inDirectory:overItem:flags:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Renames an item, honoring the flags of `renamex_np(2)`.

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
optional func renameItem(_ item: FSItem, inDirectory sourceDirectory: FSItem, named sourceName: FSFileName, to destinationName: FSFileName, inDirectory destinationDirectory: FSItem, overItem: FSItem?, flags: FSVolume.RenameFlags, context: FSContext, replyHandler reply: @escaping @Sendable (FSRenameItemResult?, (any Error)?) -> Void)
```

```swift
optional func renameItem(_ item: FSItem, inDirectory sourceDirectory: FSItem, named sourceName: FSFileName, to destinationName: FSFileName, inDirectory destinationDirectory: FSItem, overItem: FSItem?, flags: FSVolume.RenameFlags, context: FSContext) async throws -> FSRenameItemResult
```

```objc
- (void) renameItem:(FSItem *) item inDirectory:(FSItem *) sourceDirectory named:(FSFileName *) sourceName toNewName:(FSFileName *) destinationName inDirectory:(FSItem *) destinationDirectory overItem:(FSItem *) overItem flags:(FSRenameFlags) flags context:(FSContext *) context replyHandler:(void (^)(FSRenameItemResult *result, NSError *error)) reply;
```

## Discussion

This method behaves like [`renameItem(_:inDirectory:named:to:inDirectory:overItem:context:replyHandler:)`](./renameitem%28_,indirectory,named,to,indirectory,overitem,context,replyhandler%29.md), but additionally receives the [`FSVolume.RenameFlags`](../renameflags.md) requested by the caller. Implement this method when your file system can honor `renamex_np(2)` flags such as `FSRenameFlags/swap` and `FSRenameFlags/exclusive`.

Declare the flags your file system can honor with [`supportedRenameFlags`](./supportedrenameflags.md). FSKit advertises the matching `VOL_CAP_INT_RENAME_SWAP` and `VOL_CAP_INT_RENAME_EXCL` interface capabilities, and fails any rename requesting an undeclared flag with `ENOTSUP` before calling this method. If you don’t implement [`supportedRenameFlags`](./supportedrenameflags.md), FSKit assumes no flags are supported and this method only ever receives `FSRenameFlags/none`.

> **Note**: When a volume implements this method, FSKit dispatches **every** rename to it, including plain renames, for which `flags` is `FSRenameFlags/none`, instead of [`renameItem(_:inDirectory:named:to:inDirectory:overItem:context:replyHandler:)`](./renameitem%28_,indirectory,named,to,indirectory,overitem,context,replyhandler%29.md).

## Parameters

- `item`: The file system object being renamed.
- `sourceDirectory`: The directory that currently contains the item to rename.
- `sourceName`: The name of the item within the source directory.
- `destinationName`: The new name of the item as it appears in `destinationDirectory`.
- `destinationDirectory`: The directory to contain the renamed object, which may be the same as `sourceDirectory`.
- `overItem`: The file system object if the destination exists, as discovered in a prior lookup.
- `flags`: The [`FSVolume.RenameFlags`](../renameflags.md) requested by the caller. FSKit only passes flags included in [`supportedRenameFlags`](./supportedrenameflags.md). Honor them atomically as part of the rename.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. On success, pass an instance of [`FSRenameItemResult`](../../fsrenameitemresult.md) and a `nil` error; on failure, pass the relevant error. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/renameitem(_:indirectory:named:to:indirectory:overitem:flags:context:replyhandler:))*