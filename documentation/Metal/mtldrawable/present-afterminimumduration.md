# present(afterMinimumDuration:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Presents the drawable onscreen as soon as possible after a previous drawable is visible for the specified duration.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func present(afterMinimumDuration duration: CFTimeInterval)
```

#### Discussion

When a command queue schedules a command buffer for execution, it tracks whether any commands in that command buffer need to render or write to the drawable object. When you call this method, the drawable presents its contents at a future time when all render and write requests for that drawable are complete and a previous drawable has been visible onscreen for the specified duration. Use this method to schedule drawables at a regular interval.

> **Note**:  To avoid presenting a drawable before any work is scheduled, or to avoid holding on to a drawable longer than necessary, call a command buffer’s [`present(_:afterMinimumDuration:)`](mtlcommandbuffer/present(_:afterminimumduration:).md) method instead. The [`present(_:afterMinimumDuration:)`](mtlcommandbuffer/present(_:afterminimumduration:).md) method is a convenience method that calls the given drawable’s [`present(afterMinimumDuration:)`](mtldrawable/present(afterminimumduration:).md) method after the command queue schedules that command buffer for execution.

 To avoid presenting a drawable before any work is scheduled, or to avoid holding on to a drawable longer than necessary, call a command buffer’s [`present(_:afterMinimumDuration:)`](mtlcommandbuffer/present(_:afterminimumduration:).md) method instead. The [`present(_:afterMinimumDuration:)`](mtlcommandbuffer/present(_:afterminimumduration:).md) method is a convenience method that calls the given drawable’s [`present(afterMinimumDuration:)`](mtldrawable/present(afterminimumduration:).md) method after the command queue schedules that command buffer for execution.

## Parameters

- `duration`: The previous drawable’s minimum display time, in seconds.

## See Also

- [func present()](mtldrawable/present.md)
  Presents the drawable onscreen as soon as possible.
- [func present(at: CFTimeInterval)](mtldrawable/present(at:).md)
  Presents the drawable onscreen at a specific host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawable/present(afterminimumduration:))*