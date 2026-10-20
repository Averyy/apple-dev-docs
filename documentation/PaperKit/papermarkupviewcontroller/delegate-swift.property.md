# delegate

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The delegate for responding to a person’s actions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency weak var delegate: (any PaperMarkupViewController.Delegate)? { get set }
```

## See Also

### Responding to changes
- [PaperMarkupViewController.Delegate](./delegate-swift.protocol.md)
  The interface for responding to interactions in a markup view controller.
- [var undoManager: UndoManager?](./undomanager.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/delegate-swift.property)*