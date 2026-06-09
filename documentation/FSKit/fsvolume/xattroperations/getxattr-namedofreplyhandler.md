# getXattr(named:of:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Gets the specified extended attribute of the given item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func xattr(named name: FSFileName, of item: FSItem) async throws -> Data
```

## Parameters

- `name`: The extended attribute name.
- `item`: The item for which to get the extended attribute.
- `reply`: A block or closure to indicate success or failure. If getting the attribute succeeds, pass an data instance containing the extended attribute data and a `nil` error. If getting the attribute fails, pass the relevant error as the second parameter; FSKit ignores any data in this case. For an `async` Swift implementation, there’s no reply handler; simply return the data or throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/getxattr(named:of:replyhandler:))*