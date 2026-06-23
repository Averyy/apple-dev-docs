# delegate

**Framework**: AppKit  
**Kind**: property

The delegate of the text selection manager.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
weak var delegate: (any NSTextSelectionManager.Delegate)? { get set }
```

#### Discussion

The delegate is responsible for storing the current text selection and responding to selection-related events.

## See Also

- [NSTextSelectionManager.Delegate](nstextselectionmanager/delegate-swift.protocol.md)
  A set of methods that manage text selection state and let you customize selection behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.property)*