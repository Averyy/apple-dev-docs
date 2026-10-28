# FSBlockDeviceResource

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A resource that represents a block storage disk partition.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSBlockDeviceResource
```

```objc
@interface FSBlockDeviceResource : FSResource
```

## Overview

A `FSBlockDeviceResource` can exist in either a proxied or nonproxied version. Only the `fskitd` daemon creates “real” (nonproxied) instances of this class. Client applications and daemons create proxy objects for requests, and `fskitd` opens the underlying device during the processing of the request.

This class wraps a file descriptor for a disk device or partition. Its fundamental identifier is the BSD disk name ([`bsdName`](./fsblockdeviceresource/bsdname.md)) for the underlying IOMedia object. However, [`FSBlockDeviceResource`](./fsblockdeviceresource.md) doesn’t expose the underlying file descriptor. Instead, it provides accessor methods that can read from and write to the partition, either directly or using the kernel buffer cache.

When you use a `FSBlockDeviceResource`, your file system implementation also conforms to a maintenance operation protocol. These protocols add support for checking, repairing, and optionally formatting file systems. The system doesn’t mount block device file systems until they pass a file system check. For an [`FSUnaryFileSystem`](./fsunaryfilesystem.md) that uses `FSBlockDeviceResource`, conform to `FSManageableResourceMaintenanceOperations`.

> ❗ **Important**: Don’t mix direct I/O operations (`read(into:startingAt:length:)` and `write(from:startingAt:length:)`) with metadata operations ([`metadataRead(into:startingAt:length:)`](./fsblockdeviceresource/metadataread%28into,startingat,length%29.md), [`metadataWrite(from:startingAt:length:)`](./fsblockdeviceresource/metadatawrite%28from,startingat,length%29.md), and [`delayedMetadataWrite(from:startingAt:length:)`](./fsblockdeviceresource/delayedmetadatawrite%28from,startingat,length%29.md)) on the same range. Direct I/O bypasses the buffer cache, so mixing the two may result in stale or inconsistent data.

## Topics

### Accessing resource properties
- [var bsdName: String](./fsblockdeviceresource/bsdname.md)
  The device name of the resource.
- [var isWritable: Bool](./fsblockdeviceresource/iswritable.md)
  A Boolean property that indicates whether the resource can write data to the device.
- [var blockCount: UInt64](./fsblockdeviceresource/blockcount.md)
  The block count on this resource.
- [var blockSize: UInt64](./fsblockdeviceresource/blocksize.md)
  The logical block size, the size of data blocks used by the file system.
- [var physicalBlockSize: UInt64](./fsblockdeviceresource/physicalblocksize.md)
  The sector size of the device.
### Reading and writing data
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws -> Int](./fsblockdeviceresource/read%28into,startingat,length%29-4ax6s.md)
  Synchronously reads data from the resource into a buffer.
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](./fsblockdeviceresource/read%28into,startingat,length%29-5yozi.md)
  Asychronously reads data from the resource into a buffer.
- [func read(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int, completionHandler: (Int, (any Error)?) -> Void)](./fsblockdeviceresource/read%28into,startingat,length,completionhandler%29.md)
  Reads data from the resource into a buffer and executes a closure afterwards.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws -> Int](./fsblockdeviceresource/write%28from,startingat,length%29-2fmgt.md)
  Synchronously writes data from from a buffer to the resource and executes a block afterwards.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) async throws -> Int](./fsblockdeviceresource/write%28from,startingat,length%29-9oa1x.md)
  Asynchronously writes data from from a buffer to the resource.
- [func write(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int, completionHandler: (Int, (any Error)?) -> Void)](./fsblockdeviceresource/write%28from,startingat,length,completionhandler%29.md)
  Writes data from from a buffer to the resource and executes a closure afterwards.
- [- readInto:startingAt:length:error:](./fsblockdeviceresource/readinto_startingat_length_error_.md)
  Synchronously reads data from the resource into a buffer.
- [- readInto:startingAt:length:completionHandler:](./fsblockdeviceresource/readinto_startingat_length_completionhandler_.md)
  Reads data from the resource into a buffer and executes a block afterwards.
- [- writeFrom:startingAt:length:error:](./fsblockdeviceresource/writefrom_startingat_length_error_.md)
  Synchronously writes data from from a buffer to the resource and executes a block afterwards.
- [- writeFrom:startingAt:length:completionHandler:](./fsblockdeviceresource/writefrom_startingat_length_completionhandler_.md)
  Writes data from from a buffer to the resource and executes a block afterwards.
### Reading and writing data with kernel buffer cache
- [func metadataRead(into: UnsafeMutableRawBufferPointer, startingAt: off_t, length: Int) throws](./fsblockdeviceresource/metadataread%28into,startingat,length%29.md)
  Synchronously reads file system metadata from the resource into a buffer.
- [func metadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](./fsblockdeviceresource/metadatawrite%28from,startingat,length%29.md)
  Synchronously writes file system metadata from a buffer to the resource.
- [func delayedMetadataWrite(from: UnsafeRawBufferPointer, startingAt: off_t, length: Int) throws](./fsblockdeviceresource/delayedmetadatawrite%28from,startingat,length%29.md)
  Writes file system metadata from a buffer to a cache, prior to flushing it to the resource.
- [func metadataFlush() throws](./fsblockdeviceresource/metadataflush%28%29.md)
  Synchronously flushes the resource’s buffer cache.
- [func asynchronousMetadataFlush() throws](./fsblockdeviceresource/asynchronousmetadataflush%28%29.md)
  Asynchronously flushes the resource’s buffer cache.
- [func metadataClear([FSMetadataRange], withDelayedWrites: Bool) throws](./fsblockdeviceresource/metadataclear%28_,withdelayedwrites%29.md)
  Clears the given ranges within the buffer cache.
- [func metadataPurge([FSMetadataRange]) throws](./fsblockdeviceresource/metadatapurge%28_%29.md)
  Synchronously purges the given ranges from the buffer cache.
- [class FSMetadataRange](./fsmetadatarange.md)
  A range that describes contiguous metadata segments on disk.
- [- metadataReadInto:startingAt:length:error:](./fsblockdeviceresource/metadatareadinto_startingat_length_error_.md)
  Synchronously reads file system metadata from the resource into a buffer.
- [- metadataWriteFrom:startingAt:length:error:](./fsblockdeviceresource/metadatawritefrom_startingat_length_error_.md)
  Synchronously writes file system metadata from a buffer to the resource.
- [- delayedMetadataWriteFrom:startingAt:length:error:](./fsblockdeviceresource/delayedmetadatawritefrom_startingat_length_error_.md)
  Writes file system metadata from a buffer to a cache, prior to flushing it to the resource.

## Relationships

### Inherits From
- [FSResource](./fsresource.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Resources
- [class FSResource](./fsresource.md)
  An abstract resource a file system uses to provide data for a volume.
- [class FSPathURLResource](./fspathurlresource.md)
  A resource that represents a path in the system file space.
- [class FSGenericURLResource](./fsgenericurlresource.md)
  A resource that represents an abstract URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource)*