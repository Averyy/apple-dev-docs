# kCFURLVolumeSupportsVolumeSizesKey

**Framework**: Core Foundation  
**Kind**: var

Key for determining whether the volume supports returning volume size information, returned as a `CFBoolean` object. If `true`, volume size information is available as values of the [`kCFURLVolumeTotalCapacityKey`](kcfurlvolumetotalcapacitykey.md) and [`kCFURLVolumeAvailableCapacityKey`](kcfurlvolumeavailablecapacitykey.md) keys.

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
let kCFURLVolumeSupportsVolumeSizesKey: CFString!
```

## See Also

- [let kCFURLVolumeNameKey: CFString!](kcfurlvolumenamekey.md)
  The name of the volume, returned as a `CFString` object.
- [let kCFURLVolumeLocalizedNameKey: CFString!](kcfurlvolumelocalizednamekey.md)
  The user-presentable name of the volume, returned as a `CFString` object.
- [let kCFURLVolumeLocalizedFormatDescriptionKey: CFString!](kcfurlvolumelocalizedformatdescriptionkey.md)
  Key for the volume’s descriptive format name, returned as a `CFString` object.
- [let kCFURLVolumeTotalCapacityKey: CFString!](kcfurlvolumetotalcapacitykey.md)
  Key for the volume’s capacity in bytes, returned as a `CFNumber` object.
- [let kCFURLVolumeAvailableCapacityKey: CFString!](kcfurlvolumeavailablecapacitykey.md)
  Key for the volume’s available capacity in bytes, returned as a `CFNumber` object.
- [let kCFURLVolumeResourceCountKey: CFString!](kcfurlvolumeresourcecountkey.md)
  Key for the total number of resources on the volume, returned as a `CFNumber` object.
- [let kCFURLVolumeSupportsPersistentIDsKey: CFString!](kcfurlvolumesupportspersistentidskey.md)
  Key for determining whether the volume supports persistent IDs, returned as a `CFBoolean` object.
- [let kCFURLVolumeSupportsSymbolicLinksKey: CFString!](kcfurlvolumesupportssymboliclinkskey.md)
  Key for determining whether the volume supports symbolic links, returned as a `CFBoolean` object.
- [let kCFURLVolumeSupportsHardLinksKey: CFString!](kcfurlvolumesupportshardlinkskey.md)
  Key for determining whether the volume supports hard links, returned as a `CFBoolean` object.
- [let kCFURLVolumeSupportsJournalingKey: CFString!](kcfurlvolumesupportsjournalingkey.md)
  Key for determining whether the volume supports journaling, returned as a `CFBoolean` object.
- [let kCFURLVolumeIsJournalingKey: CFString!](kcfurlvolumeisjournalingkey.md)
  Key for determining whether the volume is currently journaling, returned as a `CFBoolean` object.
- [let kCFURLVolumeSupportsSparseFilesKey: CFString!](kcfurlvolumesupportssparsefileskey.md)
  Key for determining whether the volume supports sparse files, returned as a `CFBoolean` object.
- [let kCFURLVolumeSupportsZeroRunsKey: CFString!](kcfurlvolumesupportszerorunskey.md)
  Key for determining whether the volume supports zero runs, returned as a `CFBoolean` object.
- [let kCFURLVolumeSupportsCaseSensitiveNamesKey: CFString!](kcfurlvolumesupportscasesensitivenameskey.md)
  Key for determining whether the volume supports case-sensitive names, returned as a `CFBoolean` object.
- [let kCFURLVolumeSupportsCasePreservedNamesKey: CFString!](kcfurlvolumesupportscasepreservednameskey.md)
  Key for determining whether the volume supports case-preserved names, returned as a `CFBoolean` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfurlvolumesupportsvolumesizeskey)*