# waitUntilExit()

**Framework**: Foundation  
**Kind**: method

Blocks the process until the receiver is finished.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func waitUntilExit()
```

#### Discussion

This method first checks to see if the receiver is still running using [`isRunning`](process/isrunning.md). Then it polls the current run loop using `NSDefaultRunLoopMode` until the task completes.

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

[`waitUntilExit()`](process/waituntilexit().md) does not guarantee that the [`terminationHandler`](process/terminationhandler.md) block has been fully executed before [`waitUntilExit()`](process/waituntilexit().md) returns.

## See Also

- [func launch()](process/launch.md)
  Launches the task represented by the receiver.
- [func run() throws](process/run.md)
  Runs the process with the current environment.
- [func interrupt()](process/interrupt.md)
  Sends an interrupt signal to the receiver and all of its subtasks.
- [func resume() -> Bool](process/resume.md)
  Resumes execution of a suspended task.
- [func suspend() -> Bool](process/suspend.md)
  Suspends execution of the receiver task.
- [func terminate()](process/terminate.md)
  Sends a terminate signal to the receiver and all of its subtasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/waituntilexit())*