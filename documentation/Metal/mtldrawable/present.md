# present()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Presents the drawable onscreen as soon as possible.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func present()
```

#### Discussion

When a command queue schedules a command buffer for execution, it tracks whether any commands in that command buffer need to render or write to the drawable object. When you call this method, the drawable presents its contents as soon as possible after all scheduled render or write requests for that drawable are complete.

> **Note**:  To avoid presenting a drawable before any work is scheduled, or to avoid holding on to a drawable longer than necessary, call a command buffer’s [`present(_:)`](mtlcommandbuffer/present(_:).md) method instead of this method. The [`present(_:)`](mtlcommandbuffer/present(_:).md) method is a convenience method that calls the drawable’s [`present()`](mtldrawable/present().md) method after the command queue schedules that command buffer for execution.

 To avoid presenting a drawable before any work is scheduled, or to avoid holding on to a drawable longer than necessary, call a command buffer’s [`present(_:)`](mtlcommandbuffer/present(_:).md) method instead of this method. The [`present(_:)`](mtlcommandbuffer/present(_:).md) method is a convenience method that calls the drawable’s [`present()`](mtldrawable/present().md) method after the command queue schedules that command buffer for execution.

## See Also

- [func present(afterMinimumDuration: CFTimeInterval)](mtldrawable/present(afterminimumduration:).md)
  Presents the drawable onscreen as soon as possible after a previous drawable is visible for the specified duration.
- [func present(at: CFTimeInterval)](mtldrawable/present(at:).md)
  Presents the drawable onscreen at a specific host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawable/present())*