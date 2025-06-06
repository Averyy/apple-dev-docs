# FSProbeResult

**Framework**: FSKit  
**Kind**: class

An object that represents the results of a specific probe.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSProbeResult
```

#### Overview

For any [`result`](fsproberesult/result.md) value other than [`FSMatchResult.notRecognized`](fsmatchresult/notrecognized.md), ensure the [`name`](fsproberesult/name.md) and [`containerID`](fsproberesult/containerid.md) values are non-`nil`. When a container or volume format doesn’t use a name, return an empty string. Also use an empty string in the case in which the format supports a name, but the value isn’t set yet.

Some container or volume formats may lack a durable UUID on which to base a container identifier. This situation is only valid for unary file systems. In such a case, return a random UUID.

With a block device resource, a probe operation may successfully get a result but encounter an error reading the name or UUID. If this happens, use whatever information is available, and provide an empty string or random UUID for the name or container ID, respectively.

## Topics

### Working with results
- [class func recognized(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/recognized(name:containerid:).md)
  Creates a probe result for a recognized file system.
- [class func usable(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/usable(name:containerid:).md)
  Creates a probe result for a recognized and usable file system.
- [class func usableButLimited(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/usablebutlimited(name:containerid:).md)
  Creates a probe result for a recognized file system that is usable, but with limited capabilities.
- [class var usableButLimited: FSProbeResult](fsproberesult/usablebutlimited.md)
  A probe result for a recognized file system that is usable, but with limited capabilities.
- [class var notRecognized: FSProbeResult](fsproberesult/notrecognized.md)
  A probe result for an unrecognized file system.
### Working with result properties
- [var containerID: FSContainerIdentifier?](fsproberesult/containerid.md)
  The container identifier, as found during the probe operation.
- [var name: String?](fsproberesult/name.md)
  The resource name, as found during the probe operation.
- [var result: FSMatchResult](fsproberesult/result.md)
  The match result, representing the recognition and usability of a probed resource.
- [enum FSMatchResult](fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.

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

- [struct FSBlockmapFlags](fsblockmapflags.md)
  Flags that describe the behavior of a blockmap operation.
- [struct FSCompleteIOFlags](fscompleteioflags.md)
  Flags that describe the behavior of an I/O completion operation.
- [class FSEntityIdentifier](fsentityidentifier.md)
  A base type that identifies containers and volumes.
- [class FSExtentPacker](fsextentpacker.md)
  A type that directs the kernel to map space on disk to a specific file managed by this file system.
- [enum FSExtentType](fsextenttype.md)
  An enumeration of types of extents.
- [enum FSMatchResult](fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsproberesult)*