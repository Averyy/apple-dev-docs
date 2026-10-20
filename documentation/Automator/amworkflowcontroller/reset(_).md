# reset(_:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Stops a workflow, clears any action results, and resets the workflow back to an un-run state.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
@IBAction
func reset(_ sender: Any)
```

```objc
- (void) reset:(id) sender;
```

## Parameters

- `sender`: Object that initiated the reset action.

## See Also

### Controlling the Workflow
- [func pause(Any)](./pause%28_%29.md)
  Pauses a workflow that’s running.
- [func run(Any)](./run%28_%29.md)
  Runs the associated workflow, after first clearing any results stored by its actions during any previous run.
- [func step(Any)](./step%28_%29.md)
  In a paused workflow, runs the next action in the workflow and then pauses again.
- [func stop(Any)](./stop%28_%29.md)
  Stops the associated workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller/reset(_:))*