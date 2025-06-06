# pause(_:)

**Framework**: Automator  
**Kind**: method

Pauses a workflow that’s running.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
@IBAction
@MainActor func pause(_ sender: Any)
```

## Parameters

- `sender`: Object that initiated the pause action.

## See Also

- [func reset(Any)](amworkflowcontroller/reset(_:).md)
  Stops a workflow, clears any action results, and resets the workflow back to an un-run state.
- [func run(Any)](amworkflowcontroller/run(_:).md)
  Runs the associated workflow, after first clearing any results stored by its actions during any previous run.
- [func step(Any)](amworkflowcontroller/step(_:).md)
  In a paused workflow, runs the next action in the workflow and then pauses again.
- [func stop(Any)](amworkflowcontroller/stop(_:).md)
  Stops the associated workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller/pause(_:))*