# lookupItem(named:inDirectory:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Looks up an item within a directory.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func lookupItem(named name: FSFileName, inDirectory directory: FSItem) async throws -> (FSItem, FSFileName)
```

#### Discussion

If no item matching `name` exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/Foundation/NSPOSIXErrorDomain) and a code of `ENOENT`.

> 💡 **Tip**: The [`FSFileName`](fsfilename.md) sent back to the caller may differ from the `name` parameter. This flexibility allows your implementation to handle case-insensitive and case-sensitive file systems. It might also be the case that `name` uses a composed Unicode string, but the name maintained by the file system and provided to the caller is uncomposed Unicode.

## Parameters

- `name`: The name of the item to look up.
- `directory`: The directory in which to look up the item.
- `reply`: A block or closure to indicate success or failure. If lookup succeeds, pass the found [`FSItem`](fsitem.md) and its [`FSFileName`](fsfilename.md) (as saved within the file system), along with a `nil` error. If lookup fails, pass the relevant error as the third parameter; any [`FSItem`](fsitem.md) or [`FSFileName`](fsfilename.md) are ignored in this case. For an `async` Swift implementation, there’s no reply handler; simply return the [`FSItem`](fsitem.md) and [`FSFileName`](fsfilename.md) as a tuple or throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/lookupitem(named:indirectory:replyhandler:))*