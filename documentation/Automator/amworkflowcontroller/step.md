# step(_:)

**Framework**: Automator  
**Kind**: method

In a paused workflow, runs the next action in the workflow and then pauses again.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
@IBAction
@MainActor func step(_ sender: Any)
```

#### Discussion

Stepping allows a workflow to be executed one action at a time. This is useful for ensuring that the workflow is doing what it’s supposed to do, as the results of each individual action can be inspected before moving on to the next.

## Parameters

- `sender`: Object that initiated the step action.

## See Also

- [func pause(Any)](amworkflowcontroller/pause(_:).md)
  Pauses a workflow that’s running.
- [func reset(Any)](amworkflowcontroller/reset(_:).md)
  Stops a workflow, clears any action results, and resets the workflow back to an un-run state.
- [func run(Any)](amworkflowcontroller/run(_:).md)
  Runs the associated workflow, after first clearing any results stored by its actions during any previous run.
- [func stop(Any)](amworkflowcontroller/stop(_:).md)
  Stops the associated workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller/step(_:))*