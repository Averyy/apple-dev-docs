# lookupItem(name:in:packer:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Looks up an item within a directory and maps its disk space.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func lookupItem(name: FSFileName, in directory: FSItem, packer: FSExtentPacker) async throws -> (FSItem, FSFileName)
```

#### Discussion

This method allows the module to opportunistically supply extents, avoiding future calls to `blockmapFile(_:offset:length:flags:operationID:packer:)`. Only perform this technique opportunistically. In particular, don’t perform additional I/O to fetch extent data.

## Parameters

- `name`: The name of the file to look up.
- `directory`: The directory in which to look up the file.
- `packer`: An extent packer you use to pack the file’s allocated disk space.
- `reply`: A block or closure to indicate success or failure. If lookup succeeds, pass the found [`FSItem`](fsitem.md) and its [`FSFileName`](fsfilename.md), along with a `nil` error. If lookup fails, pass the relevant error as the third parameter; FSKit ignores any [`FSItem`](fsitem.md) or [`FSFileName`](fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; instead, return a tuple of the [`FSItem`](fsitem.md) and its [`FSFileName`](fsfilename.md) or throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumekerneloffloadediooperations/lookupitem(name:in:packer:replyhandler:))*