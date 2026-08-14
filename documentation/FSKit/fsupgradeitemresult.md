# FSUpgradeItemResult

**Framework**: FSKit  
**Kind**: class

The result of an upgrade-item call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSUpgradeItemResult
```

#### Overview

Use this type in your implementation of [`upgrade(_:cacheMode:context:replyHandler:)`](fsvolume/datacachehandler/upgrade(_:cachemode:context:replyhandler:).md).

## Topics

### Creating an upgrade-item result
- [init(grantedCoherency: FSVolume.KernelCacheCoherencyType)](fsupgradeitemresult/init(grantedcoherency:).md)
  Creates an upgrade-item result.
- [FSVolume.KernelCacheCoherencyType](fsvolume/kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [func upgrade(FSItem, cacheMode: FSVolume.DataCacheMode, context: FSContext, replyHandler: (FSUpgradeItemResult?, (any Error)?) -> Void)](fsvolume/datacachehandler/upgrade(_:cachemode:context:replyhandler:).md)
  Upgrades the item cache mode to a less restrictive level, allowing more caching.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsupgradeitemresult)*