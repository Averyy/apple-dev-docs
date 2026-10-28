# standardOutput

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The file handle associated with the standard output file.

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
class var standardOutput: FileHandle { get }
```

```objc
@property (class, strong, readonly) NSFileHandle * fileHandleWithStandardOutput;
```

## Return Value

The shared file handle associated with the standard output file.

## Discussion

Conventionally this is a terminal device that receives a stream of data from a program. There’s one standard output file handle per process; it’s a shared instance.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## See Also

### Related Documentation
- [convenience init(fileDescriptor: Int32)](./init%28filedescriptor%29.md)
  Creates and returns a file handle object associated with the specified file descriptor.
### Getting a file handle
- [class var standardError: FileHandle](./standarderror.md)
  The file handle associated with the standard error file.
- [class var standardInput: FileHandle](./standardinput.md)
  The file handle associated with the standard input file.
- [class var nullDevice: FileHandle](./nulldevice.md)
  The file handle associated with a null device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/standardoutput)*