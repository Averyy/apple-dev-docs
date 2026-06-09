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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.property)*