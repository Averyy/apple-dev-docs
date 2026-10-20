# FSUpgradeItemResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of an upgrade-item call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSUpgradeItemResult
```

```objc
@interface FSUpgradeItemResult : FSVolumeHandlerResult
```

#### Overview

Use this type in your implementation of [`upgrade(_:cacheMode:context:replyHandler:)`](./fsvolume/datacachehandler/upgrade%28_,cachemode,context,replyhandler%29.md).

## Topics

### Creating an upgrade-item result
- [init(grantedCoherency: FSVolume.KernelCacheCoherencyType)](./fsupgradeitemresult/init%28grantedcoherency%29.md)
  Creates an upgrade-item result.
- [FSVolume.KernelCacheCoherencyType](./fsvolume/kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](./fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Changing cache behavior
- [func upgrade(FSItem, cacheMode: FSVolume.DataCacheMode, context: FSContext, replyHandler: (FSUpgradeItemResult?, (any Error)?) -> Void)](./fsvolume/datacachehandler/upgrade%28_,cachemode,context,replyhandler%29.md)
  Upgrades the item cache mode to a less restrictive level, allowing more caching.
- [class FSItem](./fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSContext](./fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsupgradeitemresult)*