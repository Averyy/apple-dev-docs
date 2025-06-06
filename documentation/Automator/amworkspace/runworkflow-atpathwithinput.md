# runWorkflow(atPath:withInput:)

**Framework**: Automator  
**Kind**: method

Loads and runs the specified workflow file.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func runWorkflow(atPath path: String!, withInput input: Any!) throws -> Any
```

#### Return Value

`nil` if an error occurs or if the action completes successfully without producing output; otherwise, the output of the last action in the workflow.

## Parameters

- `path`: A path that specifies the location of the workflow file.
- `input`: The input for the first action in the workflow. Pass   if the first action doesn’t need input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkspace/runworkflow(atpath:withinput:))*