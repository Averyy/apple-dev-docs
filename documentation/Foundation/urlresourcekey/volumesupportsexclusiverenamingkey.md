# volumeSupportsExclusiveRenamingKey

**Framework**: Foundation  
**Kind**: property

Whether the volume supports exclusive renaming using `renamex_np(2)` with the `RENAME_EXCL` option, returned as `NSNumber` containing a Boolean value (read-only).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let volumeSupportsExclusiveRenamingKey: URLResourceKey
```

## See Also

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
- [static let volumeSupportsExtendedSecurityKey: URLResourceKey](urlresourcekey/volumesupportsextendedsecuritykey.md)
  Key for determining whether the volume supports extended security (access control lists), returned as a Boolean `NSNumber` object (read-only).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/volumesupportsexclusiverenamingkey)*