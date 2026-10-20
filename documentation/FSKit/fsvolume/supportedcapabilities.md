# FSVolume.SupportedCapabilities

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A type that represents capabilities supported by a volume, such as hard and symbolic links, journaling, and large file sizes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class SupportedCapabilities
```

```objc
@interface FSVolumeSupportedCapabilities : NSObject
```

## Topics

### Declaring identifier capabilities
- [var supportsPersistentObjectIDs: Bool](./supportedcapabilities/supportspersistentobjectids.md)
  A Boolean property that indicates whether the volume supports persistent object identifiers and can look up file system objects by their IDs.
- [var supports64BitObjectIDs: Bool](./supportedcapabilities/supports64bitobjectids.md)
  A Boolean property that indicates whether the volume supports 64-bit object IDs.
- [var supportsDocumentID: Bool](./supportedcapabilities/supportsdocumentid.md)
  A Boolean property that indicates whether the volume supports document IDs for document revisions.
### Declaring linking capabilities
- [var supportsSymbolicLinks: Bool](./supportedcapabilities/supportssymboliclinks.md)
  A Boolean property that indicates whether the volume supports symbolic links.
- [var supportsHardLinks: Bool](./supportedcapabilities/supportshardlinks.md)
  A Boolean property that indicates whether the volume supports hard links.
### Declaring journaling capabilities
- [var supportsJournal: Bool](./supportedcapabilities/supportsjournal.md)
  A Boolean property that indicates whether the volume supports a journal used to speed recovery in case of unplanned restart, such as a power outage or crash.
- [var supportsActiveJournal: Bool](./supportedcapabilities/supportsactivejournal.md)
  A Boolean property that indicates whether the volume currently uses a journal for speeding recovery after an unplanned shutdown.
### Declaring root capabilites
- [var doesNotSupportRootTimes: Bool](./supportedcapabilities/doesnotsupportroottimes.md)
  A Boolean property that indicates the volume doesn’t store reliable times for the root directory.
### Declaring file capabilities
- [var supportsSparseFiles: Bool](./supportedcapabilities/supportssparsefiles.md)
  A Boolean property that indicates whether the volume supports sparse files.
- [var supportsZeroRuns: Bool](./supportedcapabilities/supportszeroruns.md)
  A Boolean property that indicates whether the volume supports zero runs
- [var supportsFastStatFS: Bool](./supportedcapabilities/supportsfaststatfs.md)
  A Boolean property that indicates whether the volume supports fast results when fetching file system statistics.
- [var supports2TBFiles: Bool](./supportedcapabilities/supports2tbfiles.md)
  A Boolean property that indicates whether the volume supports file sizes larger than 4GB, and potentially up to 2TB.
- [var supportsOpenDenyModes: Bool](./supportedcapabilities/supportsopendenymodes.md)
  A Boolean property that indicates whether the volume supports open deny modes.
- [var supportsHiddenFiles: Bool](./supportedcapabilities/supportshiddenfiles.md)
  A Boolean property that indicates whether the volume supports hidden files.
- [var doesNotSupportImmutableFiles: Bool](./supportedcapabilities/doesnotsupportimmutablefiles.md)
  A Boolean property that indicates the volume doesn’t support immutable files.
- [var doesNotSupportSettingFilePermissions: Bool](./supportedcapabilities/doesnotsupportsettingfilepermissions.md)
  A Boolean property that indicates the volume doesn’t set file permissions.
### Declaring volume capabilities
- [var supportsSharedSpace: Bool](./supportedcapabilities/supportssharedspace.md)
  A Boolean property that indicates whether the volume supports multiple logical file systems that share space in a single “partition.”
- [var supportsVolumeGroups: Bool](./supportedcapabilities/supportsvolumegroups.md)
  A Boolean property that indicates whether the volume supports volume groups.
- [var doesNotSupportVolumeSizes: Bool](./supportedcapabilities/doesnotsupportvolumesizes.md)
  A Boolean property that indicates the volume doesn’t support certain volume size reports.
### Working with case sensitivity
- [var caseFormat: FSVolume.CaseFormat](./supportedcapabilities/caseformat.md)
  A value that indicates the volume’s support for case sensitivity.
- [FSVolume.CaseFormat](./caseformat.md)
  An enumeration of case-sensitivity support types.
### Initializers
- [init?(coder: NSCoder)](./supportedcapabilities/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Inspecting required volume properties
- [var supportedVolumeCapabilities: FSVolume.SupportedCapabilities](./handler/supportedvolumecapabilities.md)
- [var volumeStatistics: FSStatFSResult](./handler/volumestatistics.md)
  A property that provides up-to-date statistics of the volume.
- [class FSStatFSResult](../fsstatfsresult.md)
  A type used to report a volume’s statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities)*