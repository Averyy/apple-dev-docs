# AMWorkspace

**Framework**: Automator  
**Kind**: class  
**Role**: Class

A workspace for running an Automator workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMWorkspace
```

```objc
@interface AMWorkspace : NSObject
```

#### Overview

The [`AMWorkspace`](./amworkspace.md) class provides access to the shared workspace in the Automator framework, where you can run workflows without a workflow controller. Use [`shared`](./amworkspace/shared.md) to access the shared workspace and [`runWorkflow(atPath:withInput:)`](./amworkspace/runworkflow%28atpath,withinput%29.md) to run your workflow in it.

## Topics

### Accessing the Shared Workspace
- [class var shared: AMWorkspace!](./amworkspace/shared.md)
  The shared workspace object.
### Running Workflows
- [func runWorkflow(atPath: String!, withInput: Any!) throws -> Any](./amworkspace/runworkflow%28atpath,withinput%29.md)
  Loads and runs the specified workflow file.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Workflows
- [class AMWorkflow](./amworkflow.md)
  An object that lets you use an Automator workflow in your app.
- [class AMWorkflowController](./amworkflowcontroller.md)
  An object that lets you manage an Automator workflow in your app.
- [class AMWorkflowView](./amworkflowview.md)
  An object that lets you view and edit Automator workflows in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkspace)*