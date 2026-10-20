# DispatchData

**Framework**: Dispatch  
**Kind**: struct  
**Role**: Structure

An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct DispatchData
```

#### Overview

The memory buffer managed by this object may be a single contiguous block of memory, or it may consist of multiple discontiguous blocks. For the discontiguous case, the dispatch data object makes it appear as if the memory is contiguous.

## Topics

### Creating a Dispatch Data Structure
- [init(bytes: UnsafeRawBufferPointer)](./dispatchdata/init%28bytes%29-9lrd.md)
  Creates a new dispatch data object from the specified memory buffer.
- [init(bytesNoCopy: UnsafeRawBufferPointer, deallocator: DispatchData.Deallocator)](./dispatchdata/init%28bytesnocopy,deallocator%29-vfoe.md)
  Creates a new dispatch data object using the specified memory buffer and deallocator.
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](./dispatchdata/withunsafebytes%28body%29.md)
- [DispatchData.Deallocator](./dispatchdata/deallocator.md)
  Memory deallocators for dispatch data objects.
- [static let empty: DispatchData](./dispatchdata/empty.md)
  A dispatch data object representing a zero-length memory region.
### Appending Data to the Buffer
- [func append(DispatchData)](./dispatchdata/append%28_%29-3bvdr.md)
- [func append<SourceType>(UnsafeBufferPointer<SourceType>)](./dispatchdata/append%28_%29-9sgkq.md)
- [func append(UnsafeRawBufferPointer)](./dispatchdata/append%28_%29-1m94x.md)
### Copying Bytes
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int)](./dispatchdata/copybytes%28to,count%29-3j0qx.md)
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, from: Range<DispatchData.Index>?) -> Int](./dispatchdata/copybytes%28to,from%29-7zz4y.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, from: Range<DispatchData.Index>)](./dispatchdata/copybytes%28to,from%29-60yai.md)
### Accessing Buffer Data
- [subscript(DispatchData.Index) -> UInt8](./dispatchdata/subscript%28_%29.md)
- [func region(location: Int) -> (data: DispatchData, offset: Int)](./dispatchdata/region%28location%29.md)
- [DispatchData.Region](./dispatchdata/region.md)
### Iterating Over the Buffer Contents
- [func makeIterator() -> DispatchData.Iterator](./dispatchdata/makeiterator%28%29.md)
- [func enumerateBytes((UnsafeBufferPointer<UInt8>, Int, inout Bool) -> Void)](./dispatchdata/enumeratebytes%28_%29.md)
### Retrieving Buffer Subsequences
- [func subdata(in: Range<DispatchData.Index>) -> DispatchData](./dispatchdata/subdata%28in%29.md)
### Combining Sequence Elements
- [func append(DispatchData)](./dispatchdata/append%28_%29-3bvdr.md)
- [func append<SourceType>(UnsafeBufferPointer<SourceType>)](./dispatchdata/append%28_%29-9sgkq.md)
- [func append(UnsafeRawBufferPointer)](./dispatchdata/append%28_%29-1m94x.md)
- [func append(UnsafePointer<UInt8>, count: Int)](./dispatchdata/append%28_,count%29.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](./dispatchdata/copybytes%28to,count%29-4ffyj.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int)](./dispatchdata/copybytes%28to,count%29-3j0qx.md)
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, from: Range<DispatchData.Index>?) -> Int](./dispatchdata/copybytes%28to,from%29-7zz4y.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<DispatchData.Index>)](./dispatchdata/copybytes%28to,from%29-6ztcb.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, from: Range<DispatchData.Index>)](./dispatchdata/copybytes%28to,from%29-60yai.md)
- [func enumerateBytes((UnsafeBufferPointer<UInt8>, Int, inout Bool) -> Void)](./dispatchdata/enumeratebytes%28_%29.md)
- [func makeIterator() -> DispatchData.Iterator](./dispatchdata/makeiterator%28%29.md)
- [func region(location: Int) -> (data: DispatchData, offset: Int)](./dispatchdata/region%28location%29.md)
- [func subdata(in: Range<DispatchData.Index>) -> DispatchData](./dispatchdata/subdata%28in%29.md)
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](./dispatchdata/withunsafebytes%28body%29.md)
### Deprecated
- [init(bytes: UnsafeBufferPointer<UInt8>)](./dispatchdata/init%28bytes%29-mkbp.md)
  Initialize a data object with copied memory content.
- [init(bytesNoCopy: UnsafeBufferPointer<UInt8>, deallocator: DispatchData.Deallocator)](./dispatchdata/init%28bytesnocopy,deallocator%29-7h08w.md)
  Initialize a data object without copying the bytes.
- [func append(UnsafePointer<UInt8>, count: Int)](./dispatchdata/append%28_,count%29.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](./dispatchdata/copybytes%28to,count%29-4ffyj.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<DispatchData.Index>)](./dispatchdata/copybytes%28to,from%29-6ztcb.md)
### Instance Methods
- [func enumerateBytes(block: (UnsafeBufferPointer<UInt8>, Int, inout Bool) -> Void)](./dispatchdata/enumeratebytes%28block%29.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [DataProtocol](../Foundation/dataprotocol.md)
- [Escapable](../Swift/escapable.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### System Event Monitoring
- [class DispatchSource](./dispatchsource.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](./dispatch-source.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [class DispatchIO](./dispatchio.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [struct DispatchDataIterator](./dispatchdataiterator.md)
  A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch I/O](./dispatch-i-o.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](./dispatch-data.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [protocol DispatchSourceProtocol](./dispatchsourceprotocol.md)
  Defines a common set of properties and methods that are shared with all dispatch source types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata)*