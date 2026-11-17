# FSVolume.RenameFlags

**Framework**: FSKit  
**Kind**: struct  
**Role**: Structure

Behavior flags for a rename operation, corresponding to the flags accepted by `renamex_np(2)`.

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
struct RenameFlags
```

```c
enum FSRenameFlags : NSUInteger;
```

## Overview

FSKit passes these flags to [`renameItem(_:inDirectory:named:to:inDirectory:overItem:flags:context:replyHandler:)`](./handler/renameitem%28_,indirectory,named,to,indirectory,overitem,flags,context,replyhandler%29.md) so that a volume can honor them atomically as part of the rename.

## Topics

### Initializers
- [init(rawValue: UInt)](./renameflags/init%28rawvalue%29.md)
### Type Properties
- [static var exclusive: FSVolume.RenameFlags](./renameflags/exclusive.md)
  Fail with `EEXIST` if the destination already exists, as with `RENAME_EXCL`.
- [static var swap: FSVolume.RenameFlags](./renameflags/swap.md)
  Atomically exchange the source and destination items, as with `RENAME_SWAP`.
### Enumeration Cases
- [FSRenameFlagsNone](../fsrenameflags/fsrenameflagsnone.md)
  No rename flags; the operation behaves as a plain `rename(2)`.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/renameflags)*