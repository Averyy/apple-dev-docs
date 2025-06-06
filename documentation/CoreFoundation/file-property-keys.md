# File Property Keys

**Framework**: Core Foundation

Keys that apply to properties of files.

## Topics

### Constants
- [let kCFURLFileAllocatedSizeKey: CFString!](kcfurlfileallocatedsizekey.md)
  Key for the total size allocated on disk for the file, returned as an `CFNumber` object.
- [let kCFURLFileSizeKey: CFString!](kcfurlfilesizekey.md)
  Key for the file’s size in bytes, returned as a `CFNumber` object.
- [let kCFURLIsAliasFileKey: CFString!](kcfurlisaliasfilekey.md)
  Key for determining whether the file is an alias, returned as a `CFBoolean` object.
- [let kCFURLIsMountTriggerKey: CFString!](kcfurlismounttriggerkey.md)
  Key for determining whether the URL is a file system trigger directory, returned as a `CFBoolean` object. Traversing or opening a file system trigger directory causes an attempt to mount a file system on the directory.
- [let kCFURLTotalFileAllocatedSizeKey: CFString!](kcfurltotalfileallocatedsizekey.md)
  Key for the total allocated size of the file in bytes, returned as a `CFNumber` object. This includes the size of any file metadata.
- [let kCFURLTotalFileSizeKey: CFString!](kcfurltotalfilesizekey.md)
  Key for the total displayable size of the file in bytes, returned as a `CFNumber` object. This includes the size of any file metadata.

## See Also

- [Common File System Resource Keys](common-file-system-resource-keys.md)
  Keys that are applicable to file system URLs.
- [File Resource Types](file-resource-types.md)
  Possible values for the [`kCFURLFileResourceTypeKey`](kcfurlfileresourcetypekey.md) key.
- [iCloud Constants](icloud-constants.md)
  These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.
- [Volume Property Keys](volume-property-keys.md)
  Keys that apply to volumes.
- [CFError userInfo Dictionary Keys](cferror-userinfo-dictionary-keys.md)
  Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/file-property-keys)*