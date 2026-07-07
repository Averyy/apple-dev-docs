# upgrade(_:cacheMode:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Upgrades the item cache mode to a less restrictive level, allowing more caching.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func upgrade(_ item: FSItem, cacheMode: FSVolume.DataCacheMode, context: FSContext) async throws -> FSUpgradeItemResult
```

#### Discussion

FSKit calls this method when transitioning to a cache mode that allows more aggressive caching.

## Parameters

- `item`: The item for which to upgrade the cache mode.
- `cacheMode`: The new (more permissive) cache mode being requested.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If successful, pass an instance of [`FSUpgradeItemResult`](fsupgradeitemresult.md) containing the granted [`FSVolume.KernelCacheCoherencyType`](fsvolume/kernelcachecoherencytype.md), along with a `nil` error. If upgrading fails, pass the relevant error as the second parameter; FSKit ignores the [`FSUpgradeItemResult`](fsupgradeitemresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.
- [class FSUpgradeItemResult](fsupgradeitemresult.md)
  The result of an upgrade-item call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/datacachehandler/upgrade(_:cachemode:context:replyhandler:))*