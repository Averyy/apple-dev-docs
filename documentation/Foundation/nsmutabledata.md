# NSMutableData

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object representing a dynamic byte buffer in memory.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSMutableData
```

```objc
@interface NSMutableData : NSData
```

#### Overview

In Swift, this object bridges to [`Data`](./data.md); use [`NSMutableData`](./nsmutabledata.md) when you need reference semantics or other Foundation-specific behavior.

`NSMutableData` and its superclass `NSData` provide data objects, or object-oriented wrappers for byte buffers. Data objects let simple allocated buffers (that is, data with no embedded pointers) take on the behavior of Foundation objects. They are typically used for data storage and are also useful in Distributed Objects applications, where data contained in data objects can be copied or moved between applications. `NSData` creates static data objects, and `NSMutableData` creates dynamic data objects. You can easily convert one type of data object to the other with the initializer that takes an `NSData` object or an  `NSMutableData` object as an argument.

The following [`NSData`](./nsdata.md) methods change when used on a mutable data object:

- [`init(bytesNoCopy:length:freeWhenDone:)`](./nsdata/init%28bytesnocopy,length,freewhendone%29.md)
- [`init(bytesNoCopy:length:deallocator:)`](./nsdata/init%28bytesnocopy,length,deallocator%29.md)
- [`init(bytesNoCopy:length:)`](./nsdata/init%28bytesnocopy,length%29.md)
- [`dataWithBytesNoCopy:length:freeWhenDone:`](./nsdata/datawithbytesnocopy_length_freewhendone_.md)
- [`dataWithBytesNoCopy:length:`](./nsdata/datawithbytesnocopy_length_.md)

When called, the bytes are immediately copied and then the buffer is freed.

`NSMutableData` is “toll-free bridged” with its Core Foundation counterpart, [`CFData`](../CoreFoundation/cfdata.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`Data`](./data.md) structure, which bridges to the [`NSMutableData`](./nsmutabledata.md) class and its immutable superclass [`NSData`](./nsdata.md). For more information about value types, see [Working with Foundation Types](../Swift/working-with-foundation-types.md).

## Topics

### Creating Mutable Data
- [init?(capacity: Int)](./nsmutabledata/init%28capacity%29.md)
  Returns an initialized mutable data object capable of holding the specified number of bytes.
- [init?(length: Int)](./nsmutabledata/init%28length%29.md)
  Initializes and returns a mutable data object containing a given number of zeroed bytes.
- [+ dataWithCapacity:](./nsmutabledata/datawithcapacity_.md)
  Creates and returns a mutable data object capable of holding the specified number of bytes.
- [+ dataWithLength:](./nsmutabledata/datawithlength_.md)
  Creates and returns an mutable data object containing a given number of zeroed bytes.
### Accessing Raw Bytes
- [var mutableBytes: UnsafeMutableRawPointer](./nsmutabledata/mutablebytes.md)
  A pointer to the data contained by the mutable data object.
### Counting Bytes
- [var length: Int](./nsmutabledata/length.md)
  The number of bytes contained in the mutable data object.
### Adding Bytes
- [func append(UnsafeRawPointer, length: Int)](./nsmutabledata/append%28_,length%29.md)
  Appends to the receiver a given number of bytes from a given buffer.
- [func append(Data)](./nsmutabledata/append%28_%29.md)
  Appends the content of another data object to the receiver.
- [func increaseLength(by: Int)](./nsmutabledata/increaselength%28by%29.md)
  Increases the length of the receiver by a given number of bytes.
### Modifying Bytes
- [func replaceBytes(in: NSRange, withBytes: UnsafeRawPointer)](./nsmutabledata/replacebytes%28in,withbytes%29.md)
  Replaces with a given set of bytes a given range within the contents of the receiver.
- [func replaceBytes(in: NSRange, withBytes: UnsafeRawPointer?, length: Int)](./nsmutabledata/replacebytes%28in,withbytes,length%29.md)
  Replaces with a given set of bytes a given range within the contents of the receiver.
- [func resetBytes(in: NSRange)](./nsmutabledata/resetbytes%28in%29.md)
  Replaces with zeroes the contents of the receiver in a given range.
- [func setData(Data)](./nsmutabledata/setdata%28_%29.md)
  Replaces the entire contents of the receiver with the contents of another data object.
### Compressing and Decompressing Data
- [func compress(using: NSData.CompressionAlgorithm) throws](./nsmutabledata/compress%28using%29.md)
  Compresses the data object’s bytes using an algorithm that you specify.
- [func decompress(using: NSData.CompressionAlgorithm) throws](./nsmutabledata/decompress%28using%29.md)
  Decompresses the data object’s bytes.
- [NSData.CompressionAlgorithm](./nsdata/compressionalgorithm.md)
  An algorithm that indicates how to compress or decompress data.
- [var NSCompressionErrorMaximum: Int](./nscompressionerrormaximum-swift.var.md)
  The end of the range of error codes reserved for compression errors.
- [var NSCompressionErrorMinimum: Int](./nscompressionerrorminimum-swift.var.md)
  The start of the range of error codes reserved for compression errors.
- [var NSCompressionFailedError: Int](./nscompressionfailederror-swift.var.md)
  An error code value that indicates a failure to compress data using the provided algorithm.
- [var NSDecompressionFailedError: Int](./nsdecompressionfailederror-swift.var.md)
  An error code value that indicates a failure to decompress data using the provided algorithm.
- [NSCompressionErrorMaximum](./nscompressionerrormaximum-c.enum.case.md)
  The end of the range of error codes reserved for compression errors.
- [NSCompressionErrorMinimum](./nscompressionerrorminimum-c.enum.case.md)
  The start of the range of error codes reserved for compression errors.
- [NSCompressionFailedError](./nscompressionfailederror-c.enum.case.md)
  An error code value that indicates a failure to compress data using the provided algorithm.
- [NSDecompressionFailedError](./nsdecompressionfailederror-c.enum.case.md)
  An error code value that indicates a failure to decompress data using the provided algorithm.

## Relationships

### Inherits From
- [NSData](./nsdata.md)
### Inherited By
- [NSPurgeableData](./nspurgeabledata.md)
### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [CVarArg](../Swift/cvararg.md)
- [Collection](../Swift/collection.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [DataProtocol](./dataprotocol.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Binary Data
- [NSData](./nsdata.md)
  A static byte buffer in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata)*