# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an initialized process object with the environment of the current process.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

## Return Value

An initialized process object with the environment of the current process.

## Discussion

If you need to modify the environment of a process, use alloc and init, and then set up the environment before launching the new process. Otherwise, just use the class method [`run(_:arguments:terminationHandler:)`](./run%28_,arguments,terminationhandler%29.md) to create and run the process.

## See Also

### Creating and initializing a process
- [class func run(URL, arguments: [String], terminationHandler: ((Process) -> Void)?) throws -> Process](./run%28_,arguments,terminationhandler%29.md)
  Creates and runs a task with a specified executable and arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/init())*