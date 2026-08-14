# FSVolume.Identifier

**Framework**: FSKit  
**Kind**: class

A type that identifies a volume.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class Identifier
```

#### Overview

For most volumes, the volume identifier is the UUID identifying the volume.

Network file systems may access the same underlying volume using different authentication credentials. To handle this situation, add qualifying data to identify the specific container, as discussed in the superclass, [`FSEntityIdentifier`](fsentityidentifier.md).

> ❗ **Important**: Don’t subclass this class.

## Relationships

### Inherits From
- [FSEntityIdentifier](fsentityidentifier.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(volumeID: FSVolume.Identifier, volumeName: FSFileName)](fsvolume/init(volumeid:volumename:).md)
  Creates a volume with the given identifier and name.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/identifier)*