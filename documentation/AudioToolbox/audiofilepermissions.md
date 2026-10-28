# AudioFilePermissions

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

Flags for use when opening an audio file.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum AudioFilePermissions
```

```c
enum AudioFilePermissions : SInt8;
```

## Overview

Use these flags with the [`AudioFileOpenURL(_:_:_:_:)`](./audiofileopenurl%28_,_,_,_%29.md) and [`AudioFileOpen`](./audiofileopen.md) functions.

## Topics

### Constants
- [AudioFilePermissions.readPermission](./audiofilepermissions/readpermission.md)
  File is read-only.
- [AudioFilePermissions.readWritePermission](./audiofilepermissions/readwritepermission.md)
  File has read-write permission.
- [AudioFilePermissions.writePermission](./audiofilepermissions/writepermission.md)
  File is write-only.
### Initializers
- [init?(rawValue: Int8)](./audiofilepermissions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [struct AudioBytePacketTranslationFlags](./audiobytepackettranslationflags.md)
- [struct AudioFileFlags](./audiofileflags.md)
- [struct AudioFileRegionFlags](./audiofileregionflags.md)
  Flags that specify a playback direction for an audio file region structure.
- [struct AudioFileStreamParseFlags](./audiofilestreamparseflags.md)
- [struct AudioFileStreamPropertyFlags](./audiofilestreampropertyflags.md)
- [struct AudioFileStreamSeekFlags](./audiofilestreamseekflags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions)*