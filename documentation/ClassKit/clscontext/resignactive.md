# resignActive()

**Framework**: ClassKit  
**Kind**: method

Tells a context to stop being the active context.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func resignActive()
```

## Mentions

- [Informing ClassKit that a task is about to begin](informing-classkit-that-a-task-is-about-to-begin.md)

#### Discussion

Only one context can be active at a time, so the framework automatically calls this method for you if you activate another context.

## See Also

- [Informing ClassKit that a task is about to begin](informing-classkit-that-a-task-is-about-to-begin.md)
  Activate and deactivate contexts according to user interaction.
- [func becomeActive()](clscontext/becomeactive.md)
  Tells a context to become the active context.
- [var isActive: Bool](clscontext/isactive.md)
  A Boolean indicating whether the context is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/resignactive())*