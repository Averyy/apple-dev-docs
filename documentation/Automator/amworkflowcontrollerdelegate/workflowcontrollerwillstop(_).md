# workflowControllerWillStop(_:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the workflow controller object is about to stop.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
optional func workflowControllerWillStop(_ controller: AMWorkflowController)
```

```objc
- (void) workflowControllerWillStop:(AMWorkflowController *) controller;
```

## Parameters

- `controller`: The workflow controller object to stop.

## See Also

### Stopping
- [func workflowControllerDidStop(AMWorkflowController)](./workflowcontrollerdidstop%28_%29.md)
  Tells the delegate that the workflow controller object has stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerwillstop(_:))*