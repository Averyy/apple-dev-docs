# volumeSupportsImmutableFiles

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the volume supports making files immutable.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var volumeSupportsImmutableFiles: Bool? { get }
```

#### Discussion

This value is `true` if the volume supports making files immutable with the [`isUserImmutableKey`](../urlresourcekey/isuserimmutablekey.md) or [`isSystemImmutableKey`](../urlresourcekey/issystemimmutablekey.md) properties.

## See Also

### Volume support values
- [var isMountTrigger: Bool?](./ismounttrigger.md)
  A Boolean value that indicates whether this URL is a file system trigger directory.
- [var isVolume: Bool?](./isvolume.md)
  A Boolean value that indicates whether the root directory is a volume.
- [var volume: URL?](./volume.md)
  URL of the volume on which the resource is stored.
- [var volumeCreationDate: Date?](./volumecreationdate.md)
  The volume’s creation date, or `nil` if this cannot be determined.
- [var volumeIdentifier: (any NSCopying & NSSecureCoding & NSObjectProtocol)?](./volumeidentifier.md)
  An identifier that identifies the volume the file system object is on.
- [var volumeLocalizedFormatDescription: String?](./volumelocalizedformatdescription.md)
  The volume format that’s visible to the user.
- [var volumeLocalizedName: String?](./volumelocalizedname.md)
  The name of the volume that’s visible to the user.
- [var volumeMaximumFileSize: Int?](./volumemaximumfilesize.md)
  The largest file size supported by this file system, in bytes, or `nil` if this cannot be determined.
- [var volumeName: String?](./volumename.md)
  The name of the volume.
- [var volumeResourceCount: Int?](./volumeresourcecount.md)
  The total number of resources on the volume.
- [var volumeSupportsAccessPermissions: Bool?](./volumesupportsaccesspermissions.md)
  A Boolean value that indicates whether the volume supports setting standard access permissions.
- [var volumeSupportsAdvisoryFileLocking: Bool?](./volumesupportsadvisoryfilelocking.md)
  A Boolean value that indicates whether the volume implements whole-file flock(2) style advisory locks, and the O_EXLOCK and O_SHLOCK flags of the open(2) call.
- [var volumeSupportsCasePreservedNames: Bool?](./volumesupportscasepreservednames.md)
  A Boolean value that indicates whether the volume format preserves the case of file and directory names.
- [var volumeSupportsCaseSensitiveNames: Bool?](./volumesupportscasesensitivenames.md)
  A Boolean value that indicates whether the volume format treats upper and lower case characters in file and directory names as different.
- [var volumeSupportsCompression: Bool?](./volumesupportscompression.md)
  A Boolean value that indicates whether the volume supports transparent decompression of compressed files using decmpfs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/volumesupportsimmutablefiles)*