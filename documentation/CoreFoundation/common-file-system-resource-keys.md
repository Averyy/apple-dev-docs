# Common File System Resource Keys

**Framework**: Core Foundation

Keys that are applicable to file system URLs.

## Topics

### Constants
- [let kCFURLNameKey: CFString!](kcfurlnamekey.md)
  Key for the resource’s name in the file system, returned as a `CFString` object.
- [let kCFURLLocalizedNameKey: CFString!](kcfurllocalizednamekey.md)
  Key for the resource’s localized or extension-hidden name, retuned as a `CFString` object.
- [let kCFURLPathKey: CFString!](kcfurlpathkey.md)
  A `CFString` value containing the URL’s path as a file system path. (read-only)
- [let kCFURLIsRegularFileKey: CFString!](kcfurlisregularfilekey.md)
  Key for determining whether the resource is a regular file, as opposed to a directory or a symbolic link. Returned as a `CFBoolean` object.
- [let kCFURLIsDirectoryKey: CFString!](kcfurlisdirectorykey.md)
  Key for determining whether the resource is a directory, returned as a `CFBoolean` object.
- [let kCFURLIsSymbolicLinkKey: CFString!](kcfurlissymboliclinkkey.md)
  Key for determining whether the resource is a symbolic link, returned as a `CFBoolean` object.
- [let kCFURLIsVolumeKey: CFString!](kcfurlisvolumekey.md)
  Key for determining whether the resource is the root directory of a volume, returned as a `CFBoolean` object.
- [let kCFURLIsPackageKey: CFString!](kcfurlispackagekey.md)
  Key for determining whether the resource is a packaged directory, returned as a `CFBoolean` object.
- [let kCFURLIsSystemImmutableKey: CFString!](kcfurlissystemimmutablekey.md)
  Key for determining whether the resource’s system immutable bit is set, returned as a `CFBoolean` object.
- [let kCFURLIsUserImmutableKey: CFString!](kcfurlisuserimmutablekey.md)
  Key for determining whether the resource’s user immutable bit is set, returned as a `CFBoolean` object.
- [let kCFURLIsHiddenKey: CFString!](kcfurlishiddenkey.md)
  Key for determining whether the resource is normally not displayed to users, returned as a `CFBoolean` object.
- [let kCFURLHasHiddenExtensionKey: CFString!](kcfurlhashiddenextensionkey.md)
  Key for determining whether the resource’s extension is normally removed from its localized name, returned as a `CFBoolean` object.
- [let kCFURLCreationDateKey: CFString!](kcfurlcreationdatekey.md)
  Key for the resource’s creation date, returned as a `CFDate` object if the volume supports creation dates, or `nil` if creation dates are unsupported.
- [let kCFURLContentAccessDateKey: CFString!](kcfurlcontentaccessdatekey.md)
  Key for the last time the resource was accessed, returned as a `CFDate` object if the volume supports access dates, or `nil` if access dates are unsupported.
- [let kCFURLContentModificationDateKey: CFString!](kcfurlcontentmodificationdatekey.md)
  Key for the last time the resource was modified, returned as a `CFDate` object if the volume supports modification dates, or `nil` if modification dates are unsupported.
- [let kCFURLAttributeModificationDateKey: CFString!](kcfurlattributemodificationdatekey.md)
  Key for the last time the resource’s attributes were modified, returned as a `CFDate` object if the volume supports attribute modification dates, or `nil` if attribute modification dates are unsupported.
- [let kCFURLLinkCountKey: CFString!](kcfurllinkcountkey.md)
  Key for the number of hard links to the resource, returned as a `CFNumber` object.
- [let kCFURLParentDirectoryURLKey: CFString!](kcfurlparentdirectoryurlkey.md)
  Key for the parent directory of the resource, returned as a `CFURL` object, or `nil` if the resource is the root directory of its volume.
