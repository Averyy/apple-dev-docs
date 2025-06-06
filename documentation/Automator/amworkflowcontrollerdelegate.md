# AMWorkflowControllerDelegate

**Framework**: Automator  
**Kind**: protocol

A set of optional methods that a delegate of a workflow controller implements.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
protocol AMWorkflowControllerDelegate : NSObjectProtocol
```

## Topics

### Preparing to Run
- [func workflowController(AMWorkflowController, willRun: AMAction)](amworkflowcontrollerdelegate/workflowcontroller(_:willrun:).md)
  Notifies the delegate when the specified action is about to run.
- [func workflowControllerWillRun(AMWorkflowController)](amworkflowcontrollerdelegate/workflowcontrollerwillrun(_:).md)
  Notifies the delegate when the workflow controller object is about to run.
### Running
- [func workflowController(AMWorkflowController, didRun: AMAction)](amworkflowcontrollerdelegate/workflowcontroller(_:didrun:).md)
  Notifies the delegate when the specified action finishes running.
- [func workflowControllerDidRun(AMWorkflowController)](amworkflowcontrollerdelegate/workflowcontrollerdidrun(_:).md)
  Notifies the delegate when the workflow controller object finishes running.
### Stopping
- [func workflowControllerWillStop(AMWorkflowController)](amworkflowcontrollerdelegate/workflowcontrollerwillstop(_:).md)
  Tells the delegate that the workflow controller object is about to stop.
- [func workflowControllerDidStop(AMWorkflowController)](amworkflowcontrollerdelegate/workflowcontrollerdidstop(_:).md)
  Tells the delegate that the workflow controller object has stopped.
### Handling Errors
- [func workflowController(AMWorkflowController, didError: any Error)](amworkflowcontrollerdelegate/workflowcontroller(_:diderror:).md)
  Notifies the delegate when the workflow encounters an error.
### Deprecated
- [optional func workflowController(_ controller: AMWorkflowController, willRun action: AMAction)](AMWorkflowControllerDelegate/workflowController(_:willRun:).md)
  Notifies the delegate when the specified action is about to run.
- [optional func workflowControllerWillRun(_ controller: AMWorkflowController)](AMWorkflowControllerDelegate/workflowControllerWillRun(_:).md)
  Notifies the delegate when the workflow controller object is about to run.
- [optional func workflowController(_ controller: AMWorkflowController, didRun action: AMAction)](AMWorkflowControllerDelegate/workflowController(_:didRun:).md)
  Notifies the delegate when the specified action finishes running.
- [optional func workflowControllerDidRun(_ controller: AMWorkflowController)](AMWorkflowControllerDelegate/workflowControllerDidRun(_:).md)
  Notifies the delegate when the workflow controller object finishes running.
- [optional func workflowControllerWillStop(_ controller: AMWorkflowController)](AMWorkflowControllerDelegate/workflowControllerWillStop(_:).md)
  Tells the delegate that the workflow controller object is about to stop.
- [optional func workflowControllerDidStop(_ controller: AMWorkflowController)](AMWorkflowControllerDelegate/workflowControllerDidStop(_:).md)
  Tells the delegate that the workflow controller object has stopped.
- [optional func workflowController(_ controller: AMWorkflowController, didError error: any Error)](AMWorkflowControllerDelegate/workflowController(_:didError:).md)
  Notifies the delegate when the workflow encounters an error.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any AMWorkflowControllerDelegate)?](amworkflowcontroller/delegate.md)
  The controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate)*