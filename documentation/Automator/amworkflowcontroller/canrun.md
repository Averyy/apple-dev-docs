# canRun

**Framework**: Automator  
**Kind**: property

A Boolean value that indicates whether the controller’s workflow is able to run.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var canRun: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the controller’s workflow is able to run; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

You might use this method to determine when to enable a “Run” button or other UI element you use to run the workflow.

## See Also

- [var isPaused: Bool](amworkflowcontroller/ispaused.md)
  A Boolean value that indicates whether the controller’s workflow is currently paused.
- [var isRunning: Bool](amworkflowcontroller/isrunning.md)
  A Boolean value that indicates whether the controller’s workflow is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller/canrun)*