# volumeIsInternal

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the volume’s device is connected to an internal bus, or nil if not available.

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
var volumeIsInternal: Bool? { get }
```

## See Also

### Volume status values
- [var volumeIsAutomounted: Bool?](./volumeisautomounted.md)
  A Boolean value that indicates whether the volume is automounted.
- [var volumeIsBrowsable: Bool?](./volumeisbrowsable.md)
  A Boolean value that indicates whether the volume is visible through the user interface.
- [var volumeIsEjectable: Bool?](./volumeisejectable.md)
  A Boolean value that indicates whether the volume’s media is ejectable from the drive mechanism under software control.
- [var volumeIsEncrypted: Bool?](./volumeisencrypted.md)
  A Boolean value that indicates whether the volume is encrypted.
- [var volumeIsJournaling: Bool?](./volumeisjournaling.md)
  A Boolean value that indicates whether the volume is currently using a journal for speedy recovery after an unplanned restart.
- [var volumeIsLocal: Bool?](./volumeislocal.md)
  A Boolean value that indicates whether the volume is on a local device.
- [var volumeIsReadOnly: Bool?](./volumeisreadonly.md)
  A Boolean value that indicates whether the volume is read-only.
- [var volumeIsRemovable: Bool?](./volumeisremovable.md)
  A Boolean value that indicates whether the volume’s media is removable from the drive mechanism.
- [var volumeIsRootFileSystem: Bool?](./volumeisrootfilesystem.md)
  A Boolean value that indicates whether the volume is the root file system.
- [var volumeTypeName: String?](./volumetypename.md)
  The volume’s type name, as a string.
- [var volumeSubtype: Int?](./volumesubtype.md)
  An integer value that indicates the file system subtype.
- [var volumeMountFromLocation: String?](./volumemountfromlocation.md)
  The file system device location, as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/volumeisinternal)*