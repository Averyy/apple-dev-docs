# CFError userInfo Dictionary Keys

**Framework**: Core Foundation

Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.

## Topics

### Constants
- [let kCFURLKeysOfUnsetValuesKey: CFString!](kcfurlkeysofunsetvalueskey.md)
  Key for the resource properties that have not been set after the [`CFURLSetResourcePropertiesForKeys(_:_:_:)`](cfurlsetresourcepropertiesforkeys(_:_:_:).md) function returns an error, returned as an array of `CFString` objects.

## See Also

- [Common File System Resource Keys](common-file-system-resource-keys.md)
  Keys that are applicable to file system URLs.
- [File Resource Types](file-resource-types.md)
  Possible values for the [`kCFURLFileResourceTypeKey`](kcfurlfileresourcetypekey.md) key.
- [File Property Keys](file-property-keys.md)
  Keys that apply to properties of files.
- [iCloud Constants](icloud-constants.md)
  These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.
- [Volume Property Keys](volume-property-keys.md)
  Keys that apply to volumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cferror-userinfo-dictionary-keys)*