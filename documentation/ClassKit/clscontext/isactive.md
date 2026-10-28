# isActive

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign, readonly, getter=isActive) BOOL active;
```

## Discussion

Use the [`becomeActive()`](./becomeactive%28%29.md) method to activate a context, and the [`resignActive()`](./resignactive%28%29.md) method to deactivate it.

## See Also

### Activating and deactivating a context
- [Informing ClassKit that a task is about to begin](../informing-classkit-that-a-task-is-about-to-begin.md)
  Activate and deactivate contexts according to user interaction.
- [func becomeActive()](./becomeactive%28%29.md)
  Tells a context to become the active context.
- [func resignActive()](./resignactive%28%29.md)
  Tells a context to stop being the active context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/isactive)*