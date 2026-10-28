# volumeIsAutomountedKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A key for determining whether the volume is automounted.

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
static let volumeIsAutomountedKey: URLResourceKey
```

```c
extern NSURLResourceKey const NSURLVolumeIsAutomountedKey;
```

## Discussion

The corresponding value is a Boolean `NSNumber` object.

## See Also

### Volume status keys
- [static let volumeIsBrowsableKey: URLResourceKey](./volumeisbrowsablekey.md)
  A key for determining whether the volume is visible in GUI-based file-browsing environments, such as the Desktop or the Finder app.
- [static let volumeIsEjectableKey: URLResourceKey](./volumeisejectablekey.md)
  A key for determining whether the volume is ejectable from the drive mechanism under software control.
- [static let volumeIsEncryptedKey: URLResourceKey](./volumeisencryptedkey.md)
  A key for determining whether the volume is encrypted.
- [static let volumeIsInternalKey: URLResourceKey](./volumeisinternalkey.md)
  A key for determining whether the volume is connected to an internal bus.
- [static let volumeIsJournalingKey: URLResourceKey](./volumeisjournalingkey.md)
  A key for determining whether the volume is currently journaling.
- [static let volumeIsLocalKey: URLResourceKey](./volumeislocalkey.md)
  A key for determining whether the volume is on a local device.
- [static let volumeIsReadOnlyKey: URLResourceKey](./volumeisreadonlykey.md)
  A key for determining whether the volume is read-only.
- [static let volumeIsRemovableKey: URLResourceKey](./volumeisremovablekey.md)
  A key for determining whether the volume is removable from the drive mechanism.
- [static let volumeIsRootFileSystemKey: URLResourceKey](./volumeisrootfilesystemkey.md)
  A key for determining whether the volume is the root file system.
- [static let volumeSupportsFileProtectionKey: URLResourceKey](./volumesupportsfileprotectionkey.md)
  A Boolean value that indicates the volume supports data protection for files.
- [static let volumeTypeNameKey: URLResourceKey](./volumetypenamekey.md)
  The key for the name of the file system type.
- [static let volumeSubtypeKey: URLResourceKey](./volumesubtypekey.md)
  The key for the file system subtype value.
- [static let volumeMountFromLocationKey: URLResourceKey](./volumemountfromlocationkey.md)
  The key for the volume mounted-from location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/volumeisautomountedkey)*