# workflowControllerWillRun(_:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when the workflow controller object is about to run.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
optional func workflowControllerWillRun(_ controller: AMWorkflowController)
```

```objc
- (void) workflowControllerWillRun:(AMWorkflowController *) controller;
```

## Parameters

- `controller`: The workflow controller object to run.

## See Also

### Preparing to Run
- [func workflowController(AMWorkflowController, willRun: AMAction)](./workflowcontroller%28_,willrun%29.md)
  Notifies the delegate when the specified action is about to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerwillrun(_:))*