# arguments

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The command arguments that the system uses to launch the executable.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var arguments: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * arguments;
```

## Discussion

The `NSTask` object converts both `path` and the strings in `arguments` to appropriate C-style strings (using [`fileSystemRepresentation`](../nsstring/filesystemrepresentation.md)) before passing them to the task through `argv[]`. The strings in `arguments` don’t undergo shell expansion, so you don’t need to do special quoting, and shell variables, such as `$PWD`, aren’t resolved.

## Parameters

- `arguments`: An array of `NSString` objects that supplies the arguments to the task. If `arguments` is `nil`, the system raises an `NSInvalidArgumentException`.

## See Also

### Configuring a process
- [var currentDirectoryURL: URL?](./currentdirectoryurl.md)
  The current directory for the receiver.
- [var environment: [String : String]?](./environment.md)
  The environment for the receiver.
- [var executableURL: URL?](./executableurl.md)
  The receiver’s executable.
- [var qualityOfService: QualityOfService](./qualityofservice.md)
  The default quality of service level the system applies to operations the task executes.
- [var standardError: Any?](./standarderror.md)
  The standard error for the receiver.
- [var standardInput: Any?](./standardinput.md)
  The standard input for the receiver.
- [var standardOutput: Any?](./standardoutput.md)
  The standard output for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/arguments)*