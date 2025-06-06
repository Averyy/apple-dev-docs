# volumeCreationDate

**Framework**: Foundation  
**Kind**: property

The volume’s creation date, or `nil` if this cannot be determined.

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
var volumeCreationDate: Date? { get }
```

## See Also

- [var isMountTrigger: Bool?](urlresourcevalues/ismounttrigger.md)
  A Boolean value that indicates whether this URL is a file system trigger directory.
- [var isVolume: Bool?](urlresourcevalues/isvolume.md)
  A Boolean value that indicates whether the root directory is a volume.
- [var volume: URL?](urlresourcevalues/volume.md)
  URL of the volume on which the resource is stored.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/volumecreationdate)*