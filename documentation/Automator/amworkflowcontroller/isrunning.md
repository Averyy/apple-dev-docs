# isRunning

**Framework**: Automator  
**Kind**: property

A Boolean value that indicates whether the controller’s workflow is currently running.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var isRunning: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the controller’s workflow is currently running; [`false`](https://developer.apple.com/documentation/swift/false) otherwise. Use `isRunning:` to determine whether the receiver’s workflow is currently running.

## See Also

- [var canRun: Bool](amworkflowcontroller/canrun.md)
  A Boolean value that indicates whether the controller’s workflow is able to run.
- [var isPaused: Bool](amworkflowcontroller/ispaused.md)
  A Boolean value that indicates whether the controller’s workflow is currently paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller/isrunning)*