# FileDescriptor

**Framework**: System  
**Kind**: struct

An abstract handle to an input or output data resource, such as a file or a socket.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
struct FileDescriptor
```

#### Overview

You are responsible for managing the lifetime and validity of `FileDescriptor` values, in the same way as you manage a raw C file handle.

## Topics

### Creating a File Descriptor
- [init(rawValue: CInt)](filedescriptor/init(rawvalue:).md)
  Creates a strongly-typed file handle from a raw C file handle.
- [let rawValue: CInt](filedescriptor/rawvalue-swift.property.md)
  The raw C file handle.
- [FileDescriptor.RawValue](filedescriptor/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Opening a File
- [static func open(FilePath, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-4ql4b.md)
  Opens or creates a file for reading or writing.
- [static func open(UnsafePointer<CChar>, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-5t3xn.md)
  Opens or creates a file for reading or writing.
- [FileDescriptor.AccessMode](filedescriptor/accessmode.md)
  The desired read and write access for a newly opened file.
- [FileDescriptor.OpenOptions](filedescriptor/openoptions.md)
  Options that specify behavior for a newly-opened file.
### Reading From a File
- [func read(into: UnsafeMutableRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](filedescriptor/read(into:retryoninterrupt:).md)
  Reads bytes at the current file offset into a buffer.
- [func read(fromAbsoluteOffset: Int64, into: UnsafeMutableRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](filedescriptor/read(fromabsoluteoffset:into:retryoninterrupt:).md)
  Reads bytes at the specified offset into a buffer.
### Changing a File’s Offset
- [func seek(offset: Int64, from: FileDescriptor.SeekOrigin) throws -> Int64](filedescriptor/seek(offset:from:).md)
  Repositions the offset for the given file descriptor.
- [FileDescriptor.SeekOrigin](filedescriptor/seekorigin.md)
  Options for specifying what a file descriptor’s offset is relative to.
### Writing To A File
- [func write(UnsafeRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](filedescriptor/write(_:retryoninterrupt:).md)
  Writes the contents of a buffer at the current file offset.
- [func write(toAbsoluteOffset: Int64, UnsafeRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](filedescriptor/write(toabsoluteoffset:_:retryoninterrupt:).md)
  Writes the contents of a buffer at the specified offset.
- [func writeAll<S>(S) throws -> Int](filedescriptor/writeall(_:).md)
  Writes a sequence of bytes to the current offset and then updates the offset.
- [func writeAll<S>(toAbsoluteOffset: Int64, S) throws -> Int](filedescriptor/writeall(toabsoluteoffset:_:).md)
  Writes a sequence of bytes to the given offset.
### Closing a File
- [func close() throws](filedescriptor/close.md)
  Deletes a file descriptor.
- [func closeAfter<R>(() throws -> R) throws -> R](filedescriptor/closeafter(_:).md)
  Runs a closure and then closes the file descriptor, even if an error occurs.
### Encoding File Descriptors
- [init(from: any Decoder) throws](filedescriptor/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int32`.
- [func encode(to: any Encoder) throws](filedescriptor/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.
### Comparing File Descriptors
- [static func != (Self, Self) -> Bool](filedescriptor/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](filedescriptor/hash(into:).md)
- [var hashValue: Int](filedescriptor/hashvalue.md)
### Instance Methods
- [func duplicate(as: FileDescriptor?, retryOnInterrupt: Bool) throws -> FileDescriptor](filedescriptor/duplicate(as:retryoninterrupt:).md)
  Duplicates this file descriptor and return the newly created copy.
- [func resize(to: Int64, retryOnInterrupt: Bool) throws](filedescriptor/resize(to:retryoninterrupt:).md)
  Truncates or extends the file referenced by this file descriptor.
### Type Properties
- [static var standardError: FileDescriptor](filedescriptor/standarderror.md)
  The standard error file descriptor, with a numeric value of 2.
- [static var standardInput: FileDescriptor](filedescriptor/standardinput.md)
  The standard input file descriptor, with a numeric value of 0.
- [static var standardOutput: FileDescriptor](filedescriptor/standardoutput.md)
  The standard output file descriptor, with a numeric value of 1.
### Type Methods
- [static func pipe() throws -> (readEnd: FileDescriptor, writeEnd: FileDescriptor)](filedescriptor/pipe.md)
  Creates a unidirectional data channel, which can be used for interprocess communication.
### Default Implementations
- [Equatable Implementations](filedescriptor/equatable-implementations.md)
- [RawRepresentable Implementations](filedescriptor/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct FilePath](filepath.md)
  Represents a location in the file system.
- [struct FilePermissions](filepermissions.md)
  The access permissions for a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor)*