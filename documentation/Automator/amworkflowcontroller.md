# AMWorkflowController

**Framework**: Automator  
**Kind**: class

An object that lets you manage an Automator workflow in your app.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMWorkflowController
```

#### Overview

A controller can run and stop a workflow and obtain information about its state. The controller’s delegate ([`AMWorkflowControllerDelegate`](amworkflowcontrollerdelegate.md)) receives messages as the workflow is executed and its actions are run.

You can load and run a workflow with minimal overhead by using the [`AMWorkflow`](amworkflow.md) class method [`run(at:withInput:)`](amworkflow/run(at:withinput:).md). Use [`AMWorkflowController`](amworkflowcontroller.md) where you need greater control, such as the ability to start and stop the workflow. In that case, you must create and initialize both the workflow and the workflow controller objects.

## Topics

### Accessing the Workflow
- [var workflow: AMWorkflow?](amworkflowcontroller/workflow.md)
  The controller’s workflow.
### Accessing the Workflow View
- [var workflowView: AMWorkflowView?](amworkflowcontroller/workflowview-swift.property.md)
  The controller’s workflow view.
### Accessing the Delegate
- [var delegate: (any AMWorkflowControllerDelegate)?](amworkflowcontroller/delegate.md)
  The controller’s delegate.
- [protocol AMWorkflowControllerDelegate](amworkflowcontrollerdelegate.md)
  A set of optional methods that a delegate of a workflow controller implements.
### Controlling the Workflow
- [func pause(Any)](amworkflowcontroller/pause(_:).md)
  Pauses a workflow that’s running.
- [func reset(Any)](amworkflowcontroller/reset(_:).md)
  Stops a workflow, clears any action results, and resets the workflow back to an un-run state.
- [func run(Any)](amworkflowcontroller/run(_:).md)
  Runs the associated workflow, after first clearing any results stored by its actions during any previous run.
- [func step(Any)](amworkflowcontroller/step(_:).md)
  In a paused workflow, runs the next action in the workflow and then pauses again.
- [func stop(Any)](amworkflowcontroller/stop(_:).md)
  Stops the associated workflow.
### Getting Workflow Information
- [var canRun: Bool](amworkflowcontroller/canrun.md)
  A Boolean value that indicates whether the controller’s workflow is able to run.
- [var isPaused: Bool](amworkflowcontroller/ispaused.md)
  A Boolean value that indicates whether the controller’s workflow is currently paused.
- [var isRunning: Bool](amworkflowcontroller/isrunning.md)
  A Boolean value that indicates whether the controller’s workflow is currently running.

## Relationships

### Inherits From
- [NSController](../AppKit/NSController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSEditorRegistration](../AppKit/NSEditorRegistration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AMWorkflow](amworkflow.md)
  An object that lets you use an Automator workflow in your app.
- [class AMWorkflowView](amworkflowview.md)
  An object that lets you view and edit Automator workflows in your app.
- [class AMWorkspace](amworkspace.md)
  A workspace for running an Automator workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller)*