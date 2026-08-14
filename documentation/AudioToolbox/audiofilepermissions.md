# AudioFilePermissions

**Framework**: Audio Toolbox  
**Kind**: enum

Flags for use when opening an audio file.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum AudioFilePermissions
```

#### Overview

Use these flags with the [`AudioFileOpenURL(_:_:_:_:)`](audiofileopenurl(_:_:_:_:).md) and [`AudioFileOpen`](audiofileopen.md) functions.

## Topics

### Constants
- [AudioFilePermissions.readPermission](audiofilepermissions/readpermission.md)
  File is read-only.
- [AudioFilePermissions.readWritePermission](audiofilepermissions/readwritepermission.md)
  File has read-write permission.
- [AudioFilePermissions.writePermission](audiofilepermissions/writepermission.md)
  File is write-only.
### Initializers
- [init?(rawValue: Int8)](audiofilepermissions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AudioBytePacketTranslationFlags](audiobytepackettranslationflags.md)
- [struct AudioFileFlags](audiofileflags.md)
- [struct AudioFileRegionFlags](audiofileregionflags.md)
  Flags that specify a playback direction for an audio file region structure.
- [struct AudioFileStreamParseFlags](audiofilestreamparseflags.md)
- [struct AudioFileStreamPropertyFlags](audiofilestreampropertyflags.md)
- [struct AudioFileStreamSeekFlags](audiofilestreamseekflags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions)*