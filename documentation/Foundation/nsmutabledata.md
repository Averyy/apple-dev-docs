# NSMutableData

**Framework**: Foundation  
**Kind**: class

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

#### Overview

In Swift, this object bridges to [`Data`](data.md); use [`NSMutableData`](nsmutabledata.md) when you need reference semantics or other Foundation-specific behavior.

`NSMutableData` and its superclass `NSData` provide data objects, or object-oriented wrappers for byte buffers. Data objects let simple allocated buffers (that is, data with no embedded pointers) take on the behavior of Foundation objects. They are typically used for data storage and are also useful in Distributed Objects applications, where data contained in data objects can be copied or moved between applications. `NSData` creates static data objects, and `NSMutableData` creates dynamic data objects. You can easily convert one type of data object to the other with the initializer that takes an `NSData` object or an  `NSMutableData` object as an argument.

The following [`NSData`](nsdata.md) methods change when used on a mutable data object:

- [`init(bytesNoCopy:length:freeWhenDone:)`](nsdata/init(bytesnocopy:length:freewhendone:).md)
- [`init(bytesNoCopy:length:deallocator:)`](nsdata/init(bytesnocopy:length:deallocator:).md)
- [`init(bytesNoCopy:length:)`](nsdata/init(bytesnocopy:length:).md)
- [`dataWithBytesNoCopy:length:freeWhenDone:`](nsdata/datawithbytesnocopy:length:freewhendone:.md)
- [`dataWithBytesNoCopy:length:`](nsdata/datawithbytesnocopy:length:.md)

When called, the bytes are immediately copied and then the buffer is freed.

`NSMutableData` is “toll-free bridged” with its Core Foundation counterpart, [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`Data`](data.md) structure, which bridges to the [`NSMutableData`](nsmutabledata.md) class and its immutable superclass [`NSData`](nsdata.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

 The Swift overlay to the Foundation framework provides the [`Data`](data.md) structure, which bridges to the [`NSMutableData`](nsmutabledata.md) class and its immutable superclass [`NSData`](nsdata.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Creating Mutable Data
- [init?(capacity: Int)](nsmutabledata/init(capacity:).md)
  Returns an initialized mutable data object capable of holding the specified number of bytes.
- [init?(length: Int)](nsmutabledata/init(length:).md)
  Initializes and returns a mutable data object containing a given number of zeroed bytes.
### Accessing Raw Bytes
- [var mutableBytes: UnsafeMutableRawPointer](nsmutabledata/mutablebytes.md)
  A pointer to the data contained by the mutable data object.
### Counting Bytes
- [var length: Int](nsmutabledata/length.md)
  The number of bytes contained in the mutable data object.
### Adding Bytes
- [func append(UnsafeRawPointer, length: Int)](nsmutabledata/append(_:length:).md)
  Appends to the receiver a given number of bytes from a given buffer.
- [func append(Data)](nsmutabledata/append(_:).md)
  Appends the content of another data object to the receiver.
- [func increaseLength(by: Int)](nsmutabledata/increaselength(by:).md)
  Increases the length of the receiver by a given number of bytes.
### Modifying Bytes
- [func replaceBytes(in: NSRange, withBytes: UnsafeRawPointer)](nsmutabledata/replacebytes(in:withbytes:).md)
  Replaces with a given set of bytes a given range within the contents of the receiver.
- [func replaceBytes(in: NSRange, withBytes: UnsafeRawPointer?, length: Int)](nsmutabledata/replacebytes(in:withbytes:length:).md)
  Replaces with a given set of bytes a given range within the contents of the receiver.
- [func resetBytes(in: NSRange)](nsmutabledata/resetbytes(in:).md)
  Replaces with zeroes the contents of the receiver in a given range.
- [func setData(Data)](nsmutabledata/setdata(_:).md)
  Replaces the entire contents of the receiver with the contents of another data object.
### Compressing and Decompressing Data
- [func compress(using: NSData.CompressionAlgorithm) throws](nsmutabledata/compress(using:).md)
  Compresses the data object’s bytes using an algorithm that you specify.
- [func decompress(using: NSData.CompressionAlgorithm) throws](nsmutabledata/decompress(using:).md)
  Decompresses the data object’s bytes.
- [NSData.CompressionAlgorithm](nsdata/compressionalgorithm.md)
  An algorithm that indicates how to compress or decompress data.
- [var NSCompressionErrorMaximum: Int](nscompressionerrormaximum-swift.var.md)
  The end of the range of error codes reserved for compression errors.
- [var NSCompressionErrorMinimum: Int](nscompressionerrorminimum-swift.var.md)
  The start of the range of error codes reserved for compression errors.
- [var NSCompressionFailedError: Int](nscompressionfailederror-swift.var.md)
  An error code value that indicates a failure to compress data using the provided algorithm.
- [var NSDecompressionFailedError: Int](nsdecompressionfailederror-swift.var.md)
  An error code value that indicates a failure to decompress data using the provided algorithm.

## Relationships

### Inherits From
- [NSData](nsdata.md)
### Inherited By
- [NSPurgeableData](nspurgeabledata.md)
### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [CVarArg](../Swift/CVarArg.md)
- [Collection](../Swift/Collection.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProtocol](dataprotocol.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata)*