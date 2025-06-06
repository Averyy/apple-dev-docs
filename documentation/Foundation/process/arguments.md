# arguments

**Framework**: Foundation  
**Kind**: property

The command arguments that the system uses to launch the executable.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var arguments: [String]? { get set }
```

#### Discussion

The `NSTask` object converts both `path` and the strings in `arguments` to appropriate C-style strings (using [`fileSystemRepresentation`](nsstring/filesystemrepresentation.md)) before passing them to the task through `argv[]`. The strings in `arguments` don’t undergo shell expansion, so you don’t need to do special quoting, and shell variables, such as `$PWD`, aren’t resolved.

## Parameters

- `arguments`: An array of   objects that supplies the arguments to the task. If   is  , the system raises an  .

## See Also

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
- [var standardInput: Any?](process/standardinput.md)
  The standard input for the receiver.
- [var standardOutput: Any?](process/standardoutput.md)
  The standard output for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/arguments)*