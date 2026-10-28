# FSVolume.Identifier

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A type that identifies a volume.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class Identifier
```

```objc
@interface FSVolumeIdentifier : FSEntityIdentifier
```

## Overview

For most volumes, the volume identifier is the UUID identifying the volume.

Network file systems may access the same underlying volume using different authentication credentials. To handle this situation, add qualifying data to identify the specific container, as discussed in the superclass, [`FSEntityIdentifier`](../fsentityidentifier.md).

> ❗ **Important**: Don’t subclass this class.

## Relationships

### Inherits From
- [FSEntityIdentifier](../fsentityidentifier.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a volume
- [init(volumeID: FSVolume.Identifier, volumeName: FSFileName)](./init%28volumeid,volumename%29.md)
  Creates a volume with the given identifier and name.
- [class FSFileName](../fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/identifier)*