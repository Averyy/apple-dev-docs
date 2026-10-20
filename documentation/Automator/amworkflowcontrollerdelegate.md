# AMWorkflowControllerDelegate

**Framework**: Automator  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods that a delegate of a workflow controller implements.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
protocol AMWorkflowControllerDelegate : NSObjectProtocol
```

```objc
@protocol AMWorkflowControllerDelegate <NSObject>
```

## Topics

### Preparing to Run
- [func workflowController(AMWorkflowController, willRun: AMAction)](./amworkflowcontrollerdelegate/workflowcontroller%28_,willrun%29.md)
  Notifies the delegate when the specified action is about to run.
- [func workflowControllerWillRun(AMWorkflowController)](./amworkflowcontrollerdelegate/workflowcontrollerwillrun%28_%29.md)
  Notifies the delegate when the workflow controller object is about to run.
### Running
- [func workflowController(AMWorkflowController, didRun: AMAction)](./amworkflowcontrollerdelegate/workflowcontroller%28_,didrun%29.md)
  Notifies the delegate when the specified action finishes running.
- [func workflowControllerDidRun(AMWorkflowController)](./amworkflowcontrollerdelegate/workflowcontrollerdidrun%28_%29.md)
  Notifies the delegate when the workflow controller object finishes running.
### Stopping
- [func workflowControllerWillStop(AMWorkflowController)](./amworkflowcontrollerdelegate/workflowcontrollerwillstop%28_%29.md)
  Tells the delegate that the workflow controller object is about to stop.
- [func workflowControllerDidStop(AMWorkflowController)](./amworkflowcontrollerdelegate/workflowcontrollerdidstop%28_%29.md)
  Tells the delegate that the workflow controller object has stopped.
### Handling Errors
- [func workflowController(AMWorkflowController, didError: any Error)](./amworkflowcontrollerdelegate/workflowcontroller%28_,diderror%29.md)
  Notifies the delegate when the workflow encounters an error.
### Deprecated
- [func workflowController(AMWorkflowController, willRun: AMAction)](./amworkflowcontrollerdelegate/workflowcontroller%28_,willrun%29.md)
  Notifies the delegate when the specified action is about to run.
- [func workflowControllerWillRun(AMWorkflowController)](./amworkflowcontrollerdelegate/workflowcontrollerwillrun%28_%29.md)
  Notifies the delegate when the workflow controller object is about to run.
- [func workflowController(AMWorkflowController, didRun: AMAction)](./amworkflowcontrollerdelegate/workflowcontroller%28_,didrun%29.md)
  Notifies the delegate when the specified action finishes running.
- [func workflowControllerDidRun(AMWorkflowController)](./amworkflowcontrollerdelegate/workflowcontrollerdidrun%28_%29.md)
  Notifies the delegate when the workflow controller object finishes running.
- [func workflowControllerWillStop(AMWorkflowController)](./amworkflowcontrollerdelegate/workflowcontrollerwillstop%28_%29.md)
  Tells the delegate that the workflow controller object is about to stop.
- [func workflowControllerDidStop(AMWorkflowController)](./amworkflowcontrollerdelegate/workflowcontrollerdidstop%28_%29.md)
  Tells the delegate that the workflow controller object has stopped.
- [func workflowController(AMWorkflowController, didError: any Error)](./amworkflowcontrollerdelegate/workflowcontroller%28_,diderror%29.md)
  Notifies the delegate when the workflow encounters an error.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Accessing the Delegate
- [var delegate: (any AMWorkflowControllerDelegate)?](./amworkflowcontroller/delegate.md)
  The controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate)*