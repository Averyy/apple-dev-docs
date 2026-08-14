# FSVolumeHandlerResult

**Framework**: FSKit  
**Kind**: class

An abstract base class for all result objects in FSKit handler-style protocols.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSVolumeHandlerResult
```

#### Overview

This class provides the common functionality needed for all result objects. All specialized result classes inherit from this base class.

## Topics

### Accessing attributes
- [class var requestedAttributes: FSItem.GetAttributesRequest](fsvolumehandlerresult/requestedattributes.md)
  A set of attributes to populate.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [FSActivateResult](fsactivateresult.md)
- [FSBlockmapResult](fsblockmapresult.md)
- [FSCheckAccessResult](fscheckaccessresult.md)
- [FSCompleteIOResult](fscompleteioresult.md)
- [FSCreateItemResult](fscreateitemresult.md)
- [FSCreateLinkResult](fscreatelinkresult.md)
- [FSDeactivateItemResult](fsdeactivateitemresult.md)
- [FSEnumerateDirectoryResult](fsenumeratedirectoryresult.md)
- [FSGetAttributesResult](fsgetattributesresult.md)
- [FSGetXattrResult](fsgetxattrresult.md)
- [FSListXattrsResult](fslistxattrsresult.md)
- [FSLookupItemResult](fslookupitemresult.md)
- [FSOpenItemResult](fsopenitemresult.md)
- [FSPreallocateResult](fspreallocateresult.md)
- [FSReadFileResult](fsreadfileresult.md)
- [FSReadSymlinkResult](fsreadsymlinkresult.md)
- [FSRemoveItemResult](fsremoveitemresult.md)
- [FSRenameItemResult](fsrenameitemresult.md)
- [FSSeekRegionResult](fsseekregionresult.md)
- [FSSetAttributesResult](fssetattributesresult.md)
- [FSSetXattrResult](fssetxattrresult.md)
- [FSUpgradeItemResult](fsupgradeitemresult.md)
- [FSVolumeRenameResult](fsvolumerenameresult.md)
- [FSWriteFileResult](fswritefileresult.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [FSVolume.Handler](fsvolume/handler.md)
  Methods that all volumes implement to provide required capabilities.
- [FSVolume.PathConfOperations](fsvolume/pathconfoperations.md)
  Properties implemented by volumes that support providing the values of system limits or options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumehandlerresult)*