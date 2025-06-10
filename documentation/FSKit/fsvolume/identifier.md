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
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(volumeID: FSVolume.Identifier, volumeName: FSFileName)](fsvolume/init(volumeid:volumename:).md)
  Creates a volume with the given identifier and name.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/identifier)*