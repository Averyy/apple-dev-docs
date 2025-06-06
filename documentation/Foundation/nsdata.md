# NSData

**Framework**: Foundation  
**Kind**: class

A static byte buffer in memory.

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
class NSData
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Overview

In Swift, the buffer bridges to [`Data`](data.md); use [`NSData`](nsdata.md) when you need reference semantics or other Foundation-specific behavior.

[`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) and its mutable subclass [`NSMutableData`](nsmutabledata.md) provide data objects, or object-oriented wrappers for byte buffers. Data objects let simple allocated buffers (that is, data with no embedded pointers) take on the behavior of Foundation objects.

The size of the data is subject to a theoretical limit of about 8 exabytes (1 EB = 10¹⁸ bytes; in practice, the limit should not be a factor).

[`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) is  with its Core Foundation counterpart, [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`Data`](data.md) structure, which bridges to the [`NSData`](nsdata.md) class and its mutable subclass [`NSMutableData`](nsmutabledata.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

 The Swift overlay to the Foundation framework provides the [`Data`](data.md) structure, which bridges to the [`NSData`](nsdata.md) class and its mutable subclass [`NSMutableData`](nsmutabledata.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

##### Writing Data Atomically

[`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) provides methods for atomically saving their contents to a file, which guarantee that the data is either saved in its entirety, or it fails completely. An atomic write first writes the data to a temporary file and then, only if this write succeeds, moves the temporary file to its final location.

Although atomic write operations minimize the risk of data loss due to corrupt or partially written files, they may not be appropriate when writing to a temporary directory, the user’s home directory or other publicly accessible directories. When you work with a publicly accessible file, treat that file as an untrusted and potentially dangerous resource. An attacker may compromise or corrupt these files. The attacker can also replace the files with hard or symbolic links, causing your write operations to overwrite or corrupt other system resources.

Avoid using the [`write(to:atomically:)`](nsdata/write(to:atomically:).md) method (and the related methods) when working inside a publicly accessible directory. Instead, use [`FileHandle`](filehandle.md) with an existing file descriptor to securely write the file.

For more information, see [`Securing File Operations`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585-SW9) in [`Secure Coding Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## Topics

### Creating Data
- [init(bytes: UnsafeRawPointer?, length: Int)](nsdata/init(bytes:length:).md)
  Initializes a data object filled with a given number of bytes copied from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](nsdata/init(bytesnocopy:length:).md)
  Initializes a data object filled with a given number of bytes of data from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)?)](nsdata/init(bytesnocopy:length:deallocator:).md)
  Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, freeWhenDone: Bool)](nsdata/init(bytesnocopy:length:freewhendone:).md)
  Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [init(data: Data)](nsdata/init(data:).md)
  Initializes a data object with the contents of another data object.
### Reading Data from a File
- [convenience init?(contentsOfURL: URL)](nsdata/init(contentsofurl:)-6foqd.md)
  Creates a data object from the data at the specified file URL.
- [convenience init(contentsOfURL: URL, options: NSData.ReadingOptions) throws](nsdata/init(contentsofurl:options:)-95rht.md)
  Creates a data object from the data at the provided file URL using specific reading options.
- [init?(contentsOfFile: String)](nsdata/init(contentsoffile:).md)
  Initializes a data object with the content of the file at a given path.
- [init(contentsOfFile: String, options: NSData.ReadingOptions) throws](nsdata/init(contentsoffile:options:).md)
  Initializes a data object with the content of the file at a given path.
- [init?(contentsOfURL: URL)](nsdata/init(contentsofurl:)-6rrnr.md)
  Creates a data object from the data at the specified file URL, or returns `nil` if the system can’t create one.
- [init(contentsOfURL: URL, options: NSData.ReadingOptions) throws](nsdata/init(contentsofurl:options:)-5abi3.md)
  Creates a data object from the data at the provided file URL using specific reading options.
- [NSData.ReadingOptions](nsdata/readingoptions.md)
  Options for methods used to read data objects.
- [init?(contentsOfMappedFile: String)](nsdata/init(contentsofmappedfile:).md)
  Initializes a data object with the contents of the mapped file specified by a given path.
