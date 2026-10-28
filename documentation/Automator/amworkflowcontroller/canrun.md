# canRun

**Framework**: Automator  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the controller’s workflow is able to run.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var canRun: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canRun;
```

## Return Value

[`true`](../../Swift/true.md) if the controller’s workflow is able to run; [`false`](../../Swift/false.md) otherwise.

## Discussion

You might use this method to determine when to enable a “Run” button or other UI element you use to run the workflow.

## See Also

### Getting Workflow Information
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the controller’s workflow is currently paused.
- [var isRunning: Bool](./isrunning.md)
  A Boolean value that indicates whether the controller’s workflow is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller/canrun)*