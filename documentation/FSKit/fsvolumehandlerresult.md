# FSVolumeHandlerResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

An abstract base class for all result objects in FSKit handler-style protocols.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSVolumeHandlerResult
```

```objc
@interface FSVolumeHandlerResult : NSObject
```

## Overview

This class provides the common functionality needed for all result objects. All specialized result classes inherit from this base class.

## Topics

### Accessing attributes
- [class var requestedAttributes: FSItem.GetAttributesRequest](./fsvolumehandlerresult/requestedattributes.md)
  A set of attributes to populate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [FSActivateResult](./fsactivateresult.md)
- [FSBlockmapResult](./fsblockmapresult.md)
- [FSCheckAccessResult](./fscheckaccessresult.md)
- [FSCompleteIOResult](./fscompleteioresult.md)
- [FSCreateItemResult](./fscreateitemresult.md)
- [FSCreateLinkResult](./fscreatelinkresult.md)
- [FSDeactivateItemResult](./fsdeactivateitemresult.md)
- [FSEnumerateDirectoryResult](./fsenumeratedirectoryresult.md)
- [FSGetAttributesResult](./fsgetattributesresult.md)
- [FSGetXattrResult](./fsgetxattrresult.md)
- [FSListXattrsResult](./fslistxattrsresult.md)
- [FSLookupItemResult](./fslookupitemresult.md)
- [FSOpenItemResult](./fsopenitemresult.md)
- [FSPreallocateResult](./fspreallocateresult.md)
- [FSReadFileResult](./fsreadfileresult.md)
- [FSReadSymlinkResult](./fsreadsymlinkresult.md)
- [FSRemoveItemResult](./fsremoveitemresult.md)
- [FSRenameItemResult](./fsrenameitemresult.md)
- [FSSeekRegionResult](./fsseekregionresult.md)
- [FSSetAttributesResult](./fssetattributesresult.md)
- [FSSetXattrResult](./fssetxattrresult.md)
- [FSUpgradeItemResult](./fsupgradeitemresult.md)
- [FSVolumeRenameResult](./fsvolumerenameresult.md)
- [FSWriteFileResult](./fswritefileresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Implementing required handlers
- [FSVolume.Handler](./fsvolume/handler.md)
  Methods that all volumes implement to provide required capabilities.
- [FSVolume.PathConfOperations](./fsvolume/pathconfoperations.md)
  Properties implemented by volumes that support providing the values of system limits or options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumehandlerresult)*