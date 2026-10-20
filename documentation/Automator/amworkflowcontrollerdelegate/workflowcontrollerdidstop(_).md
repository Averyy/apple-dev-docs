# workflowControllerDidStop(_:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the workflow controller object has stopped.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
optional func workflowControllerDidStop(_ controller: AMWorkflowController)
```

```objc
- (void) workflowControllerDidStop:(AMWorkflowController *) controller;
```

## Parameters

- `controller`: The workflow controller object that stopped.

## See Also

### Stopping
- [func workflowControllerWillStop(AMWorkflowController)](./workflowcontrollerwillstop%28_%29.md)
  Tells the delegate that the workflow controller object is about to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerdidstop(_:))*