# waitUntilExit()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Blocks the process until the receiver is finished.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func waitUntilExit()
```

```objc
- (void) waitUntilExit;
```

#### Discussion

This method first checks to see if the receiver is still running using [`isRunning`](./isrunning.md). Then it polls the current run loop using `NSDefaultRunLoopMode` until the task completes.

**Swift**:

```swift
let task: NSTask = // Create and initialize a task
    task.launch()
task.waitUntilExit()
let status = task.terminationStatus
 
if status == 0 {
    print("Task succeeded.")
} else {
    print("Task failed.")
}
```

**Objective-C**:

```objc
NSTask *task = // Create and initialize a task
[task launch];
[task waitUntilExit];
int status = [task terminationStatus];
 
if (status == 0) {
    NSLog(@"Task succeeded.");
} else {
    NSLog(@"Task failed.");
}
```

[`waitUntilExit()`](./waituntilexit%28%29.md) does not guarantee that the [`terminationHandler`](./terminationhandler.md) block has been fully executed before [`waitUntilExit()`](./waituntilexit%28%29.md) returns.

## See Also

### Related Documentation
- [func launch()](./launch%28%29.md)
  Launches the task represented by the receiver.
### Running and stopping
- [func run() throws](./run%28%29.md)
  Runs the process with the current environment.
- [func interrupt()](./interrupt%28%29.md)
  Sends an interrupt signal to the receiver and all of its subtasks.
- [func resume() -> Bool](./resume%28%29.md)
  Resumes execution of a suspended task.
- [func suspend() -> Bool](./suspend%28%29.md)
  Suspends execution of the receiver task.
- [func terminate()](./terminate%28%29.md)
  Sends a terminate signal to the receiver and all of its subtasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/waituntilexit())*