- [let kCFURLVolumeURLKey: CFString!](kcfurlvolumeurlkey.md)
  Key for the root directory of the resource’s volume, returned as a `CFURL` object.
- [let kCFURLTypeIdentifierKey: CFString!](kcfurltypeidentifierkey.md)
  Key for the resource’s uniform type identifier (UTI), returned as a `CFString` object.
- [let kCFURLLocalizedTypeDescriptionKey: CFString!](kcfurllocalizedtypedescriptionkey.md)
  Key for the resource’s localized type description, returned as a `CFString` object.
- [let kCFURLLabelNumberKey: CFString!](kcfurllabelnumberkey.md)
  Key for the resource’s label number, returned as a `CFNumber` object.
- [let kCFURLLabelColorKey: CFString!](kcfurllabelcolorkey.md)
  Key for the resource’s label color, returned as a `CFColorRef` object, or `NULL` if the resource has no label color.
- [let kCFURLLocalizedLabelKey: CFString!](kcfurllocalizedlabelkey.md)
  Key for the resource’s localized label text, returned as a `CFString` object, or `NULL` if the resource has no localized label text.
- [let kCFURLEffectiveIconKey: CFString!](kcfurleffectiveiconkey.md)
  Key for the resource’s typical icon, returned as a `CGImageRef` object.
- [let kCFURLCustomIconKey: CFString!](kcfurlcustomiconkey.md)
  Key for the icon stored with the resource, returned as a `CGImageRef` object, or `NULL` if the resource has no custom icon.
- [let kCFURLFileResourceIdentifierKey: CFString!](kcfurlfileresourceidentifierkey.md)
  Key for the resource’s unique identifier, returned as a `CFType` object.
- [let kCFURLVolumeIdentifierKey: CFString!](kcfurlvolumeidentifierkey.md)
  Key for the unique identifier of the resource’s volume, returned as a `CFType` object.
- [let kCFURLPreferredIOBlockSizeKey: CFString!](kcfurlpreferredioblocksizekey.md)
  Key for the optimal block size to use when reading or writing this file’s data, returned as a `CFNumber` object, or `NULL` if the preferred size is not available.
- [let kCFURLIsReadableKey: CFString!](kcfurlisreadablekey.md)
  Key for determining whether the current process (as determined by the EUID) can read the resource, returned as a `CFBoolean` object.
- [let kCFURLIsWritableKey: CFString!](kcfurliswritablekey.md)
  Key for determining whether the current process (as determined by the EUID) can write to the resource, returned as a `CFBoolean` object.
- [let kCFURLIsExecutableKey: CFString!](kcfurlisexecutablekey.md)
  Key for determining whether the current process (as determined by the EUID) can execute the resource (if it is a file) or search the resource (if it is a directory), returned as a `CFBoolean` object.
- [let kCFURLFileSecurityKey: CFString!](kcfurlfilesecuritykey.md)
  Key for the resource’s security information, returned as a `CFFileSecurity` object.
- [let kCFURLIsExcludedFromBackupKey: CFString!](kcfurlisexcludedfrombackupkey.md)
- [let kCFURLFileResourceTypeKey: CFString!](kcfurlfileresourcetypekey.md)
  Key for the resource’s object type, returned as a `CFString` object.

## See Also

- [File Resource Types](file-resource-types.md)
  Possible values for the [`kCFURLFileResourceTypeKey`](kcfurlfileresourcetypekey.md) key.
- [File Property Keys](file-property-keys.md)
  Keys that apply to properties of files.
- [iCloud Constants](icloud-constants.md)
  These constants can be used to determining whether a file is stored in the cloud and to obtain information about its status.
- [Volume Property Keys](volume-property-keys.md)
  Keys that apply to volumes.
- [CFError userInfo Dictionary Keys](cferror-userinfo-dictionary-keys.md)
  Keys in the userInfo dictionary of a `CFError` object when certain CFURL functions return an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/common-file-system-resource-keys)*