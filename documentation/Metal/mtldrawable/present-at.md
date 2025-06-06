# present(at:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Presents the drawable onscreen at a specific host time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func present(at presentationTime: CFTimeInterval)
```

#### Discussion

When a command queue schedules a command buffer for execution, it tracks whether any commands in that command buffer need to render or write to the drawable object. When you call this method, the drawable waits until all render and write requests for that drawable are complete. If they complete prior to the specified time, the drawable presents the content at that time. If the commands complete after the presentation time, the drawable presents its contents as soon as possible.

> **Note**:  To avoid presenting a drawable before any work is scheduled, or to avoid holding on to a drawable longer than necessary, call a command buffer’s [`present(_:atTime:)`](mtlcommandbuffer/present(_:attime:).md) method instead of a drawable’s [`present(at:)`](mtldrawable/present(at:).md) method. The [`present(_:atTime:)`](mtlcommandbuffer/present(_:attime:).md) method is a convenience method that calls the given drawable’s [`present(at:)`](mtldrawable/present(at:).md) method after the command queue schedules that command buffer for execution.

## Parameters

- `presentationTime`: The Mach absolute time at which the drawable should be presented, in seconds.

## See Also

- [func present()](mtldrawable/present.md)
  Presents the drawable onscreen as soon as possible.
- [func present(afterMinimumDuration: CFTimeInterval)](mtldrawable/present(afterminimumduration:).md)
  Presents the drawable onscreen as soon as possible after a previous drawable is visible for the specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawable/present(at:))*