# CMReadOnlyDataBlockBuffer

**Framework**: Core Media  
**Kind**: struct

A block buffer that provides read-only access to the a range of bytes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct CMReadOnlyDataBlockBuffer
```

#### Overview

Block buffer provides a contiguous range of data offsets (from 0 to [`count`](cmreadonlydatablockbuffer/count.md)) across a possibly non-contiguous range of bytes. The byte range may contain memory blocks and buffer references. The bytes held by this buffer can not be modified. However, the composition of the byte range can be changed by appending other memory blocks or buffer references.

## Topics

### Structures
- [CMReadOnlyDataBlockBuffer.BlockRegion](cmreadonlydatablockbuffer/blockregion.md)
  A contiguous region of memory within a block buffer.
### Operators
- [static func + (CMReadOnlyDataBlockBuffer, CMReadOnlyDataBlockBuffer) -> CMReadOnlyDataBlockBuffer](cmreadonlydatablockbuffer/+(_:_:)-58lg4.md)
  Creates a new block buffer by concatenating two block buffers.
- [static func + (CMReadOnlyDataBlockBuffer, consuming CMMutableDataBlockBuffer) -> CMReadOnlyDataBlockBuffer](cmreadonlydatablockbuffer/+(_:_:)-92jke.md)
  Creates a new block buffer by concatenating two block buffers.
- [static func += (inout CMReadOnlyDataBlockBuffer, CMReadOnlyDataBlockBuffer)](cmreadonlydatablockbuffer/+=(_:_:)-67kx8.md)
  Appends the bytes of another block buffer without copying.
- [static func += (inout CMReadOnlyDataBlockBuffer, consuming CMMutableDataBlockBuffer)](cmreadonlydatablockbuffer/+=(_:_:)-7fm8e.md)
  Appends the bytes of another block buffer without copying.
### Initializers
- [init(consuming CMMutableDataBlockBuffer)](cmreadonlydatablockbuffer/init(_:)-5fdm2.md)
  Create a readonly block buffer from existing block buffer.
- [init(DispatchData)](cmreadonlydatablockbuffer/init(_:)-80jym.md)
  Create a new block buffer referencing bytes from DispatchData. DispatchData objects consisting of multiple regions will produce a non-contiguous block buffer with each dispatch data region corresponding to a region in the block buffer.
- [init(Data)](cmreadonlydatablockbuffer/init(_:)-w7h3.md)
  Create a new block buffer referencing bytes from Data.
- [init(subBlockCapacity: Int)](cmreadonlydatablockbuffer/init(subblockcapacity:).md)
  Create empty block buffer.
- [init(unsafeBlockBuffer: sending CMBlockBuffer)](cmreadonlydatablockbuffer/init(unsafeblockbuffer:).md)
  Create a readonly block buffer from an existing block buffer.
### Instance Properties
- [var isContiguous: Bool](cmreadonlydatablockbuffer/iscontiguous.md)
  Determine whether the block buffer is contiguous.
### Instance Methods
- [func append(referenceOf: CMReadOnlyDataBlockBuffer, optimizeDepth: Bool)](cmreadonlydatablockbuffer/append(referenceof:optimizedepth:)-2x1ta.md)
  Append a reference to a range of another block buffer.
- [func append(referenceOf: consuming CMMutableDataBlockBuffer, optimizeDepth: Bool)](cmreadonlydatablockbuffer/append(referenceof:optimizedepth:)-5g65c.md)
  Append a reference to a range of another block buffer.
- [func withContiguousStorageIfAvailable<R>((UnsafeRawBufferPointer) throws -> sending R) rethrows -> sending R?](cmreadonlydatablockbuffer/withcontiguousstorageifavailable(_:)-7tacg.md)
  Access contents of the buffer if available as contiguous memory block.
- [func withUnsafeBlockBuffer<R>((CMBlockBuffer) throws -> sending R) rethrows -> sending R](cmreadonlydatablockbuffer/withunsafeblockbuffer(_:).md)
  Access the underlying CMBlockBuffer instance.
### Default Implementations
- [Collection Implementations](cmreadonlydatablockbuffer/collection-implementations.md)
- [DataProtocol Implementations](cmreadonlydatablockbuffer/dataprotocol-implementations.md)
- [RandomAccessCollection Implementations](cmreadonlydatablockbuffer/randomaccesscollection-implementations.md)
- [Sequence Implementations](cmreadonlydatablockbuffer/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [CMSampleBuffer.Content](cmsamplebuffer/content.md)
- [CMSampleBuffer.ContentWithFormatDescription](cmsamplebuffer/contentwithformatdescription.md)
- [CMSampleBuffer.MultiSampleContent](cmsamplebuffer/multisamplecontent.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [DataProtocol](../Foundation/DataProtocol.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer)*