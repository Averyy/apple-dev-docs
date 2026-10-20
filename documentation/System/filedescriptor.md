# FileDescriptor

**Framework**: System  
**Kind**: struct  
**Role**: Structure

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
- [init(rawValue: CInt)](./filedescriptor/init%28rawvalue%29.md)
  Creates a strongly-typed file handle from a raw C file handle.
- [let rawValue: CInt](./filedescriptor/rawvalue.md)
  The raw C file handle.
### Opening a File
- [static func open(FilePath, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](./filedescriptor/open%28_,_,options,permissions,retryoninterrupt%29-4ql4b.md)
  Opens or creates a file for reading or writing.
- [static func open(UnsafePointer<CChar>, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](./filedescriptor/open%28_,_,options,permissions,retryoninterrupt%29-5t3xn.md)
  Opens or creates a file for reading or writing.
- [FileDescriptor.AccessMode](./filedescriptor/accessmode.md)
  The desired read and write access for a newly opened file.
- [FileDescriptor.OpenOptions](./filedescriptor/openoptions.md)
  Options that specify behavior for a newly-opened file.
### Reading From a File
- [func read(into: UnsafeMutableRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](./filedescriptor/read%28into,retryoninterrupt%29.md)
  Reads bytes at the current file offset into a buffer.
- [func read(fromAbsoluteOffset: Int64, into: UnsafeMutableRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](./filedescriptor/read%28fromabsoluteoffset,into,retryoninterrupt%29.md)
  Reads bytes at the specified offset into a buffer.
### Changing a File’s Offset
- [func seek(offset: Int64, from: FileDescriptor.SeekOrigin) throws -> Int64](./filedescriptor/seek%28offset,from%29.md)
  Repositions the offset for the given file descriptor.
- [FileDescriptor.SeekOrigin](./filedescriptor/seekorigin.md)
  Options for specifying what a file descriptor’s offset is relative to.
### Writing To A File
- [func write(UnsafeRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](./filedescriptor/write%28_,retryoninterrupt%29.md)
  Writes the contents of a buffer at the current file offset.
- [func write(toAbsoluteOffset: Int64, UnsafeRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](./filedescriptor/write%28toabsoluteoffset,_,retryoninterrupt%29.md)
  Writes the contents of a buffer at the specified offset.
- [func writeAll<S>(S) throws -> Int](./filedescriptor/writeall%28_%29.md)
  Writes a sequence of bytes to the current offset and then updates the offset.
- [func writeAll<S>(toAbsoluteOffset: Int64, S) throws -> Int](./filedescriptor/writeall%28toabsoluteoffset,_%29.md)
  Writes a sequence of bytes to the given offset.
### Closing a File
- [func close() throws](./filedescriptor/close%28%29.md)
  Deletes a file descriptor.
- [func closeAfter<R>(() throws -> R) throws -> R](./filedescriptor/closeafter%28_%29.md)
  Runs a closure and then closes the file descriptor, even if an error occurs.
### Structures
- [FileDescriptor.DuplicateOptions](./filedescriptor/duplicateoptions.md)
  Options that specify behavior for a duplicated file descriptor.
- [FileDescriptor.PipeOptions](./filedescriptor/pipeoptions.md)
  Options that specify behavior for a newly-created pipe.
### Instance Methods
- [func duplicate(as: FileDescriptor, options: FileDescriptor.DuplicateOptions, retryOnInterrupt: Bool) throws(Errno) -> FileDescriptor](./filedescriptor/duplicate%28as,options,retryoninterrupt%29.md)
  Duplicates this file descriptor and returns the newly created copy.
- [func duplicate(as: FileDescriptor?, retryOnInterrupt: Bool) throws -> FileDescriptor](./filedescriptor/duplicate%28as,retryoninterrupt%29.md)
  Duplicates this file descriptor and returns the newly created copy.
- [func resize(to: Int64, retryOnInterrupt: Bool) throws](./filedescriptor/resize%28to,retryoninterrupt%29.md)
  Truncates or extends the file referenced by this file descriptor.
- [func stat(retryOnInterrupt: Bool) throws(Errno) -> Stat](./filedescriptor/stat%28retryoninterrupt%29.md)
  Creates a `Stat` struct for the file referenced by this `FileDescriptor`.
### Type Properties
- [static var standardError: FileDescriptor](./filedescriptor/standarderror.md)
  The standard error file descriptor, with a numeric value of 2.
- [static var standardInput: FileDescriptor](./filedescriptor/standardinput.md)
  The standard input file descriptor, with a numeric value of 0.
- [static var standardOutput: FileDescriptor](./filedescriptor/standardoutput.md)
  The standard output file descriptor, with a numeric value of 1.
### Type Methods
- [static func pipe() throws -> (readEnd: FileDescriptor, writeEnd: FileDescriptor)](./filedescriptor/pipe%28%29.md)
  Creates a unidirectional data channel, which can be used for interprocess communication.
- [static func pipe(options: FileDescriptor.PipeOptions) throws(Errno) -> (readEnd: FileDescriptor, writeEnd: FileDescriptor)](./filedescriptor/pipe%28options%29.md)
  Creates a unidirectional data channel, which can be used for interprocess communication.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Files
- [struct FilePath](./filepath.md)
  Represents a location in the file system.
- [struct FilePermissions](./filepermissions.md)
  The access permissions for a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor)*