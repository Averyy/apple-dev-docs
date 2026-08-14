# FSEntityIdentifier

**Framework**: FSKit  
**Kind**: class

A base type that identifies containers and volumes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSEntityIdentifier
```

#### Overview

An [`FSEntityIdentifier`](fsentityidentifier.md) is a UUID to identify a container or volume, optionally with eight bytes of qualifying (differentiating) data. You use the qualifiers in cases in which a file server can receive multiple connections from the same client, which differ by user credentials. In this case, the identifier for each client is the server’s base UUID, and a unique qualifier that differs by client.

> ❗ **Important**: Don’t subclass this class.

## Topics

### Creating an entity identifier
- [init()](fsentityidentifier/init.md)
  Creates an entity identifier with a random UUID.
- [init(uuid: UUID)](fsentityidentifier/init(uuid:)-9e20k.md)
  Creates an entity identifier with the given UUID.
- [init(uuid: UUID, data: Data)](fsentityidentifier/init(uuid:data:)-8dixs.md)
  Creates an entity identifier with the given UUID and qualifier data.
- [init(uuid: UUID, qualifier: UInt64)](fsentityidentifier/init(uuid:qualifier:)-9ty70.md)
  Creates an entity identifier with the given UUID and qualifier data as a 64-bit unsigned integer.
### Inspecting identifier properties
- [var uuid: UUID](fsentityidentifier/uuid.md)
  A UUID to uniquely identify this entity.
- [var qualifier: Data?](fsentityidentifier/qualifier.md)
  An optional piece of data to distinguish entities that otherwise share the same UUID.
### Initializers
- [init(UUID: UUID)](fsentityidentifier/init(uuid:)-1cibs.md)
- [init(UUID: UUID, data: Data)](fsentityidentifier/init(uuid:data:)-1cpve.md)
- [init(UUID: UUID, qualifier: UInt64)](fsentityidentifier/init(uuid:qualifier:)-x26c.md)
- [init?(UUID: UUID, qualifierData: Data)](fsentityidentifier/init(uuid:qualifierdata:)-49874.md)
- [init?(coder: NSCoder)](fsentityidentifier/init(coder:).md)
- [init?(uuid: UUID, qualifierData: Data)](fsentityidentifier/init(uuid:qualifierdata:)-8xlg1.md)
  Creates an entity identifier with the given UUID and qualifier data.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [FSContainerIdentifier](fscontaineridentifier.md)
- [FSVolume.Identifier](fsvolume/identifier.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSExtentPacker](fsextentpacker.md)
  A type that directs the kernel to map space on disk to a specific file managed by this file system.
- [enum FSExtentType](fsextenttype.md)
  An enumeration of types of extents.
- [enum FSMatchResult](fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.
- [class FSProbeResult](fsproberesult.md)
  An object that represents the results of a specific probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsentityidentifier)*