# isRunning

**Framework**: Automator  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the controller’s workflow is currently running.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var isRunning: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isRunning) BOOL running;
```

#### Discussion

[`true`](../../Swift/true.md) if the controller’s workflow is currently running; [`false`](../../Swift/false.md) otherwise. Use `isRunning:` to determine whether the receiver’s workflow is currently running.

## See Also

### Getting Workflow Information
- [var canRun: Bool](./canrun.md)
  A Boolean value that indicates whether the controller’s workflow is able to run.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the controller’s workflow is currently paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller/isrunning)*