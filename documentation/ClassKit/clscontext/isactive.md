# isActive

**Framework**: ClassKit  
**Kind**: property

A Boolean indicating whether the context is active.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isActive: Bool { get }
```

#### Discussion

Use the [`becomeActive()`](clscontext/becomeactive().md) method to activate a context, and the [`resignActive()`](clscontext/resignactive().md) method to deactivate it.

## See Also

- [Informing ClassKit that a task is about to begin](informing-classkit-that-a-task-is-about-to-begin.md)
  Activate and deactivate contexts according to user interaction.
- [func becomeActive()](clscontext/becomeactive.md)
  Tells a context to become the active context.
- [func resignActive()](clscontext/resignactive.md)
  Tells a context to stop being the active context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/isactive)*