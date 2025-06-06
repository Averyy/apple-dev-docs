# standardError

**Framework**: Foundation  
**Kind**: property

The file handle associated with the standard error file.

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
class var standardError: FileHandle { get }
```

#### Return Value

The shared file handle associated with the standard error file.

#### Discussion

Conventionally this is a terminal device where the system sends error messages. There’s one standard error file handle per process; it’s a shared instance.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## See Also

- [convenience init(fileDescriptor: Int32)](filehandle/init(filedescriptor:).md)
  Creates and returns a file handle object associated with the specified file descriptor.
- [class var standardInput: FileHandle](filehandle/standardinput.md)
  The file handle associated with the standard input file.
- [class var standardOutput: FileHandle](filehandle/standardoutput.md)
  The file handle associated with the standard output file.
- [class var nullDevice: FileHandle](filehandle/nulldevice.md)
  The file handle associated with a null device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/standarderror)*