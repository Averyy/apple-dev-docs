# environment

**Framework**: Foundation  
**Kind**: property

The environment for the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var environment: [String : String]? { get set }
```

#### Discussion

If this method isn’t used, the environment is inherited from the process that created the receiver. This method raises an `NSInvalidArgumentException` if the system has launched the receiver.

## Parameters

- `environmentDictionary`: A dictionary of environment variable values whose keys are the variable names.

## See Also

- [var arguments: [String]?](process/arguments.md)
  The command arguments that the system uses to launch the executable.
- [var currentDirectoryURL: URL?](process/currentdirectoryurl.md)
  The current directory for the receiver.
- [var executableURL: URL?](process/executableurl.md)
  The receiver’s executable.
- [var qualityOfService: QualityOfService](process/qualityofservice.md)
  The default quality of service level the system applies to operations the task executes.
- [var standardError: Any?](process/standarderror.md)
  The standard error for the receiver.
- [var standardInput: Any?](process/standardinput.md)
  The standard input for the receiver.
- [var standardOutput: Any?](process/standardoutput.md)
  The standard output for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/environment)*