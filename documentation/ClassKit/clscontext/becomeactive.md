# becomeActive()

**Framework**: ClassKit  
**Kind**: method

Tells a context to become the active context.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func becomeActive()
```

## Mentions

- [Informing ClassKit that a task is about to begin](informing-classkit-that-a-task-is-about-to-begin.md)

#### Discussion

You activate contexts to inform ClassKit which tasks are most recently or commonly visited.

Only one context can be active at a time, so if you tell a context to become active when another already is, the framework automatically deactivates the old one.

## See Also

- [Informing ClassKit that a task is about to begin](informing-classkit-that-a-task-is-about-to-begin.md)
  Activate and deactivate contexts according to user interaction.
- [func resignActive()](clscontext/resignactive.md)
  Tells a context to stop being the active context.
- [var isActive: Bool](clscontext/isactive.md)
  A Boolean indicating whether the context is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/becomeactive())*