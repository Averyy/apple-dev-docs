# supportedRenameFlags

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The subset of `renamex_np(2)` flags this volume can honor.

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
optional var supportedRenameFlags: FSVolume.RenameFlags { get }
```

```objc
@property (readonly) FSRenameFlags supportedRenameFlags;
```

## Discussion

Implement this property alongside [`renameItem(_:inDirectory:named:to:inDirectory:overItem:flags:context:replyHandler:)`](./renameitem%28_,indirectory,named,to,indirectory,overitem,flags,context,replyhandler%29.md) to declare which flags your file system supports. FSKit advertises the matching interface capabilities — `VOL_CAP_INT_RENAME_SWAP` for `FSRenameFlags/swap` and `VOL_CAP_INT_RENAME_EXCL` for `FSRenameFlags/exclusive` — so applications can discover them with `getattrlist(2)`.

> **Note**: FSKit will fail any rename requesting a flag that isn’t included here with an error code of `ENOTSUP`. If you don’t implement this property, FSKit assumes the volume supports no rename flags, and fails every flagged `renamex_np(2)` with `ENOTSUP`.

FSKit reads this value after the file system replies to the `loadResource` message. Changing the returned value during the runtime of the volume has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/supportedrenameflags)*