# nullDevice

**Framework**: Foundation  
**Kind**: property

The file handle associated with a null device.

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
class var nullDevice: FileHandle { get }
```

#### Return Value

A file handle associated with a null device.

#### Discussion

You can use null-device file handles as “placeholders” for standard-device file handles or in collection objects to avoid exceptions and other errors resulting from messages being sent to invalid file handles. Read messages sent to a null-device file handle return an end-of-file indicator (an empty `NSData` object) rather than raise an exception. Write messages are no-ops, whereas [`fileDescriptor`](filehandle/filedescriptor.md) returns an illegal value. Other methods are no-ops or return “sensible” values.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## See Also

- [convenience init(fileDescriptor: Int32)](filehandle/init(filedescriptor:).md)
  Creates and returns a file handle object associated with the specified file descriptor.
- [class var standardError: FileHandle](filehandle/standarderror.md)
  The file handle associated with the standard error file.
- [class var standardInput: FileHandle](filehandle/standardinput.md)
  The file handle associated with the standard input file.
- [class var standardOutput: FileHandle](filehandle/standardoutput.md)
  The file handle associated with the standard output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/nulldevice)*