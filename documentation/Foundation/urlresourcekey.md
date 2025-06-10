# URLResourceKey

**Framework**: Foundation  
**Kind**: struct

Keys that apply to file system URLs.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct URLResourceKey
```

#### Discussion

To request information using one of these keys, pass it to the `forKey:` parameter of the [`getResourceValue(_:forKey:)`](nsurl/getresourcevalue(_:forkey:).md) instance method.

## Topics

### Application keys
- [static let isApplicationKey: URLResourceKey](urlresourcekey/isapplicationkey.md)
- [static let applicationIsScriptableKey: URLResourceKey](urlresourcekey/applicationisscriptablekey.md)
### Directory keys
- [static let isDirectoryKey: URLResourceKey](urlresourcekey/isdirectorykey.md)
  A key for determining whether the resource is a directory.
- [static let parentDirectoryURLKey: URLResourceKey](urlresourcekey/parentdirectoryurlkey.md)
  The container directory of the resource.
- [static let directoryEntryCountKey: URLResourceKey](urlresourcekey/directoryentrycountkey.md)
  The key for a count of items in the directory.
### File keys
- [static let fileAllocatedSizeKey: URLResourceKey](urlresourcekey/fileallocatedsizekey.md)
  The key for the total allocated size on-disk for the file.
- [static let fileProtectionKey: URLResourceKey](urlresourcekey/fileprotectionkey.md)
  The key for the protection level of the file.
- [struct URLFileProtection](urlfileprotection.md)
  Protection-level values for a URL resource key.
- [static let fileContentIdentifierKey: URLResourceKey](urlresourcekey/filecontentidentifierkey.md)
  The key for a value that APFS assigns to identify a file’s content data stream.
- [static let fileResourceIdentifierKey: URLResourceKey](urlresourcekey/fileresourceidentifierkey.md)
  The key for the resource’s unique identifier.
- [static let fileResourceTypeKey: URLResourceKey](urlresourcekey/fileresourcetypekey.md)
  The key for the resource’s object type.
- [struct URLFileResourceType](urlfileresourcetype.md)
  Possible values for the type of file resource.
- [static let fileSecurityKey: URLResourceKey](urlresourcekey/filesecuritykey.md)
  The key for the resource’s security information.
- [static let fileSizeKey: URLResourceKey](urlresourcekey/filesizekey.md)
  The key for the file’s size, in bytes.
- [static let isAliasFileKey: URLResourceKey](urlresourcekey/isaliasfilekey.md)
  The key for determining whether the file is an alias.
- [static let isPackageKey: URLResourceKey](urlresourcekey/ispackagekey.md)
  The key for determining whether the resource is a file package.
- [static let isRegularFileKey: URLResourceKey](urlresourcekey/isregularfilekey.md)
  The key for determining whether the resource is a regular file rather than a directory or a symbolic link.
- [static let isPurgeableKey: URLResourceKey](urlresourcekey/ispurgeablekey.md)
  The key for a Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [static let isSparseKey: URLResourceKey](urlresourcekey/issparsekey.md)
  The key for a Boolean value that indicates whether the file has sparse regions.
- [static let mayHaveExtendedAttributesKey: URLResourceKey](urlresourcekey/mayhaveextendedattributeskey.md)
  The key for a Boolean value that indicates whether the file has extended attributes.
- [static let mayShareFileContentKey: URLResourceKey](urlresourcekey/maysharefilecontentkey.md)
  The key for a Boolean value that indicates whether cloned files and their original files may share data blocks.
- [static let preferredIOBlockSizeKey: URLResourceKey](urlresourcekey/preferredioblocksizekey.md)
  The key for the optimal block size to use when reading or writing the file’s data.
- [static let totalFileAllocatedSizeKey: URLResourceKey](urlresourcekey/totalfileallocatedsizekey.md)
  The key for the total allocated size of the file, in bytes.
- [static let totalFileSizeKey: URLResourceKey](urlresourcekey/totalfilesizekey.md)
  The key for the total displayable size of the file, in bytes.
- [static let fileIdentifierKey: URLResourceKey](urlresourcekey/fileidentifierkey.md)
  The key for the file system’s internal inode identifier for the item.
### Volume capacity keys
- [Checking Volume Storage Capacity](checking-volume-storage-capacity.md)
  Confirm that you have enough local storage space for a large amount of data.
- [static let volumeAvailableCapacityKey: URLResourceKey](urlresourcekey/volumeavailablecapacitykey.md)
  Key for the volume’s available capacity in bytes (read-only).
- [static let volumeAvailableCapacityForImportantUsageKey: URLResourceKey](urlresourcekey/volumeavailablecapacityforimportantusagekey.md)
  Key for the volume’s available capacity in bytes for storing important resources (read-only).
- [static let volumeAvailableCapacityForOpportunisticUsageKey: URLResourceKey](urlresourcekey/volumeavailablecapacityforopportunisticusagekey.md)
  Key for the volume’s available capacity in bytes for storing nonessential resources (read-only).
- [static let volumeTotalCapacityKey: URLResourceKey](urlresourcekey/volumetotalcapacitykey.md)
  Key for the volume’s total capacity in bytes (read-only).
### Volume status keys
- [static let volumeIsAutomountedKey: URLResourceKey](urlresourcekey/volumeisautomountedkey.md)
  A key for determining whether the volume is automounted.
- [static let volumeIsBrowsableKey: URLResourceKey](urlresourcekey/volumeisbrowsablekey.md)
  A key for determining whether the volume is visible in GUI-based file-browsing environments, such as the Desktop or the Finder app.
- [static let volumeIsEjectableKey: URLResourceKey](urlresourcekey/volumeisejectablekey.md)
  A key for determining whether the volume is ejectable from the drive mechanism under software control.
- [static let volumeIsEncryptedKey: URLResourceKey](urlresourcekey/volumeisencryptedkey.md)
  A key for determining whether the volume is encrypted.
- [static let volumeIsInternalKey: URLResourceKey](urlresourcekey/volumeisinternalkey.md)
  A key for determining whether the volume is connected to an internal bus.
- [static let volumeIsJournalingKey: URLResourceKey](urlresourcekey/volumeisjournalingkey.md)
  A key for determining whether the volume is currently journaling.
- [static let volumeIsLocalKey: URLResourceKey](urlresourcekey/volumeislocalkey.md)
  A key for determining whether the volume is on a local device.
- [static let volumeIsReadOnlyKey: URLResourceKey](urlresourcekey/volumeisreadonlykey.md)
  A key for determining whether the volume is read-only.
- [static let volumeIsRemovableKey: URLResourceKey](urlresourcekey/volumeisremovablekey.md)
  A key for determining whether the volume is removable from the drive mechanism.
- [static let volumeIsRootFileSystemKey: URLResourceKey](urlresourcekey/volumeisrootfilesystemkey.md)
  A key for determining whether the volume is the root file system.
- [static let volumeSupportsFileProtectionKey: URLResourceKey](urlresourcekey/volumesupportsfileprotectionkey.md)
  A Boolean value that indicates the volume supports data protection for files.
- [static let volumeTypeNameKey: URLResourceKey](urlresourcekey/volumetypenamekey.md)
  The key for the name of the file system type.
- [static let volumeSubtypeKey: URLResourceKey](urlresourcekey/volumesubtypekey.md)
  The key for the file system subtype value.
- [static let volumeMountFromLocationKey: URLResourceKey](urlresourcekey/volumemountfromlocationkey.md)
  The key for the volume mounted-from location.
### Volume support keys
- [static let isMountTriggerKey: URLResourceKey](urlresourcekey/ismounttriggerkey.md)
  Key for determining whether the URL is a file system trigger directory, returned as a Boolean `NSNumber` object (read-only). Traversing or opening a file system trigger directory causes an attempt to mount a file system on the directory.
- [static let isVolumeKey: URLResourceKey](urlresourcekey/isvolumekey.md)
  Key for determining whether the resource is the root directory of a volume, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeCreationDateKey: URLResourceKey](urlresourcekey/volumecreationdatekey.md)
  Key for the volume’s creation date, returned as an `NSDate` object, or `NULL` if it cannot be determined (read-only).
- [static let volumeIdentifierKey: URLResourceKey](urlresourcekey/volumeidentifierkey.md)
  The unique identifier of the resource’s volume, returned as an `id` (read-only).
- [static let volumeLocalizedFormatDescriptionKey: URLResourceKey](urlresourcekey/volumelocalizedformatdescriptionkey.md)
  Key for the volume’s descriptive format name, returned as an `NSString` object (read-only).
- [static let volumeLocalizedNameKey: URLResourceKey](urlresourcekey/volumelocalizednamekey.md)
  The name of the volume as it should be displayed in the user interface, returned as an `NSString` object (read-only).
- [static let volumeMaximumFileSizeKey: URLResourceKey](urlresourcekey/volumemaximumfilesizekey.md)
  Key for the largest file size supported by the volume in bytes, returned as a Boolean `NSNumber` object, or `nil` if it cannot be determined (read-only).
- [static let volumeNameKey: URLResourceKey](urlresourcekey/volumenamekey.md)
  The name of the volume, returned as an `NSString` object (read-write). Settable only if `NSURLVolumeSupportsRenamingKey` is [`true`](https://developer.apple.com/documentation/swift/true).
- [static let volumeResourceCountKey: URLResourceKey](urlresourcekey/volumeresourcecountkey.md)
  Key for the total number of resources on the volume, returned as an `NSNumber` object (read-only).
- [static let volumeSupportsAccessPermissionsKey: URLResourceKey](urlresourcekey/volumesupportsaccesspermissionskey.md)
- [static let volumeSupportsAdvisoryFileLockingKey: URLResourceKey](urlresourcekey/volumesupportsadvisoryfilelockingkey.md)
  Key for determining whether the volume implements whole-file advisory locks in the style of flock, along with the `O_EXLOCK` and `O_SHLOCK` flags of the open function, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsCasePreservedNamesKey: URLResourceKey](urlresourcekey/volumesupportscasepreservednameskey.md)
  Key for determining whether the volume supports case-preserved names, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsCaseSensitiveNamesKey: URLResourceKey](urlresourcekey/volumesupportscasesensitivenameskey.md)
  Key for determining whether the volume supports case-sensitive names, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsCompressionKey: URLResourceKey](urlresourcekey/volumesupportscompressionkey.md)
  Whether the volume supports transparent decompression of compressed files using `decmpfs`, returned as `NSNumber` containing a Boolean value (read-only).
- [static let volumeSupportsExclusiveRenamingKey: URLResourceKey](urlresourcekey/volumesupportsexclusiverenamingkey.md)
  Whether the volume supports exclusive renaming using `renamex_np(2)` with the `RENAME_EXCL` option, returned as `NSNumber` containing a Boolean value (read-only).
- [static let volumeSupportsExtendedSecurityKey: URLResourceKey](urlresourcekey/volumesupportsextendedsecuritykey.md)
  Key for determining whether the volume supports extended security (access control lists), returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsFileCloningKey: URLResourceKey](urlresourcekey/volumesupportsfilecloningkey.md)
  Whether the volume supports cloning using `clonefile(2)`, returned as `NSNumber` containing a Boolean value (read-only).
- [static let volumeSupportsHardLinksKey: URLResourceKey](urlresourcekey/volumesupportshardlinkskey.md)
  Key for determining whether the volume supports hard links, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsImmutableFilesKey: URLResourceKey](urlresourcekey/volumesupportsimmutablefileskey.md)
- [static let volumeSupportsJournalingKey: URLResourceKey](urlresourcekey/volumesupportsjournalingkey.md)
  Key for determining whether the volume supports journaling, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsPersistentIDsKey: URLResourceKey](urlresourcekey/volumesupportspersistentidskey.md)
  Key for determining whether the volume supports persistent IDs, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsRenamingKey: URLResourceKey](urlresourcekey/volumesupportsrenamingkey.md)
  Key for determining whether the volume can be renamed, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsRootDirectoryDatesKey: URLResourceKey](urlresourcekey/volumesupportsrootdirectorydateskey.md)
  Key for determining whether the volume supports reliable storage of times for the root directory, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsSparseFilesKey: URLResourceKey](urlresourcekey/volumesupportssparsefileskey.md)
  Key for determining whether the volume supports sparse files, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsSwapRenamingKey: URLResourceKey](urlresourcekey/volumesupportsswaprenamingkey.md)
  Whether the volume supports renaming using `renamex_np(2)` with the `RENAME_SWAP` option, returned as `NSNumber` containing a Boolean value (read-only).
- [static let volumeSupportsSymbolicLinksKey: URLResourceKey](urlresourcekey/volumesupportssymboliclinkskey.md)
  Key for determining whether the volume supports symbolic links, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsVolumeSizesKey: URLResourceKey](urlresourcekey/volumesupportsvolumesizeskey.md)
  Key for determining whether the volume supports returning volume size information, returned as a Boolean `NSNumber` object (read-only). If `true`, volume size information is available as values of the [`volumeTotalCapacityKey`](urlresourcekey/volumetotalcapacitykey.md) and[`volumeAvailableCapacityKey`](urlresourcekey/volumeavailablecapacitykey.md) keys.
- [static let volumeSupportsZeroRunsKey: URLResourceKey](urlresourcekey/volumesupportszerorunskey.md)
  Key for determining whether the volume supports zero runs, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeURLForRemountingKey: URLResourceKey](urlresourcekey/volumeurlforremountingkey.md)
  Key for the URL needed to remount the network volume, returned as an `NSURL` object, or `nil` if a URL is not available (read-only).
- [static let volumeURLKey: URLResourceKey](urlresourcekey/volumeurlkey.md)
  The root directory of the resource’s volume, returned as an `NSURL` object (read-only).
- [static let volumeUUIDStringKey: URLResourceKey](urlresourcekey/volumeuuidstringkey.md)
  Key for the volume’s persistent UUID, returned as an `NSString` object, or `nil` if a persistent UUID is not available (read-only).
### Ubiquitous keys
- [static let isUbiquitousItemKey: URLResourceKey](urlresourcekey/isubiquitousitemkey.md)
  The key for a Boolean value that indicates whether the item is in iCloud storage.
- [static let ubiquitousSharedItemMostRecentEditorNameComponentsKey: URLResourceKey](urlresourcekey/ubiquitousshareditemmostrecenteditornamecomponentskey.md)
  The key for the name components of the most recent editor.
- [static let ubiquitousItemDownloadRequestedKey: URLResourceKey](urlresourcekey/ubiquitousitemdownloadrequestedkey.md)
  The key for a Boolean value that indicates whether the system has already made a call [`startDownloadingUbiquitousItem(at:)`](filemanager/startdownloadingubiquitousitem(at:).md) to download the item.
- [static let ubiquitousItemIsDownloadingKey: URLResourceKey](urlresourcekey/ubiquitousitemisdownloadingkey.md)
  The key for a Boolean value that indicates whether the system is downloading the item from iCloud.
- [static let ubiquitousItemDownloadingErrorKey: URLResourceKey](urlresourcekey/ubiquitousitemdownloadingerrorkey.md)
  The key for an error object that indicates why downloading the item from iCloud fails.
- [static let ubiquitousItemDownloadingStatusKey: URLResourceKey](urlresourcekey/ubiquitousitemdownloadingstatuskey.md)
  The key for the current download state for the item.
- [struct URLUbiquitousItemDownloadingStatus](urlubiquitousitemdownloadingstatus.md)
  Values that describe the iCloud storage state of a file.
- [static let ubiquitousItemIsExcludedFromSyncKey: URLResourceKey](urlresourcekey/ubiquitousitemisexcludedfromsynckey.md)
  The key of a Boolean value that indicates whether the system excludes the item from syncing.
- [static let ubiquitousItemIsUploadedKey: URLResourceKey](urlresourcekey/ubiquitousitemisuploadedkey.md)
  The key for a Boolean value that indicates whether the system uploads the item’s data to iCloud storage.
- [static let ubiquitousItemIsUploadingKey: URLResourceKey](urlresourcekey/ubiquitousitemisuploadingkey.md)
  The key for a Boolean value that indicates whether the system is uploading the item to iCloud.
- [static let ubiquitousItemUploadingErrorKey: URLResourceKey](urlresourcekey/ubiquitousitemuploadingerrorkey.md)
  The key for an error object that indicates why uploading the item to iCloud fails.
- [static let ubiquitousItemHasUnresolvedConflictsKey: URLResourceKey](urlresourcekey/ubiquitousitemhasunresolvedconflictskey.md)
  The key for a Boolean value that indicates whether this item has outstanding conflicts.
- [static let ubiquitousItemContainerDisplayNameKey: URLResourceKey](urlresourcekey/ubiquitousitemcontainerdisplaynamekey.md)
  The key for a string that contains the name of the item’s container as it appears to the user.
- [static let ubiquitousSharedItemOwnerNameComponentsKey: URLResourceKey](urlresourcekey/ubiquitousshareditemownernamecomponentskey.md)
  The key for the name components of the item’s owner.
- [static let ubiquitousSharedItemCurrentUserPermissionsKey: URLResourceKey](urlresourcekey/ubiquitousshareditemcurrentuserpermissionskey.md)
  The key for the current user’s permissions.
- [static let ubiquitousSharedItemCurrentUserRoleKey: URLResourceKey](urlresourcekey/ubiquitousshareditemcurrentuserrolekey.md)
  The key for the role of the current user.
- [static let ubiquitousItemIsSharedKey: URLResourceKey](urlresourcekey/ubiquitousitemissharedkey.md)
  The key for a Boolean value that indicates a shared item.
- [struct URLUbiquitousSharedItemRole](urlubiquitousshareditemrole.md)
  The key for the role of a shared item.
- [struct URLUbiquitousSharedItemPermissions](urlubiquitousshareditempermissions.md)
  The key for the permissions of a shared item.
### Thumbnail keys
- [static let thumbnailKey: URLResourceKey](urlresourcekey/thumbnailkey.md)
  All thumbnails as a single NSImage (read-write).
- [static let thumbnailDictionaryKey: URLResourceKey](urlresourcekey/thumbnaildictionarykey.md)
  A dictionary of NSImage/UIImage objects keyed by size (read-write). See [`URLThumbnailDictionaryItem`](urlthumbnaildictionaryitem.md) for a list of possible keys.
- [struct URLThumbnailDictionaryItem](urlthumbnaildictionaryitem.md)
  Possible keys for the [`thumbnailDictionaryKey`](urlresourcekey/thumbnaildictionarykey.md) dictionary.
### Other resource keys
- [static let keysOfUnsetValuesKey: URLResourceKey](urlresourcekey/keysofunsetvalueskey.md)
  Key for the resource properties that have not been set after the [`setResourceValues(_:)`](nsurl/setresourcevalues(_:).md) method returns an error, returned as an array of `NSString` objects.
- [static let quarantinePropertiesKey: URLResourceKey](urlresourcekey/quarantinepropertieskey.md)
- [static let addedToDirectoryDateKey: URLResourceKey](urlresourcekey/addedtodirectorydatekey.md)
  The time at which the resource’s was created or renamed into or within its parent directory, returned as an `NSDate`. Inconsistent behavior may be observed when this attribute is requested on hard-linked items. This property is not supported by all volumes. (read-only)
- [static let attributeModificationDateKey: URLResourceKey](urlresourcekey/attributemodificationdatekey.md)
  The time at which the resource’s attributes were most recently modified, returned as an `NSDate` object if the volume supports attribute modification dates, or `nil` if attribute modification dates are unsupported (read-only).
- [static let contentAccessDateKey: URLResourceKey](urlresourcekey/contentaccessdatekey.md)
  The time at which the resource was most recently accessed.
- [static let contentModificationDateKey: URLResourceKey](urlresourcekey/contentmodificationdatekey.md)
  The time at which the resource was most recently modified.
- [static let creationDateKey: URLResourceKey](urlresourcekey/creationdatekey.md)
  The time at which the resource was created.
- [static let customIconKey: URLResourceKey](urlresourcekey/customiconkey.md)
  The icon stored with the resource, returned as an `NSImage` object, or `nil` if the resource has no custom icon.
- [static let documentIdentifierKey: URLResourceKey](urlresourcekey/documentidentifierkey.md)
  The document identifier returned as an `NSNumber` (read-only).
- [static let effectiveIconKey: URLResourceKey](urlresourcekey/effectiveiconkey.md)
  The resource’s normal icon, returned as an `NSImage` object (read-only).
- [static let generationIdentifierKey: URLResourceKey](urlresourcekey/generationidentifierkey.md)
  An opaque generation identifier, returned as an `id <NSCopying, NSCoding, NSObject>` (read-only)
- [static let hasHiddenExtensionKey: URLResourceKey](urlresourcekey/hashiddenextensionkey.md)
  Key for determining whether the resource’s extension is normally removed from its localized name, returned as a Boolean `NSNumber` object (read-write).
- [static let isExcludedFromBackupKey: URLResourceKey](urlresourcekey/isexcludedfrombackupkey.md)
  A key for indicating whether the system excludes the resource from all backups of app data.
- [static let isExecutableKey: URLResourceKey](urlresourcekey/isexecutablekey.md)
  Key for determining whether the current process (as determined by the EUID) can execute the resource (if it is a file) or search the resource (if it is a directory), returned as a Boolean `NSNumber` object (read-only).
- [static let isHiddenKey: URLResourceKey](urlresourcekey/ishiddenkey.md)
  Key for determining whether the resource is normally not displayed to users, returned as a Boolean `NSNumber` object (read-write).
- [static let isReadableKey: URLResourceKey](urlresourcekey/isreadablekey.md)
  Key for determining whether the current process (as determined by the EUID) can read the resource, returned as a Boolean `NSNumber` object (read-only).
- [static let isSymbolicLinkKey: URLResourceKey](urlresourcekey/issymboliclinkkey.md)
  Key for determining whether the resource is a symbolic link, returned as a Boolean `NSNumber` object (read-only).
- [static let isSystemImmutableKey: URLResourceKey](urlresourcekey/issystemimmutablekey.md)
  Key for determining whether the resource’s system immutable bit is set, returned as a Boolean `NSNumber` object (read-write).
- [static let isUserImmutableKey: URLResourceKey](urlresourcekey/isuserimmutablekey.md)
  Key for determining whether the resource’s user immutable bit is set, returned as a Boolean `NSNumber` object (read-write).
- [static let isWritableKey: URLResourceKey](urlresourcekey/iswritablekey.md)
  Key for determining whether the current process (as determined by the EUID) can write to the resource, returned as a Boolean `NSNumber` object (read-only).
- [static let labelColorKey: URLResourceKey](urlresourcekey/labelcolorkey.md)
  The resource’s label color, returned as an `NSColor` object, or `nil` if the resource has no label color (read-only).
- [static let labelNumberKey: URLResourceKey](urlresourcekey/labelnumberkey.md)
  The resource’s label number, returned as an `NSNumber` object (read-write).
- [static let linkCountKey: URLResourceKey](urlresourcekey/linkcountkey.md)
  The number of hard links to the resource, returned as an `NSNumber` object (read-only).
- [static let localizedLabelKey: URLResourceKey](urlresourcekey/localizedlabelkey.md)
  The resource’s localized label text, returned as an `NSString` object, or `nil` if the resource has no localized label text (read-only).
- [static let localizedNameKey: URLResourceKey](urlresourcekey/localizednamekey.md)
  The resource’s localized or extension-hidden name, returned as an `NSString` object (read-only).
- [static let localizedTypeDescriptionKey: URLResourceKey](urlresourcekey/localizedtypedescriptionkey.md)
  The resource’s localized type description, returned as an `NSString` object (read-only).
- [static let nameKey: URLResourceKey](urlresourcekey/namekey.md)
  The resource’s name in the file system, returned as an `NSString` object (read-write).
- [static let pathKey: URLResourceKey](urlresourcekey/pathkey.md)
  The file system path for the URL, returned as an [`NSString`](nsstring.md) object (read-only).
- [static let canonicalPathKey: URLResourceKey](urlresourcekey/canonicalpathkey.md)
- [static let tagNamesKey: URLResourceKey](urlresourcekey/tagnameskey.md)
  The names of tags attached to the resource, returned as an array of `NSString` values (read-write).
- [static let typeIdentifierKey: URLResourceKey](urlresourcekey/typeidentifierkey.md)
  The resource’s uniform type identifier (UTI), returned as an `NSString` object (read-only).
- [static let contentTypeKey: URLResourceKey](urlresourcekey/contenttypekey.md)
  The resource’s type.
### Initializers
- [init(String)](urlresourcekey/init(_:).md)
- [init(rawValue: String)](urlresourcekey/init(rawvalue:).md)
### Deprecated
- [static let ubiquitousItemIsDownloadedKey: URLResourceKey](urlresourcekey/ubiquitousitemisdownloadedkey.md)
  The key for a Boolean value that indicates whether the system downloaded this item’s data from iCloud storage.
- [static let ubiquitousItemPercentDownloadedKey: URLResourceKey](urlresourcekey/ubiquitousitempercentdownloadedkey.md)
  The key for a value that indicates the percentage of data that the system downloaded from iCloud storage.
- [static let ubiquitousItemPercentUploadedKey: URLResourceKey](urlresourcekey/ubiquitousitempercentuploadedkey.md)
  The key for a value that indicates the percentage of data that the system uploaded to iCloud storage.
### Type Properties
- [static let ubiquitousItemIsSyncPausedKey: URLResourceKey](urlresourcekey/ubiquitousitemissyncpausedkey.md)
- [static let ubiquitousItemSupportedSyncControlsKey: URLResourceKey](urlresourcekey/ubiquitousitemsupportedsynccontrolskey.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func resourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](nsurl/resourcevalues(forkeys:).md)
  Returns the resource values for the properties identified by specified array of keys.
- [func getResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: URLResourceKey) throws](nsurl/getresourcevalue(_:forkey:).md)
  Returns the value of the resource property for the specified key.
- [func setResourceValue(Any?, forKey: URLResourceKey) throws](nsurl/setresourcevalue(_:forkey:).md)
  Sets the URL’s resource property for a given key to a given value.
- [func setResourceValues([URLResourceKey : Any]) throws](nsurl/setresourcevalues(_:).md)
  Sets the URL’s resource properties for a given set of keys to a given set of values.
- [func removeAllCachedResourceValues()](nsurl/removeallcachedresourcevalues.md)
  Removes all cached resource values and temporary resource values from the URL object.
- [func removeCachedResourceValue(forKey: URLResourceKey)](nsurl/removecachedresourcevalue(forkey:).md)
  Removes the cached resource value identified by a given key from the URL object.
- [func setTemporaryResourceValue((any Sendable)?, forKey: URLResourceKey)](nsurl/settemporaryresourcevalue(_:forkey:).md)
  Sets a temporary resource value on the URL object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey)*