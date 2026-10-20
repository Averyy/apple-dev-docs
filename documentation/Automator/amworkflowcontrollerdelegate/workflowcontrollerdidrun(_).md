# workflowControllerDidRun(_:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when the workflow controller object finishes running.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
optional func workflowControllerDidRun(_ controller: AMWorkflowController)
```

```objc
- (void) workflowControllerDidRun:(AMWorkflowController *) controller;
```

## Parameters

- `controller`: The workflow controller object that finished running.

## See Also

### Running
- [func workflowController(AMWorkflowController, didRun: AMAction)](./workflowcontroller%28_,didrun%29.md)
  Notifies the delegate when the specified action finishes running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerdidrun(_:))*