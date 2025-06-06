# URLResourceValues

**Framework**: Foundation  
**Kind**: struct

The properties that the file system resources support.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct URLResourceValues
```

#### Overview

Not all property values exist for all file system URLs. For example, if a file is located on a volume that doesn’t support creation dates, you can request the creation date property, but the request returns `nil` and doesn’t generate an error.

Only the fields requested by the keys you pass into the `URL` function to receive this value will be populated. The other fields return `nil` regardless of the underlying property on the file system.

As a convenience, you can request volume resource values from any file system URL. The value returned reflects the property value for the volume that the resource is located on.

## Topics

### Application values
- [var applicationIsScriptable: Bool?](urlresourcevalues/applicationisscriptable.md)
  A Boolean value that indicates whether the application is scriptable.
- [var isApplication: Bool?](urlresourcevalues/isapplication.md)
  A Boolean value that indicates whether the resource is an application.
### Directory values
- [var isDirectory: Bool?](urlresourcevalues/isdirectory.md)
  A Boolean value that indicates whether the resource is a directory.
- [var directoryEntryCount: Int?](urlresourcevalues/directoryentrycount.md)
  The count of file system objects in the directory.
### File values
- [var documentIdentifier: Int?](urlresourcevalues/documentidentifier.md)
  A value that the kernel assigns to identify a document.
- [var fileContentIdentifier: Int64?](urlresourcevalues/filecontentidentifier.md)
  A value APFS assigns that identifies a file’s content data stream.
- [var fileAllocatedSize: Int?](urlresourcevalues/fileallocatedsize.md)
  The total allocated size on-disk for the file, in bytes.
- [var fileProtection: URLFileProtection?](urlresourcevalues/fileprotection.md)
  The protection level for the file.
- [var fileResourceIdentifier: (any NSCopying & NSSecureCoding & NSObjectProtocol)?](urlresourcevalues/fileresourceidentifier.md)
  An identifier for comparing two file system objects for equality.
- [var fileResourceType: URLFileResourceType?](urlresourcevalues/fileresourcetype.md)
  The type of the file system object.
- [var fileSecurity: NSFileSecurity?](urlresourcevalues/filesecurity.md)
  The file system object’s security information.
- [var fileSize: Int?](urlresourcevalues/filesize.md)
  The total file size, in bytes.
- [var isPurgeable: Bool?](urlresourcevalues/ispurgeable.md)
  A Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [var isSparse: Bool?](urlresourcevalues/issparse.md)
  A Boolean value that indicates whether the file has sparse regions.
- [var mayHaveExtendedAttributes: Bool?](urlresourcevalues/mayhaveextendedattributes.md)
  A Boolean value that indicates the file may have extended attributes.
- [var isExecutable: Bool?](urlresourcevalues/isexecutable.md)
  A Boolean value that indicates whether you can execute the file resource or search a directory resource.
- [var isRegularFile: Bool?](urlresourcevalues/isregularfile.md)
  A Boolean value that indicates whether the resource is a regular file.
- [var mayShareFileContent: Bool?](urlresourcevalues/maysharefilecontent.md)
  A Boolean value that indicates whether the cloned files and their original files may share data blocks.
- [var totalFileAllocatedSize: Int?](urlresourcevalues/totalfileallocatedsize.md)
  The total allocated size of the file, in bytes.
- [var totalFileSize: Int?](urlresourcevalues/totalfilesize.md)
  The total displayable size of the file, in bytes.
- [var fileIdentifier: UInt64?](urlresourcevalues/fileidentifier.md)
  The file system’s internal inode identifier for the item.
### Volume capacity values
- [var volumeAvailableCapacity: Int?](urlresourcevalues/volumeavailablecapacity.md)
  The volume’s available capacity, in bytes.
- [var volumeAvailableCapacityForImportantUsage: Int64?](urlresourcevalues/volumeavailablecapacityforimportantusage.md)
  The volume’s available capacity for storing important resources, in bytes.
- [var volumeAvailableCapacityForOpportunisticUsage: Int64?](urlresourcevalues/volumeavailablecapacityforopportunisticusage.md)
  The volume’s available capacity for storing nonessential resources, in bytes.
- [var volumeTotalCapacity: Int?](urlresourcevalues/volumetotalcapacity.md)
  The volume’s total capacity, in bytes.
### Volume status values
- [var volumeIsAutomounted: Bool?](urlresourcevalues/volumeisautomounted.md)
  A Boolean value that indicates whether the volume is automounted.
- [var volumeIsBrowsable: Bool?](urlresourcevalues/volumeisbrowsable.md)
  A Boolean value that indicates whether the volume is visible through the user interface.
- [var volumeIsEjectable: Bool?](urlresourcevalues/volumeisejectable.md)
  A Boolean value that indicates whether the volume’s media is ejectable from the drive mechanism under software control.
- [var volumeIsEncrypted: Bool?](urlresourcevalues/volumeisencrypted.md)
  A Boolean value that indicates whether the volume is encrypted.
- [var volumeIsInternal: Bool?](urlresourcevalues/volumeisinternal.md)
  A Boolean value that indicates whether the volume’s device is connected to an internal bus, or nil if not available.
- [var volumeIsJournaling: Bool?](urlresourcevalues/volumeisjournaling.md)
  A Boolean value that indicates whether the volume is currently using a journal for speedy recovery after an unplanned restart.
- [var volumeIsLocal: Bool?](urlresourcevalues/volumeislocal.md)
  A Boolean value that indicates whether the volume is on a local device.
- [var volumeIsReadOnly: Bool?](urlresourcevalues/volumeisreadonly.md)
  A Boolean value that indicates whether the volume is read-only.
- [var volumeIsRemovable: Bool?](urlresourcevalues/volumeisremovable.md)
  A Boolean value that indicates whether the volume’s media is removable from the drive mechanism.
- [var volumeIsRootFileSystem: Bool?](urlresourcevalues/volumeisrootfilesystem.md)
  A Boolean value that indicates whether the volume is the root file system.
- [var volumeTypeName: String?](urlresourcevalues/volumetypename.md)
  The volume’s type name, as a string.
- [var volumeSubtype: Int?](urlresourcevalues/volumesubtype.md)
  An integer value that indicates the file system subtype.
- [var volumeMountFromLocation: String?](urlresourcevalues/volumemountfromlocation.md)
  The file system device location, as a string.
### Volume support values
- [var isMountTrigger: Bool?](urlresourcevalues/ismounttrigger.md)
  A Boolean value that indicates whether this URL is a file system trigger directory.
- [var isVolume: Bool?](urlresourcevalues/isvolume.md)
  A Boolean value that indicates whether the root directory is a volume.
- [var volume: URL?](urlresourcevalues/volume.md)
  URL of the volume on which the resource is stored.
- [var volumeCreationDate: Date?](urlresourcevalues/volumecreationdate.md)
  The volume’s creation date, or `nil` if this cannot be determined.
- [var volumeIdentifier: (any NSCopying & NSSecureCoding & NSObjectProtocol)?](urlresourcevalues/volumeidentifier.md)
  An identifier that identifies the volume the file system object is on.
- [var volumeLocalizedFormatDescription: String?](urlresourcevalues/volumelocalizedformatdescription.md)
  The volume format that’s visible to the user.
- [var volumeLocalizedName: String?](urlresourcevalues/volumelocalizedname.md)
  The name of the volume that’s visible to the user.
- [var volumeMaximumFileSize: Int?](urlresourcevalues/volumemaximumfilesize.md)
  The largest file size supported by this file system, in bytes, or `nil` if this cannot be determined.
- [var volumeName: String?](urlresourcevalues/volumename.md)
  The name of the volume.
- [var volumeResourceCount: Int?](urlresourcevalues/volumeresourcecount.md)
  The total number of resources on the volume.
- [var volumeSupportsAccessPermissions: Bool?](urlresourcevalues/volumesupportsaccesspermissions.md)
  A Boolean value that indicates whether the volume supports setting standard access permissions.
- [var volumeSupportsAdvisoryFileLocking: Bool?](urlresourcevalues/volumesupportsadvisoryfilelocking.md)
  A Boolean value that indicates whether the volume implements whole-file flock(2) style advisory locks, and the O_EXLOCK and O_SHLOCK flags of the open(2) call.
- [var volumeSupportsCasePreservedNames: Bool?](urlresourcevalues/volumesupportscasepreservednames.md)
  A Boolean value that indicates whether the volume format preserves the case of file and directory names.
- [var volumeSupportsCaseSensitiveNames: Bool?](urlresourcevalues/volumesupportscasesensitivenames.md)
  A Boolean value that indicates whether the volume format treats upper and lower case characters in file and directory names as different.
- [var volumeSupportsCompression: Bool?](urlresourcevalues/volumesupportscompression.md)
  A Boolean value that indicates whether the volume supports transparent decompression of compressed files using decmpfs.
- [var volumeSupportsExclusiveRenaming: Bool?](urlresourcevalues/volumesupportsexclusiverenaming.md)
  A Boolean value that indicates whether the volume warns of a pre-existing destination when renaming a file.
- [var volumeSupportsExtendedSecurity: Bool?](urlresourcevalues/volumesupportsextendedsecurity.md)
  A Boolean value that indicates whether the volume implements extended security (ACLs).
- [var volumeSupportsFileCloning: Bool?](urlresourcevalues/volumesupportsfilecloning.md)
  A Boolean value that indicates whether the volume supports file cloning.
- [var volumeSupportsHardLinks: Bool?](urlresourcevalues/volumesupportshardlinks.md)
  A Boolean value that indicates whether the volume format supports hard links.
- [var volumeSupportsImmutableFiles: Bool?](urlresourcevalues/volumesupportsimmutablefiles.md)
  A Boolean value that indicates whether the volume supports making files immutable.
- [var volumeSupportsJournaling: Bool?](urlresourcevalues/volumesupportsjournaling.md)
  A Boolean value that indicates whether the volume format supports a journal used to speed recovery in case of unplanned restart (such as a power outage or crash).
- [var volumeSupportsPersistentIDs: Bool?](urlresourcevalues/volumesupportspersistentids.md)
  A Boolean value that indicates whether the volume format supports persistent object identifiers and can look up file system objects by their IDs.
- [var volumeSupportsRenaming: Bool?](urlresourcevalues/volumesupportsrenaming.md)
  A Boolean value that indicates whether the volume can be renamed.
- [var volumeSupportsRootDirectoryDates: Bool?](urlresourcevalues/volumesupportsrootdirectorydates.md)
  A Boolean value that indicates whether the volume supports reliable storage of times for the root directory.
- [var volumeSupportsSparseFiles: Bool?](urlresourcevalues/volumesupportssparsefiles.md)
  A Boolean value that indicates whether the volume format supports sparse files.
- [var volumeSupportsSwapRenaming: Bool?](urlresourcevalues/volumesupportsswaprenaming.md)
  A Boolean value that indicates whether the volume supports swapping source and target files when both exist.
- [var volumeSupportsSymbolicLinks: Bool?](urlresourcevalues/volumesupportssymboliclinks.md)
  A Boolean value that indicates whether the volume format supports symbolic links.
- [var volumeSupportsVolumeSizes: Bool?](urlresourcevalues/volumesupportsvolumesizes.md)
  A Boolean value that indicates whether the volume supports returning volume size values.
- [var volumeSupportsZeroRuns: Bool?](urlresourcevalues/volumesupportszeroruns.md)
  A Boolean value that indicates whether the volume keeps track of allocated but unwritten parts of a file so that it can substitute zeroes without actually writing zeroes to the media.
- [var volumeURLForRemounting: URL?](urlresourcevalues/volumeurlforremounting.md)
  The `URL` needed to remount a network volume, or `nil` if not available.
- [var volumeUUIDString: String?](urlresourcevalues/volumeuuidstring.md)
  The volume’s persistent `UUID` as a string, or `nil` if a persistent `UUID` is not available for the volume.
### Ubiquitous values
- [var isUbiquitousItem: Bool?](urlresourcevalues/isubiquitousitem.md)
  A Boolean value that indicates whether the item is in the iCloud storage.
- [var ubiquitousItemIsShared: Bool?](urlresourcevalues/ubiquitousitemisshared.md)
  A Boolean value that indicates a shared item.
- [var ubiquitousItemIsExcludedFromSync: Bool?](urlresourcevalues/ubiquitousitemisexcludedfromsync.md)
  A Boolean value that indicates the system excludes the item from syncing.
- [var ubiquitousSharedItemCurrentUserPermissions: URLUbiquitousSharedItemPermissions?](urlresourcevalues/ubiquitousshareditemcurrentuserpermissions.md)
  The current user’s permissions for the shared item.
- [var ubiquitousSharedItemCurrentUserRole: URLUbiquitousSharedItemRole?](urlresourcevalues/ubiquitousshareditemcurrentuserrole.md)
  The current user’s role for the shared item.
- [var ubiquitousSharedItemMostRecentEditorNameComponents: PersonNameComponents?](urlresourcevalues/ubiquitousshareditemmostrecenteditornamecomponents.md)
  The name components of the most recent editor of the shared item.
- [var ubiquitousSharedItemOwnerNameComponents: PersonNameComponents?](urlresourcevalues/ubiquitousshareditemownernamecomponents.md)
  The name components of the owner of the shared item.
- [var ubiquitousItemContainerDisplayName: String?](urlresourcevalues/ubiquitousitemcontainerdisplayname.md)
  The name of the item’s container as the system displays it to users.
- [var ubiquitousItemDownloadRequested: Bool?](urlresourcevalues/ubiquitousitemdownloadrequested.md)
  A Boolean value that indicates whether the user or the system requests a download of the item.
- [var ubiquitousItemDownloadingError: NSError?](urlresourcevalues/ubiquitousitemdownloadingerror.md)
  The error when downloading the item from iCloud fails.
- [var ubiquitousItemDownloadingStatus: URLUbiquitousItemDownloadingStatus?](urlresourcevalues/ubiquitousitemdownloadingstatus.md)
  The download status of the item.
- [var ubiquitousItemHasUnresolvedConflicts: Bool?](urlresourcevalues/ubiquitousitemhasunresolvedconflicts.md)
  A Boolean value that indicates whether the item has outstanding conflicts.
- [var ubiquitousItemIsDownloading: Bool?](urlresourcevalues/ubiquitousitemisdownloading.md)
  A Boolean value that indicates whether the system is downloading the item.
- [var ubiquitousItemIsUploaded: Bool?](urlresourcevalues/ubiquitousitemisuploaded.md)
  A Boolean value that indicates whether data is present in the cloud for the item.
- [var ubiquitousItemIsUploading: Bool?](urlresourcevalues/ubiquitousitemisuploading.md)
  A Boolean value that indicates whether the system is uploading the item.
- [var ubiquitousItemUploadingError: NSError?](urlresourcevalues/ubiquitousitemuploadingerror.md)
  The error when uploading the item to iCloud fails.
### Thumbnail values
- [var thumbnail: NSImage?](urlresourcevalues/thumbnail.md)
  A thumbnail image of the URL.
- [var thumbnailDictionary: [URLThumbnailDictionaryItem : UIImage]?](urlresourcevalues/thumbnaildictionary-7jyzz.md)
  A dictionary of UIKit image objects keyed by size.
- [var thumbnailDictionary: [URLThumbnailDictionaryItem : NSImage]?](urlresourcevalues/thumbnaildictionary-4ztst.md)
  A dictionary of AppKit image objects keyed by size.
### Universal resource values
- [var addedToDirectoryDate: Date?](urlresourcevalues/addedtodirectorydate.md)
  The date the resource was created, or renamed into or within its parent directory.
- [var allValues: [URLResourceKey : Any]](urlresourcevalues/allvalues.md)
  A loosely-typed dictionary containing all keys and values.
- [var attributeModificationDate: Date?](urlresourcevalues/attributemodificationdate.md)
  The time the resource’s attributes were last modified.
- [var canonicalPath: String?](urlresourcevalues/canonicalpath.md)
  The URL’s path as a canonical absolute file system path.
- [var contentAccessDate: Date?](urlresourcevalues/contentaccessdate.md)
  The date the resource was last accessed.
- [var contentModificationDate: Date?](urlresourcevalues/contentmodificationdate.md)
  The time the resource content was last modified.
- [var creationDate: Date?](urlresourcevalues/creationdate.md)
  The date the resource was created.
- [var customIcon: NSImage?](urlresourcevalues/customicon.md)
- [var effectiveIcon: AnyObject?](urlresourcevalues/effectiveicon.md)
- [var generationIdentifier: (any NSCopying & NSSecureCoding & NSObjectProtocol)?](urlresourcevalues/generationidentifier.md)
  An opaque generation identifier which can be compared using `==` to determine if the data in a document has been modified.
- [var hasHiddenExtension: Bool?](urlresourcevalues/hashiddenextension.md)
  True for resources whose filename extension is removed from the localized name property.
- [var isAliasFile: Bool?](urlresourcevalues/isaliasfile.md)
  true if the resource is a Finder alias file or a symlink, false otherwise
- [var isExcludedFromBackup: Bool?](urlresourcevalues/isexcludedfrombackup.md)
  True if resource should be excluded from backups, false otherwise.
- [var isHidden: Bool?](urlresourcevalues/ishidden.md)
  True for resources normally not displayed to users.
- [var isPackage: Bool?](urlresourcevalues/ispackage.md)
  True for packaged directories.
- [var isReadable: Bool?](urlresourcevalues/isreadable.md)
  True if this process (as determined by EUID) can read the resource.
- [var isSymbolicLink: Bool?](urlresourcevalues/issymboliclink.md)
  True for symlinks.
- [var isSystemImmutable: Bool?](urlresourcevalues/issystemimmutable.md)
  True for system-immutable resources.
- [var isUserImmutable: Bool?](urlresourcevalues/isuserimmutable.md)
  True for user-immutable resources
- [var isWritable: Bool?](urlresourcevalues/iswritable.md)
  True if this process (as determined by EUID) can write to the resource.
- [var labelColor: NSColor?](urlresourcevalues/labelcolor.md)
- [var labelNumber: Int?](urlresourcevalues/labelnumber.md)
  The label number assigned to the resource.
- [var linkCount: Int?](urlresourcevalues/linkcount.md)
  Number of hard links to the resource.
- [var localizedLabel: String?](urlresourcevalues/localizedlabel.md)
  The user-visible label text.
- [var localizedName: String?](urlresourcevalues/localizedname.md)
  Localized or extension-hidden name as displayed to users.
- [var localizedTypeDescription: String?](urlresourcevalues/localizedtypedescription.md)
  User-visible type or “kind” description.
- [var name: String?](urlresourcevalues/name.md)
  The resource name provided by the file system.
- [var parentDirectory: URL?](urlresourcevalues/parentdirectory.md)
  The resource’s parent directory, if any.
- [var path: String?](urlresourcevalues/path.md)
  The URL’s path as a file system path.
- [var preferredIOBlockSize: Int?](urlresourcevalues/preferredioblocksize.md)
  The optimal block size when reading or writing this file’s data, or nil if not available.
- [var quarantineProperties: [String : Any]?](urlresourcevalues/quarantineproperties.md)
  The quarantine properties as defined in LSQuarantine.h. To remove quarantine information from a file, pass `nil` as the value when setting this property.
- [var tagNames: [String]?](urlresourcevalues/tagnames.md)
  The array of Tag names.
- [var typeIdentifier: String?](urlresourcevalues/typeidentifier.md)
  A string that represents the identifier for the type of the resource.
- [var contentType: UTType?](urlresourcevalues/contenttype.md)
  The resource’s type.
### Initializers
- [init()](urlresourcevalues/init.md)
  Initializes a new resource values structure.

## See Also

- [func resourceValues(forKeys: Set<URLResourceKey>) throws -> URLResourceValues](url/resourcevalues(forkeys:).md)
  Returns a collection of resource values identified by the given resource keys.
- [func setResourceValues(URLResourceValues) throws](url/setresourcevalues(_:).md)
  Sets the resource value identified by a given resource key.
- [func removeCachedResourceValue(forKey: URLResourceKey)](url/removecachedresourcevalue(forkey:).md)
  Removes the cached resource value identified by a given resource value key from the URL object.
- [func removeAllCachedResourceValues()](url/removeallcachedresourcevalues.md)
  Removes all cached resource values and all temporary resource values from the URL object.
- [func setTemporaryResourceValue(any Sendable, forKey: URLResourceKey)](url/settemporaryresourcevalue(_:forkey:).md)
  Sets a temporary resource value on the URL object.
- [struct URLResourceKey](urlresourcekey.md)
  Keys that apply to file system URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues)*