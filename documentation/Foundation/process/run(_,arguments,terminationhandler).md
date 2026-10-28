# run(_:arguments:terminationHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and runs a task with a specified executable and arguments.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class func run(_ url: URL, arguments: [String], terminationHandler: (@Sendable (Process) -> Void)? = nil) throws -> Process
```

```objc
+ (NSTask *) launchedTaskWithExecutableURL:(NSURL *) url arguments:(NSArray<NSString *> *) arguments error:(NSError **) error terminationHandler:(void (^)(NSTask *)) terminationHandler;
```

## Return Value

An initialized `NSTask` object with the environment of the current process.

## Parameters

- `url`: The URL for the executable.
- `arguments`: An array of `NSString` objects that supplies the arguments to the task. If `arguments` is `nil`, the system raises an `NSInvalidArgumentException`.
- `terminationHandler`: The system invokes this completion block when the task has completed.

## See Also

### Creating and initializing a process
- [init()](./init%28%29.md)
  Returns an initialized process object with the environment of the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/run(_:arguments:terminationhandler:))*