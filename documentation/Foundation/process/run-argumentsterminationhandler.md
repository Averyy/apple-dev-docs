# run(_:arguments:terminationHandler:)

**Framework**: Foundation  
**Kind**: method

Creates and runs a task with a specified executable and arguments.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class func run(_ url: URL, arguments: [String], terminationHandler: ((Process) -> Void)? = nil) throws -> Process
```

#### Return Value

An initialized `NSTask` object with the environment of the current process.

## Parameters

- `url`: The URL for the executable.
- `arguments`: An array of   objects that supplies the arguments to the task. If   is  , the system raises an  .
- `terminationHandler`: The system invokes this completion block when the task has completed.

## See Also

- [init()](process/init.md)
  Returns an initialized process object with the environment of the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/run(_:arguments:terminationhandler:))*