# executableURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s executable.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var executableURL: URL? { get set }
```

```objc
@property (copy, nullable) NSURL * executableURL;
```

## See Also

### Configuring a process
- [var arguments: [String]?](./arguments.md)
  The command arguments that the system uses to launch the executable.
- [var currentDirectoryURL: URL?](./currentdirectoryurl.md)
  The current directory for the receiver.
- [var environment: [String : String]?](./environment.md)
  The environment for the receiver.
- [var qualityOfService: QualityOfService](./qualityofservice.md)
  The default quality of service level the system applies to operations the task executes.
- [var standardError: Any?](./standarderror.md)
  The standard error for the receiver.
- [var standardInput: Any?](./standardinput.md)
  The standard input for the receiver.
- [var standardOutput: Any?](./standardoutput.md)
  The standard output for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/executableurl)*