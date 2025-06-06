# workflowController(_:willRun:)

**Framework**: Automator  
**Kind**: method

Notifies the delegate when the specified action is about to run.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
optional func workflowController(_ controller: AMWorkflowController, willRun action: AMAction)
```

## Parameters

- `controller`: The controller object sending the message.
- `action`: The workflow action to run.

## See Also

- [func workflowControllerWillRun(AMWorkflowController)](amworkflowcontrollerdelegate/workflowcontrollerwillrun(_:).md)
  Notifies the delegate when the workflow controller object is about to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller(_:willrun:))*