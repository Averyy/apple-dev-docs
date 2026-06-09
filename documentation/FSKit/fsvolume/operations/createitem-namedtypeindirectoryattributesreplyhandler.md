# createItem(named:type:inDirectory:attributes:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Creates a new file or directory item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func createItem(named name: FSFileName, type: FSItem.ItemType, inDirectory directory: FSItem, attributes newAttributes: FSItem.SetAttributesRequest) async throws -> (FSItem, FSFileName)
```

#### Discussion

If an item named `name` already exists in the directory indicated by `directory`, complete the request with an error with a domain of [`NSPOSIXErrorDomain`](https://developer.apple.com/documentation/Foundation/NSPOSIXErrorDomain) and a code of `EEXIST`.

## Parameters

- `name`: The new item’s name.
- `type`: The new item’s type.  Valid values are [`FSItem.ItemType.file`](fsitem/itemtype/file.md) or [`FSItem.ItemType.directory`](fsitem/itemtype/directory.md).
- `directory`: The directory in which to create the item.
- `newAttributes`: Attributes to apply to the new item.
- `reply`: A block or closure to indicate success or failure. If creation succeeds, pass the newly-created [`FSItem`](fsitem.md) and its [`FSFileName`](fsfilename.md), along with a `nil` error. If creation fails, pass the relevant error as the third parameter; FSKit ignores any [`FSItem`](fsitem.md) or [`FSFileName`](fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; simply return a tuple of the [`FSItem`](fsitem.md) and its [`FSFileName`](fsfilename.md) or throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/createitem(named:type:indirectory:attributes:replyhandler:))*