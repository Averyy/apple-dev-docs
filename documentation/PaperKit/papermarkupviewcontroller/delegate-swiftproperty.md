# delegate

**Framework**: PaperKit  
**Kind**: property

The delegate for responding to a person’s actions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency weak var delegate: (any PaperMarkupViewController.Delegate)? { get set }
```

## See Also

- [PaperMarkupViewController.Delegate](papermarkupviewcontroller/delegate-swift.protocol.md)
  The interface for responding to interactions in a markup view controller.
- [var undoManager: UndoManager?](papermarkupviewcontroller/undomanager.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.property)*