- [class func dataWithContentsOfMappedFile(String) -> Any?](nsdata/datawithcontentsofmappedfile(_:).md)
  Creates a data object from the mapped file at a given path.
### Writing Data to a File
- [func write(toFile: String, atomically: Bool) -> Bool](nsdata/write(tofile:atomically:).md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(toFile: String, options: NSData.WritingOptions) throws](nsdata/write(tofile:options:).md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](nsdata/write(to:atomically:).md)
  Writes the data object’s bytes to the location specified by a given URL.
- [func write(to: URL, options: NSData.WritingOptions) throws](nsdata/write(to:options:).md)
  Writes the data object’s bytes to the location specified by a given URL.
- [NSData.WritingOptions](nsdata/writingoptions.md)
  Options for methods used to write data objects.
### Encoding and Decoding Base64 Representations
- [init?(base64EncodedData: Data, options: NSData.Base64DecodingOptions)](nsdata/init(base64encodeddata:options:).md)
  Initializes a data object with the given Base64 encoded data.
- [init?(base64Encoding: String)](nsdata/init(base64encoding:).md)
  Initializes a data object initialized with the given Base64 encoded string.
- [init?(base64EncodedString: String, options: NSData.Base64DecodingOptions)](nsdata/init(base64encodedstring:options:).md)
  Initializes a data object with the given Base64 encoded string.
- [func base64EncodedData(options: NSData.Base64EncodingOptions) -> Data](nsdata/base64encodeddata(options:).md)
  Creates a Base64, UTF-8 encoded data object from the string using the given options.
- [func base64EncodedString(options: NSData.Base64EncodingOptions) -> String](nsdata/base64encodedstring(options:).md)
  Creates a Base64 encoded string from the string using the given options.
- [func base64Encoding() -> String](nsdata/base64encoding.md)
  Initializes a Base64 encoded string from the string.
- [NSData.Base64EncodingOptions](nsdata/base64encodingoptions.md)
  Options for methods used to Base64 encode data.
- [NSData.Base64DecodingOptions](nsdata/base64decodingoptions.md)
  Options to modify the decoding algorithm used to decode Base64 encoded data.
### Accessing Underlying Bytes
- [var bytes: UnsafeRawPointer](nsdata/bytes.md)
  A pointer to the data object’s contents.
- [func enumerateBytes((UnsafeRawPointer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdata/enumeratebytes(_:).md)
  Enumerates each range of bytes in the data object using a block.
- [func getBytes(UnsafeMutableRawPointer)](nsdata/getbytes(_:).md)
  Copies a data object’s contents into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, length: Int)](nsdata/getbytes(_:length:).md)
  Copies a number of bytes from the start of the data object into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, range: NSRange)](nsdata/getbytes(_:range:).md)
  Copies a range of bytes from the data object into a given buffer.
### Finding Data
- [func subdata(with: NSRange) -> Data](nsdata/subdata(with:).md)
  Returns a new data object containing the data object’s bytes that fall within the limits specified by a given range.
- [func range(of: Data, options: NSData.SearchOptions, in: NSRange) -> NSRange](nsdata/range(of:options:in:).md)
  Finds and returns the range of the first occurrence of the given data, within the given range, subject to given options.
- [NSData.SearchOptions](nsdata/searchoptions.md)
  Options for method used to search data objects.
### Testing Data
- [func isEqual(to: Data) -> Bool](nsdata/isequal(to:).md)
  Returns a Boolean value indicating whether this data object is the same as another.
- [var length: Int](nsdata/length.md)
  The number of bytes contained by the data object.
### Describing Data
- [var description: String](nsdata/description.md)
  A string that contains a hexadecimal representation of the data object’s contents in a property list format.
### Compressing and Decompressing Data
- [func compressed(using: NSData.CompressionAlgorithm) throws -> Self](nsdata/compressed(using:).md)
  Returns a new data object by compressing the data object’s bytes.
- [func decompressed(using: NSData.CompressionAlgorithm) throws -> Self](nsdata/decompressed(using:).md)
  Returns a new data object by decompressing data object’s bytes.
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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableData](nsmutabledata.md)
### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [CKRecordValue](../CloudKit/CKRecordValue-c.protocol.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CVarArg](../Swift/CVarArg.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata)*