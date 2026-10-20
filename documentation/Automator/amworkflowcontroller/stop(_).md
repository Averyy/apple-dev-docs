# stop(_:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Stops the associated workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
@IBAction
func stop(_ sender: Any)
```

```objc
- (void) stop:(id) sender;
```

## Parameters

- `sender`: Object that initiated the stop action.

## See Also

### Controlling the Workflow
- [func pause(Any)](./pause%28_%29.md)
  Pauses a workflow that’s running.
- [func reset(Any)](./reset%28_%29.md)
  Stops a workflow, clears any action results, and resets the workflow back to an un-run state.
- [func run(Any)](./run%28_%29.md)
  Runs the associated workflow, after first clearing any results stored by its actions during any previous run.
- [func step(Any)](./step%28_%29.md)
  In a paused workflow, runs the next action in the workflow and then pauses again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowcontroller/stop(_:))*