# workflowController(_:didRun:)

**Framework**: Automator  
**Kind**: method

Notifies the delegate when the specified action finishes running.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
optional func workflowController(_ controller: AMWorkflowController, didRun action: AMAction)
```

## Parameters

- `controller`: The controller object sending the message.
- `action`: The workflow action that ran.

## See Also

- [func workflowControllerDidRun(AMWorkflowController)](amworkflowcontrollerdelegate/workflowcontrollerdidrun(_:).md)
  Notifies the delegate when the workflow controller object finishes running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller(_:didrun:))*