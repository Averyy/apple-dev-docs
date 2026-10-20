# isPaused

**Framework**: Automator  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the controller’s workflow is currently paused.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var isPaused: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPaused) BOOL paused;
```

#### Return Value

[`true`](../../Swift/true.md) if the controller’s workflow is currently paused; [`false`](../../Swift/false.md) otherwise.

## See Also

### Getting Workflow Information
- [var canRun: Bool](./canrun.md)
  A Boolean value that indicates whether the controller’s workflow is able to run.
- [var isRunning: Bool](./isrunning.md)
  A Boolean value that indicates whether the controller’s workflow is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller/ispaused)*