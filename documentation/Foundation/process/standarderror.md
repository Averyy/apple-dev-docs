# standardError

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The standard error for the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var standardError: Any? { get set }
```

```objc
@property (retain, nullable) id standardError;
```

## Discussion

If `file` is an `NSPipe` object, launching the receiver automatically closes the write end of the pipe in the current task. Don’t create a handle for the pipe and pass that as the argument, or the system won’t automatically close the write end of the pipe.

If this method isn’t used, the standard error is inherited from the process that created the receiver. This method raises an `NSInvalidArgumentException` if the system has lauched the receiver.

## Parameters

- `file`: The standard error for the receiver, which can be either an [`FileHandle`](../filehandle.md) or an [`Pipe`](../pipe.md) object.

## See Also

### Configuring a process
- [var arguments: [String]?](./arguments.md)
  The command arguments that the system uses to launch the executable.
- [var currentDirectoryURL: URL?](./currentdirectoryurl.md)
  The current directory for the receiver.
- [var environment: [String : String]?](./environment.md)
  The environment for the receiver.
- [var executableURL: URL?](./executableurl.md)
  The receiver’s executable.
- [var qualityOfService: QualityOfService](./qualityofservice.md)
  The default quality of service level the system applies to operations the task executes.
- [var standardInput: Any?](./standardinput.md)
  The standard input for the receiver.
- [var standardOutput: Any?](./standardoutput.md)
  The standard output for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/standarderror)*