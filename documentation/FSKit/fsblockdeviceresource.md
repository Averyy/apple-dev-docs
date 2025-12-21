# FSBlockDeviceResource

**Framework**: FSKit  
**Kind**: class

A resource that represents a block storage disk partition.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSBlockDeviceResource
```

#### Overview

A `FSBlockDeviceResource` can exist in either a proxied or nonproxied version. Only the `fskitd` daemon creates “real” (nonproxied) instances of this class. Client applications and daemons create proxy objects for requests, and `fskitd` opens the underlying device during the processing of the request.

This class wraps a file descriptor for a disk device or partition. Its fundamental identifier is the BSD disk name ([`bsdName`](fsblockdeviceresource/bsdname.md)) for the underlying IOMedia object. However, [`FSBlockDeviceResource`](fsblockdeviceresource.md) doesn’t expose the underlying file descriptor. Instead, it provides accessor methods that can read from and write to the partition, either directly or using the kernel buffer cache.

When you use a `FSBlockDeviceResource`, your file system implementation also conforms to a maintenance operation protocol. These protocols add support for checking, repairing, and optionally formatting file systems. The system doesn’t mount block device file systems until they pass a file system check. For an [`FSUnaryFileSystem`](fsunaryfilesystem.md) that uses `FSBlockDeviceResource`, conform to `FSManageableResourceMaintenanceOperations`.

## Topics

### Accessing resource properties
- [var bsdName: String](fsblockdeviceresource/bsdname.md)
  The device name of the resource.
- [var isWritable: Bool](fsblockdeviceresource/iswritable.md)
  A Boolean property that indicates whether the resource can write data to the device.
- [var blockCount: UInt64](fsblockdeviceresource/blockcount.md)
  The block count on this resource.
- [var blockSize: UInt64](fsblockdeviceresource/blocksize.md)
  The logical block size, the size of data blocks used by the file system.
- [var physicalBlockSize: UInt64](fsblockdeviceresource/physicalblocksize.md)
  The sector size of the device.
### Reading and writing data
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws -> Int](fsblockdeviceresource/read(into:startingat:length:)-4ax6s.md)
  Synchronously reads data from the resource into a buffer.
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](fsblockdeviceresource/read(into:startingat:length:)-5yozi.md)
  Asychronously reads data from the resource into a buffer.
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int, completionHandler: (Int, (any Error)?) -> Void)](fsblockdeviceresource/read(into:startingat:length:completionhandler:).md)
  Reads data from the resource into a buffer and executes a closure afterwards.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws -> Int](fsblockdeviceresource/write(from:startingat:length:)-2fmgt.md)
  Synchronously writes data from from a buffer to the resource and executes a block afterwards.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](fsblockdeviceresource/write(from:startingat:length:)-9oa1x.md)
  Asynchronously writes data from from a buffer to the resource.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int, completionHandler: (Int, (any Error)?) -> Void)](fsblockdeviceresource/write(from:startingat:length:completionhandler:).md)
  Writes data from from a buffer to the resource and executes a closure afterwards.
### Reading and writing data with kernel buffer cache
- [func metadataRead(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws](fsblockdeviceresource/metadataread(into:startingat:length:).md)
  Synchronously reads file system metadata from the resource into a buffer.
- [func metadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](fsblockdeviceresource/metadatawrite(from:startingat:length:).md)
  Synchronously writes file system metadata from a buffer to the resource.
- [func delayedMetadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](fsblockdeviceresource/delayedmetadatawrite(from:startingat:length:).md)
  Writes file system metadata from a buffer to a cache, prior to flushing it to the resource.
- [func metadataFlush() throws](fsblockdeviceresource/metadataflush.md)
  Synchronously flushes the resource’s buffer cache.
- [func asynchronousMetadataFlush() throws](fsblockdeviceresource/asynchronousmetadataflush.md)
  Asynchronously flushes the resource’s buffer cache.
- [func metadataClear([FSMetadataRange], withDelayedWrites: Bool) throws](fsblockdeviceresource/metadataclear(_:withdelayedwrites:).md)
  Clears the given ranges within the buffer cache.
- [func metadataPurge([FSMetadataRange]) throws](fsblockdeviceresource/metadatapurge(_:).md)
  Synchronously purges the given ranges from the buffer cache.
- [class FSMetadataRange](fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.

## Relationships

### Inherits From
- [FSResource](fsresource.md)
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

- [class FSResource](fsresource.md)
  An abstract resource a file system uses to provide data for a volume.
- [class FSPathURLResource](fspathurlresource.md)
  A resource that represents a path in the system file space.
- [class FSGenericURLResource](fsgenericurlresource.md)
  A resource that represents an abstract URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource)*