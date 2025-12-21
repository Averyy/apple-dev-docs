# Data

**Framework**: Foundation  
**Kind**: struct

A byte buffer in memory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct Data
```

## Mentions

- [Processing URL session data task results with Combine](processing-url-session-data-task-results-with-combine.md)
- [Encoding and Decoding Custom Types](encoding-and-decoding-custom-types.md)

#### Overview

The [`Data`](data.md) value type allows simple byte buffers to take on the behavior of Foundation objects. You can create empty or pre-populated buffers from a variety of sources and later add or remove bytes. You can filter and sort the content, or compare against other buffers. You can manipulate subranges of bytes and iterate over some or all of them.

[`Data`](data.md) bridges to the [`NSData`](nsdata.md) class and its mutable subclass, [`NSMutableData`](nsmutabledata.md). You can use these interchangeably in code that interacts with Objective-C APIs.

## Topics

### Creating Empty Data
- [init()](data/init.md)
  Creates an empty data buffer.
- [init(capacity: Int)](data/init(capacity:).md)
  Creates an empty data buffer of a specified size.
- [init(count: Int)](data/init(count:).md)
  Creates a new data buffer with the specified count of zeroed bytes.
- [func resetBytes(in: Range<Data.Index>)](data/resetbytes(in:).md)
  Sets a region of the data buffer to `0`.
### Creating Populated Data
- [init()](data/init.md)
  Creates an empty data buffer.
- [init<SourceType>(buffer: UnsafeBufferPointer<SourceType>)](data/init(buffer:)-75sng.md)
  Creates a data buffer with copied memory content using a buffer pointer.
- [init<SourceType>(buffer: UnsafeMutableBufferPointer<SourceType>)](data/init(buffer:)-6xgv4.md)
  Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytes: UnsafeRawPointer, count: Int)](data/init(bytes:count:).md)
  Creates data with copied memory content.
- [init(bytesNoCopy: UnsafeMutableRawPointer, count: Int, deallocator: Data.Deallocator)](data/init(bytesnocopy:count:deallocator:).md)
  Creates a data buffer with memory content without copying the bytes.
- [init(capacity: Int)](data/init(capacity:).md)
  Creates an empty data buffer of a specified size.
- [init(count: Int)](data/init(count:).md)
  Creates a new data buffer with the specified count of zeroed bytes.
### Creating Data from Raw Memory
- [init(bytes: UnsafeRawPointer, count: Int)](data/init(bytes:count:).md)
  Creates data with copied memory content.
- [init<SourceType>(buffer: UnsafeBufferPointer<SourceType>)](data/init(buffer:)-75sng.md)
  Creates a data buffer with copied memory content using a buffer pointer.
- [init<SourceType>(buffer: UnsafeMutableBufferPointer<SourceType>)](data/init(buffer:)-6xgv4.md)
  Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, count: Int, deallocator: Data.Deallocator)](data/init(bytesnocopy:count:deallocator:).md)
  Creates a data buffer with memory content without copying the bytes.
- [Data.Deallocator](data/deallocator.md)
  A deallocator you use to customize how the backing store is deallocated for data created with the no-copy initializer.
### Reading and Writing Data
- [func write(to: URL, options: Data.WritingOptions) throws](data/write(to:options:).md)
  Writes the contents of the data buffer to a location.
- [typealias ReadingOptions](data/readingoptions.md)
  Options to control the reading of data from a URL.
- [typealias WritingOptions](data/writingoptions.md)
  Options to control the writing of data to a URL.
### Base-64 Encoding
- [func base64EncodedData(options: Data.Base64EncodingOptions) -> Data](data/base64encodeddata(options:).md)
  Returns Base-64 encoded data.
- [func base64EncodedString(options: Data.Base64EncodingOptions) -> String](data/base64encodedstring(options:).md)
  Returns a Base-64 encoded string.
- [typealias Base64DecodingOptions](data/base64decodingoptions.md)
  Options to use when decoding data.
- [typealias Base64EncodingOptions](data/base64encodingoptions.md)
  Options to use when encoding data.
### Accessing Bytes
- [subscript(Data.Index) -> UInt8](data/subscript(_:)-8kg64.md)
  Accesses the byte at the specified index.
### Accessing Underlying Memory
- [func withUnsafeBytes<ResultType, ContentType>((UnsafePointer<ContentType>) throws -> ResultType) rethrows -> ResultType](data/withunsafebytes(_:).md)
  Accesses the raw bytes in the data’s buffer.
- [func withUnsafeMutableBytes<ResultType, ContentType>((UnsafeMutablePointer<ContentType>) throws -> ResultType) rethrows -> ResultType](data/withunsafemutablebytes(_:)-7ac1g.md)
  Mutates the raw bytes in the data’s buffer.
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](data/copybytes(to:count:).md)
  Copies the contents of the data to memory.
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<Data.Index>)](data/copybytes(to:from:)-8qk4r.md)
  Copies a subset of the contents of the data to memory.
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, from: Range<Data.Index>?) -> Int](data/copybytes(to:from:)-4o6zj.md)
  Copies the bytes in a range from the data into a buffer.
### Adding Bytes
- [func append(Data)](data/append(_:)-vjwy.md)
  Appends the specified data to the end of this data.
- [func append<SourceType>(UnsafeBufferPointer<SourceType>)](data/append(_:)-xtlw.md)
  Append a buffer of bytes to the data.
- [func append(UnsafePointer<UInt8>, count: Int)](data/append(_:count:).md)
  Appends the specified bytes from memory to the end of the data.
- [func append(contentsOf: [UInt8])](data/append(contentsof:).md)
  Appends the bytes in the specified array to the end of the data.
### Replacing a Range of Bytes
- [func replaceSubrange(Range<Data.Index>, with: Data)](data/replacesubrange(_:with:)-3jcfi.md)
  Replaces a region of bytes in the data with new data.
- [func replaceSubrange<ByteCollection>(Range<Data.Index>, with: ByteCollection)](data/replacesubrange(_:with:)-9u7ry.md)
  Replaces a region of bytes in the data with new bytes from a collection.
- [func replaceSubrange<SourceType>(Range<Data.Index>, with: UnsafeBufferPointer<SourceType>)](data/replacesubrange(_:with:)-9nzh.md)
  Replaces a region of bytes in the data with new bytes from a buffer.
- [func replaceSubrange(Range<Data.Index>, with: UnsafeRawPointer, count: Int)](data/replacesubrange(_:with:count:).md)
  Replaces a region of bytes in the data with bytes from memory.
### Finding Bytes
- [func range(of: Data, options: Data.SearchOptions, in: Range<Data.Index>?) -> Range<Data.Index>?](data/range(of:options:in:).md)
  Finds the range of the specified data as a subsequence of this data, if it exists.
- [typealias SearchOptions](data/searchoptions.md)
  Options that control a data search operation.
### Excluding Bytes
- [func advanced(by: Int) -> Data](data/advanced(by:).md)
  Returns a new data buffer created by removing the given number of bytes from the front of the original buffer.
### Iterating Over Bytes
- [func makeIterator() -> Data.Iterator](data/makeiterator.md)
  Returns an iterator over the contents of the data.
- [func enumerateBytes((UnsafeBufferPointer<UInt8>, Data.Index, inout Bool) -> Void)](data/enumeratebytes(_:).md)
  Enumerates the contents of the data’s buffer.
### Splitting the Buffer
- [func subdata(in: Range<Data.Index>) -> Data](data/subdata(in:).md)
  Returns a new copy of the data in a specified range.
### Comparing Data
- [static func == (Data, Data) -> Bool](data/==(_:_:).md)
  Returns `true` if the two `Data` arguments are equal.
### Manipulating Indexes
- [var startIndex: Data.Index](data/startindex.md)
  The beginning index into the data.
- [var endIndex: Data.Index](data/endindex.md)
  The end index into the data.
### Describing Data
- [var description: String](data/description.md)
  A human-readable description for the data.
- [var debugDescription: String](data/debugdescription.md)
  A human-readable debug description for the data.
### Using Reference Types
- [class NSData](nsdata.md)
  A static byte buffer in memory.
- [class NSMutableData](nsmutabledata.md)
  An object representing a dynamic byte buffer in memory.
### Initializers
- [init?(base64Encoded: Data, options: Data.Base64DecodingOptions)](data/init(base64encoded:options:)-1g88z.md)
  Initialize a `Data` from a Base-64, UTF-8 encoded `Data`.
- [init?(base64Encoded: String, options: Data.Base64DecodingOptions)](data/init(base64encoded:options:)-654f.md)
  Initialize a `Data` from a Base-64 encoded String using the given options.
- [init(bytes: Array<UInt8>)](data/init(bytes:)-5krj4.md)
- [init<S>(bytes: S)](data/init(bytes:)-5s0rs.md)
- [init(bytes: ArraySlice<UInt8>)](data/init(bytes:)-9othw.md)
- [init(contentsOf: URL, options: Data.ReadingOptions) throws](data/init(contentsof:options:).md)
  Initialize a `Data` with the contents of a `URL`.
- [init(referencing: NSData)](data/init(referencing:).md)
  Initialize a `Data` by adopting a reference type.
- [init(repeating: UInt8, count: Int)](data/init(repeating:count:).md)
  Initialize a `Data` with a repeating byte pattern
### Instance Properties
- [var bytes: RawSpan](data/bytes.md)
- [var count: Int](data/count.md)
  The number of bytes in the data.
- [var mutableBytes: MutableRawSpan](data/mutablebytes.md)
- [var mutableSpan: MutableSpan<UInt8>](data/mutablespan.md)
- [var span: Span<UInt8>](data/span.md)
### Instance Methods
- [func hash(into: inout Hasher)](data/hash(into:).md)
  The hash value for the data.
- [func withUnsafeMutableBytes<ResultType>((UnsafeMutableRawBufferPointer) throws -> ResultType) rethrows -> ResultType](data/withunsafemutablebytes(_:)-8o6xa.md)
### Subscripts
- [subscript<R>(R) -> Data](data/subscript(_:)-59z5z.md)
### Default Implementations
- [Attachable Implementations](data/attachable-implementations.md)
- [CustomDebugStringConvertible Implementations](data/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](data/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Attachable](../Testing/Attachable.md)
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [Collection](../Swift/Collection.md)
- [ContiguousBytes](contiguousbytes.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProtocol](dataprotocol.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [MutableDataProtocol](mutabledataprotocol.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [RangeReplaceableCollection](../Swift/RangeReplaceableCollection.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)
- [Transferable](../CoreTransferable/Transferable.md)

## See Also

- [protocol DataProtocol](dataprotocol.md)
  A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.
- [protocol MutableDataProtocol](mutabledataprotocol.md)
  A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.
- [protocol ContiguousBytes](contiguousbytes.md)
  A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data)*