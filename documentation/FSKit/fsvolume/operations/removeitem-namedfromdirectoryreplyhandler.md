# removeItem(_:named:fromDirectory:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Removes an existing item from a given directory.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func removeItem(_ item: FSItem, named name: FSFileName, fromDirectory directory: FSItem) async throws
```

#### Discussion

Don’t actually remove the item object itself in your implementation; instead, only remove the given item name from the given directory. Remove and deallocate the item in `reclaimItem(_:)`.

## Parameters

- `item`: The item to remove.
- `name`: The name of the item to remove.
- `directory`: The directory from which to remove the item.
- `reply`: A block or closure to indicate success or failure. If removal fails, pass an error as the one parameter to the reply handler. If removal succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/removeitem(_:named:fromdirectory:replyhandler:))*