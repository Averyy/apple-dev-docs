# standardInput

**Framework**: Foundation  
**Kind**: property

The standard input for the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var standardInput: Any? { get set }
```

#### Discussion

If `file` is an `NSPipe` object, launching the receiver automatically closes the read end of the pipe in the current task. Don’t create a handle for the pipe and pass that as the argument, or the read end of the pipe won’t be closed automatically.

If this method isn’t used, the standard input is inherited from the process that created the receiver. This method raises an `NSInvalidArgumentException` if the system has lauched the receiver.

## Parameters

- `file`: The standard input for the receiver, which can be either an   or an   object.

## See Also

- [var arguments: [String]?](process/arguments.md)
  The command arguments that the system uses to launch the executable.
- [var currentDirectoryURL: URL?](process/currentdirectoryurl.md)
  The current directory for the receiver.
- [var environment: [String : String]?](process/environment.md)
  The environment for the receiver.
- [var executableURL: URL?](process/executableurl.md)
  The receiver’s executable.
- [var qualityOfService: QualityOfService](process/qualityofservice.md)
  The default quality of service level the system applies to operations the task executes.
- [var standardError: Any?](process/standarderror.md)
  The standard error for the receiver.
- [var standardOutput: Any?](process/standardoutput.md)
  The standard output for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/standardinput)*