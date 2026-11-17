# swap

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

Atomically exchange the source and destination items, as with `RENAME_SWAP`.

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
static var swap: FSVolume.RenameFlags { get }
```

```c
FSRenameFlagsSwap
```

## Discussion

Both the source and destination must exist. On success, the two items are exchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/renameflags/swap)*