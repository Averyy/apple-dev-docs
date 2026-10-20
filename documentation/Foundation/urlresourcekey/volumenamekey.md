# volumeNameKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The name of the volume, returned as an string object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let volumeNameKey: URLResourceKey
```

```c
extern NSURLResourceKey const NSURLVolumeNameKey;
```

#### Discussion

Settable only if `NSURLVolumeSupportsRenamingKey` is [`true`](../../Swift/true.md).

## See Also

### Volume support keys
- [static let isMountTriggerKey: URLResourceKey](./ismounttriggerkey.md)
  Key for determining whether the URL is a file system trigger directory, returned as a Boolean `NSNumber` object (read-only). Traversing or opening a file system trigger directory causes an attempt to mount a file system on the directory.
- [static let isVolumeKey: URLResourceKey](./isvolumekey.md)
  Key for determining whether the resource is the root directory of a volume, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeCreationDateKey: URLResourceKey](./volumecreationdatekey.md)
  Key for the volume’s creation date, returned as an `NSDate` object, or `NULL` if it cannot be determined (read-only).
- [static let volumeIdentifierKey: URLResourceKey](./volumeidentifierkey.md)
  The unique identifier of the resource’s volume, returned as an `id` (read-only).
- [static let volumeLocalizedFormatDescriptionKey: URLResourceKey](./volumelocalizedformatdescriptionkey.md)
  Key for the volume’s descriptive format name, returned as an `NSString` object (read-only).
- [static let volumeLocalizedNameKey: URLResourceKey](./volumelocalizednamekey.md)
  The name of the volume as it should be displayed in the user interface, returned as an `NSString` object (read-only).
- [static let volumeMaximumFileSizeKey: URLResourceKey](./volumemaximumfilesizekey.md)
  Key for the largest file size supported by the volume in bytes, returned as a Boolean `NSNumber` object, or `nil` if it cannot be determined (read-only).
- [static let volumeResourceCountKey: URLResourceKey](./volumeresourcecountkey.md)
  Key for the total number of resources on the volume, returned as an `NSNumber` object (read-only).
- [static let volumeSupportsAccessPermissionsKey: URLResourceKey](./volumesupportsaccesspermissionskey.md)
  `true` if the volume supports setting POSIX access permissions with the `NSURLFileSecurityKey` property. (Read-only, value type boolean `NSNumber`).
- [static let volumeSupportsAdvisoryFileLockingKey: URLResourceKey](./volumesupportsadvisoryfilelockingkey.md)
  Key for determining whether the volume implements whole-file advisory locks in the style of flock, along with the `O_EXLOCK` and `O_SHLOCK` flags of the open function, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsCasePreservedNamesKey: URLResourceKey](./volumesupportscasepreservednameskey.md)
  Key for determining whether the volume supports case-preserved names, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsCaseSensitiveNamesKey: URLResourceKey](./volumesupportscasesensitivenameskey.md)
  Key for determining whether the volume supports case-sensitive names, returned as a Boolean `NSNumber` object (read-only).
- [static let volumeSupportsCompressionKey: URLResourceKey](./volumesupportscompressionkey.md)
  Whether the volume supports transparent decompression of compressed files using `decmpfs`, returned as `NSNumber` containing a Boolean value (read-only).
- [static let volumeSupportsExclusiveRenamingKey: URLResourceKey](./volumesupportsexclusiverenamingkey.md)
  Whether the volume supports exclusive renaming using `renamex_np(2)` with the `RENAME_EXCL` option, returned as `NSNumber` containing a Boolean value (read-only).
- [static let volumeSupportsExtendedSecurityKey: URLResourceKey](./volumesupportsextendedsecuritykey.md)
  Key for determining whether the volume supports extended security (access control lists), returned as a Boolean `NSNumber` object (read-only).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/volumenamekey)*