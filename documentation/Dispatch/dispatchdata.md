# DispatchData

**Framework**: Dispatch  
**Kind**: struct

An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct DispatchData
```

#### Overview

The memory buffer managed by this object may be a single contiguous block of memory, or it may consist of multiple discontiguous blocks. For the discontiguous case, the dispatch data object makes it appear as if the memory is contiguous.

## Topics

### Creating a Dispatch Data Structure
- [init(bytes: UnsafeRawBufferPointer)](dispatchdata/init(bytes:)-9lrd.md)
  Creates a new dispatch data object from the specified memory buffer.
- [init(bytesNoCopy: UnsafeRawBufferPointer, deallocator: DispatchData.Deallocator)](dispatchdata/init(bytesnocopy:deallocator:)-vfoe.md)
  Creates a new dispatch data object using the specified memory buffer and deallocator.
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](dispatchdata/withunsafebytes(body:).md)
- [DispatchData.Deallocator](dispatchdata/deallocator.md)
  Memory deallocators for dispatch data objects.
- [static let empty: DispatchData](dispatchdata/empty.md)
  A dispatch data object representing a zero-length memory region.
### Appending Data to the Buffer
- [func append(DispatchData)](dispatchdata/append(_:)-3bvdr.md)
- [func append<SourceType>(UnsafeBufferPointer<SourceType>)](dispatchdata/append(_:)-9sgkq.md)
- [func append(UnsafeRawBufferPointer)](dispatchdata/append(_:)-1m94x.md)
### Copying Bytes
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int)](dispatchdata/copybytes(to:count:)-3j0qx.md)
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, from: Range<DispatchData.Index>?) -> Int](dispatchdata/copybytes(to:from:)-7zz4y.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, from: Range<DispatchData.Index>)](dispatchdata/copybytes(to:from:)-60yai.md)
### Accessing Buffer Data
- [subscript(DispatchData.Index) -> UInt8](dispatchdata/subscript(_:).md)
- [func region(location: Int) -> (data: DispatchData, offset: Int)](dispatchdata/region(location:).md)
- [DispatchData.Region](dispatchdata/region.md)
### Iterating Over the Buffer Contents
- [func makeIterator() -> DispatchData.Iterator](dispatchdata/makeiterator.md)
- [func enumerateBytes((UnsafeBufferPointer<UInt8>, Int, inout Bool) -> Void)](dispatchdata/enumeratebytes(_:).md)
### Retrieving Buffer Subsequences
- [func subdata(in: Range<DispatchData.Index>) -> DispatchData](dispatchdata/subdata(in:).md)
### Combining Sequence Elements
- [func append(DispatchData)](dispatchdata/append(_:)-3bvdr.md)
- [func append<SourceType>(UnsafeBufferPointer<SourceType>)](dispatchdata/append(_:)-9sgkq.md)
- [func append(UnsafeRawBufferPointer)](dispatchdata/append(_:)-1m94x.md)
- [func append(UnsafePointer<UInt8>, count: Int)](dispatchdata/append(_:count:).md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](dispatchdata/copybytes(to:count:)-4ffyj.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int)](dispatchdata/copybytes(to:count:)-3j0qx.md)
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, from: Range<DispatchData.Index>?) -> Int](dispatchdata/copybytes(to:from:)-7zz4y.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<DispatchData.Index>)](dispatchdata/copybytes(to:from:)-6ztcb.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, from: Range<DispatchData.Index>)](dispatchdata/copybytes(to:from:)-60yai.md)
- [func enumerateBytes((UnsafeBufferPointer<UInt8>, Int, inout Bool) -> Void)](dispatchdata/enumeratebytes(_:).md)
- [func makeIterator() -> DispatchData.Iterator](dispatchdata/makeiterator.md)
- [func region(location: Int) -> (data: DispatchData, offset: Int)](dispatchdata/region(location:).md)
- [func subdata(in: Range<DispatchData.Index>) -> DispatchData](dispatchdata/subdata(in:).md)
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](dispatchdata/withunsafebytes(body:).md)
### Deprecated
- [init(bytes: UnsafeBufferPointer<UInt8>)](dispatchdata/init(bytes:)-mkbp.md)
  Initialize a data object with copied memory content.
- [init(bytesNoCopy: UnsafeBufferPointer<UInt8>, deallocator: DispatchData.Deallocator)](dispatchdata/init(bytesnocopy:deallocator:)-7h08w.md)
  Initialize a data object without copying the bytes.
- [func append(UnsafePointer<UInt8>, count: Int)](dispatchdata/append(_:count:).md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](dispatchdata/copybytes(to:count:)-4ffyj.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<DispatchData.Index>)](dispatchdata/copybytes(to:from:)-6ztcb.md)
### Instance Methods
- [func enumerateBytes(block: (UnsafeBufferPointer<UInt8>, Int, inout Bool) -> Void)](dispatchdata/enumeratebytes(block:).md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [DataProtocol](../Foundation/DataProtocol.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [class DispatchSource](dispatchsource.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](dispatch-source.md)
  An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [class DispatchIO](dispatchio.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [struct DispatchDataIterator](dispatchdataiterator.md)
  A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch I/O](dispatch-i-o.md)
  An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](dispatch-data.md)
  An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [protocol DispatchSourceProtocol](dispatchsourceprotocol.md)
  Defines a common set of properties and methods that are shared with all dispatch source types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata)*