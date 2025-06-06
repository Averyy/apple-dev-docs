# workflowController(_:didError:)

**Framework**: Automator  
**Kind**: method

Notifies the delegate when the workflow encounters an error.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
optional func workflowController(_ controller: AMWorkflowController, didError error: any Error)
```

## Parameters

- `controller`: The controller object sending the message.
- `error`: If a workflow error occurs, upon return contains an instance of   that describes the problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller(_:diderror:))*