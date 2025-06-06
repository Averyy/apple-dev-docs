# FSVolume.SupportedCapabilities

**Framework**: FSKit  
**Kind**: class

A type that represents capabillities supported by a volume, such as hard and symbolic links, journaling, and large file sizes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class SupportedCapabilities
```

## Topics

### Declaring identifier capabilities
- [var supportsPersistentObjectIDs: Bool](fsvolume/supportedcapabilities/supportspersistentobjectids.md)
  A Boolean property that indicates whether the volume supports persistent object identifiers and can look up file system objects by their IDs.
- [var supports64BitObjectIDs: Bool](fsvolume/supportedcapabilities/supports64bitobjectids.md)
  A Boolean property that indicates whether the volume supports 64-bit object IDs.
- [var supportsDocumentID: Bool](fsvolume/supportedcapabilities/supportsdocumentid.md)
  A Boolean property that indicates whether the volume supports document IDs for document revisions.
### Declaring linking capabilities
- [var supportsSymbolicLinks: Bool](fsvolume/supportedcapabilities/supportssymboliclinks.md)
  A Boolean property that indicates whether the volume supports symbolic links.
- [var supportsHardLinks: Bool](fsvolume/supportedcapabilities/supportshardlinks.md)
  A Boolean property that indicates whether the volume supports hard links.
### Declaring journaling capabilities
- [var supportsJournal: Bool](fsvolume/supportedcapabilities/supportsjournal.md)
  A Boolean property that indicates whether the volume supports a journal used to speed recovery in case of unplanned restart, such as a power outage or crash.
- [var supportsActiveJournal: Bool](fsvolume/supportedcapabilities/supportsactivejournal.md)
  A Boolean property that indicates whether the volume currently uses a journal for speeding recovery after an unplanned shutdown.
### Declaring root capabilites
- [var doesNotSupportRootTimes: Bool](fsvolume/supportedcapabilities/doesnotsupportroottimes.md)
  A Boolan property that indicates the volume doesn’t store reliable times for the root directory.
### Declaring file capabilities
- [var supportsSparseFiles: Bool](fsvolume/supportedcapabilities/supportssparsefiles.md)
  A Boolean property that indicates whether the volume supports sparse files.
- [var supportsZeroRuns: Bool](fsvolume/supportedcapabilities/supportszeroruns.md)
  A Boolean property that indicates whether the volume supports zero runs
- [var supportsFastStatFS: Bool](fsvolume/supportedcapabilities/supportsfaststatfs.md)
  A Boolean property that indicates whether the volume supports fast results when fetching file system statistics.
- [var supports2TBFiles: Bool](fsvolume/supportedcapabilities/supports2tbfiles.md)
  A Boolean property that indicates whether the volume supports file sizes larger than 4GB, and potentially up to 2TB.
- [var supportsOpenDenyModes: Bool](fsvolume/supportedcapabilities/supportsopendenymodes.md)
  A Boolean property that indicates whether the volume supports open deny modes.
- [var supportsHiddenFiles: Bool](fsvolume/supportedcapabilities/supportshiddenfiles.md)
  A Boolean property that indicates whether the volume supports hidden files.
- [var doesNotSupportImmutableFiles: Bool](fsvolume/supportedcapabilities/doesnotsupportimmutablefiles.md)
  A Boolean property that indicates the volume doesn’t support immutable files.
- [var doesNotSupportSettingFilePermissions: Bool](fsvolume/supportedcapabilities/doesnotsupportsettingfilepermissions.md)
  A Boolean property that indicates the volume doesn’t set file permissions.
### Declaring volume capabilities
- [var supportsSharedSpace: Bool](fsvolume/supportedcapabilities/supportssharedspace.md)
  A Boolean property that indicates whether the volume supports multiple logical file systems that share space in a single “partition.”
- [var supportsVolumeGroups: Bool](fsvolume/supportedcapabilities/supportsvolumegroups.md)
  A Boolean property that indicates whether the volume supports volume groups.
- [var doesNotSupportVolumeSizes: Bool](fsvolume/supportedcapabilities/doesnotsupportvolumesizes.md)
  A Boolean property that indicates the volume doesn’t support certain volume size reports.
### Working with case sensitivity
- [var caseFormat: FSVolume.CaseFormat](fsvolume/supportedcapabilities/caseformat.md)
  A value that indicates the volume’s support for case sensitivity.
- [FSVolume.CaseFormat](fsvolume/caseformat.md)
  An enumeration of case-sensitivity support types.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var supportedVolumeCapabilities: FSVolume.SupportedCapabilities](fsvolume/operations/supportedvolumecapabilities.md)
  A property that provides the supported capabilities of the volume.
- [var volumeStatistics: FSStatFSResult](fsvolume/operations/volumestatistics.md)
  A property that provides up-to-date statistics of the volume.
- [class FSStatFSResult](fsstatfsresult.md)
  A type used to report a volume’s statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities)*