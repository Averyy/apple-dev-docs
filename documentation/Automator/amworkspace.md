# AMWorkspace

**Framework**: Automator  
**Kind**: class

A workspace for running an Automator workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMWorkspace
```

#### Overview

The [`AMWorkspace`](amworkspace.md) class provides access to the shared workspace in the Automator framework, where you can run workflows without a workflow controller. Use [`shared`](amworkspace/shared.md) to access the shared workspace and [`runWorkflow(atPath:withInput:)`](amworkspace/runworkflow(atpath:withinput:).md) to run your workflow in it.

## Topics

### Accessing the Shared Workspace
- [class var shared: AMWorkspace!](amworkspace/shared.md)
  The shared workspace object.
### Running Workflows
- [func runWorkflow(atPath: String!, withInput: Any!) throws -> Any](amworkspace/runworkflow(atpath:withinput:).md)
  Loads and runs the specified workflow file.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AMWorkflow](amworkflow.md)
  An object that lets you use an Automator workflow in your app.
- [class AMWorkflowController](amworkflowcontroller.md)
  An object that lets you manage an Automator workflow in your app.
- [class AMWorkflowView](amworkflowview.md)
  An object that lets you view and edit Automator workflows in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkspace)*