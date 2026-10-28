# present()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Presents the drawable onscreen as soon as possible.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func present()
```

```objc
- (void) present;
```

## Discussion

When a command queue schedules a command buffer for execution, it tracks whether any commands in that command buffer need to render or write to the drawable object. When you call this method, the drawable presents its contents as soon as possible after all scheduled render or write requests for that drawable are complete.

> **Note**:  To avoid presenting a drawable before any work is scheduled, or to avoid holding on to a drawable longer than necessary, call a command buffer’s [`present(_:)`](../mtlcommandbuffer/present%28_%29.md) method instead of this method. The [`present(_:)`](../mtlcommandbuffer/present%28_%29.md) method is a convenience method that calls the drawable’s [`present()`](./present%28%29.md) method after the command queue schedules that command buffer for execution.

## See Also

### Presenting the drawable
- [func present(afterMinimumDuration: CFTimeInterval)](./present%28afterminimumduration%29.md)
  Presents the drawable onscreen as soon as possible after a previous drawable is visible for the specified duration.
- [func present(at: CFTimeInterval)](./present%28at%29.md)
  Presents the drawable onscreen at a specific host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawable/present())*